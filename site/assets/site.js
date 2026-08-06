(() => {
  const form = document.querySelector("#catalog-controls");
  const grid = document.querySelector("#tool-grid");
  const resultLabel = document.querySelector("#catalog-results");
  const emptyState = document.querySelector("#catalog-empty");

  if (!(form instanceof HTMLFormElement) || !(grid instanceof HTMLElement)) {
    return;
  }

  const search = form.elements.namedItem("q");
  const category = form.elements.namedItem("category");
  const status = form.elements.namedItem("status");
  const sort = form.elements.namedItem("sort");
  const cards = Array.from(grid.querySelectorAll(".tool-card"));
  let pendingResetFrame = null;

  if (
    !(search instanceof HTMLInputElement) ||
    !(category instanceof HTMLSelectElement) ||
    !(status instanceof HTMLSelectElement) ||
    !(sort instanceof HTMLSelectElement)
  ) {
    return;
  }

  const normalized = (value) => value.trim().toLocaleLowerCase();
  const numberValue = (card, key) => Number(card.dataset[key] || 0);
  const dateValue = (card) => Date.parse(card.dataset.updated || "") || 0;

  const comparators = {
    rank: (left, right) => numberValue(left, "rank") - numberValue(right, "rank"),
    stars: (left, right) =>
      numberValue(right, "stars") - numberValue(left, "stars") ||
      (left.dataset.name || "").localeCompare(right.dataset.name || ""),
    updated: (left, right) =>
      dateValue(right) - dateValue(left) ||
      (left.dataset.name || "").localeCompare(right.dataset.name || ""),
    name: (left, right) =>
      (left.dataset.name || "").localeCompare(right.dataset.name || ""),
  };

  const updateAddress = () => {
    const params = new URLSearchParams();
    if (search.value.trim()) params.set("q", search.value.trim());
    if (category.value) params.set("category", category.value);
    if (status.value) params.set("status", status.value);
    if (sort.value !== "rank") params.set("sort", sort.value);

    const url = new URL(window.location.href);
    url.search = params.toString();
    window.history.replaceState(null, "", url);
  };

  const applyFilters = ({ updateUrl = true } = {}) => {
    const query = normalized(search.value);
    const selectedCategory = category.value;
    const selectedStatus = status.value;
    let visibleCount = 0;

    for (const card of cards) {
      const matchesSearch = !query || (card.dataset.search || "").includes(query);
      const matchesCategory = !selectedCategory || card.dataset.category === selectedCategory;
      const matchesStatus = !selectedStatus || card.dataset.status === selectedStatus;
      const visible = matchesSearch && matchesCategory && matchesStatus;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    }

    const comparator = comparators[sort.value] || comparators.rank;
    for (const card of [...cards].sort(comparator)) {
      grid.append(card);
    }

    if (resultLabel) {
      resultLabel.textContent = `Showing ${visibleCount} ${visibleCount === 1 ? "tool" : "tools"}`;
    }
    if (emptyState) {
      emptyState.hidden = visibleCount !== 0;
    }
    if (updateUrl) {
      updateAddress();
    }
  };

  const selectHasValue = (select, value) =>
    Array.from(select.options).some((option) => option.value === value);

  const restoreFromAddress = () => {
    const params = new URLSearchParams(window.location.search);
    search.value = params.get("q") || "";

    const requestedCategory = params.get("category") || "";
    if (selectHasValue(category, requestedCategory)) category.value = requestedCategory;

    const requestedStatus = params.get("status") || "";
    if (selectHasValue(status, requestedStatus)) status.value = requestedStatus;

    const requestedSort = params.get("sort") || "rank";
    if (selectHasValue(sort, requestedSort)) sort.value = requestedSort;
  };

  form.addEventListener("submit", (event) => event.preventDefault());
  form.addEventListener("input", () => applyFilters());
  form.addEventListener("change", () => applyFilters());
  const applyResetNow = () => {
    if (pendingResetFrame !== null) {
      window.cancelAnimationFrame(pendingResetFrame);
      pendingResetFrame = null;
    }
    applyFilters();
  };

  form.addEventListener("reset", () => {
    pendingResetFrame = window.requestAnimationFrame(() => {
      pendingResetFrame = null;
      applyFilters();
    });
  });

  document.querySelectorAll("[data-reset-catalog]").forEach((button) => {
    button.addEventListener("click", () => {
      form.reset();
      search.focus();
    });
  });

  document.querySelectorAll('a[href^="#tool-"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      const fragment = link.getAttribute("href");
      const target = fragment ? document.getElementById(fragment.slice(1)) : null;
      if (target?.hidden) {
        event.preventDefault();
        form.reset();
        applyResetNow();

        const url = new URL(window.location.href);
        url.hash = fragment;
        const method = window.location.hash === fragment ? "replaceState" : "pushState";
        window.history[method](null, "", url);
        target.scrollIntoView({ block: "start" });
      }
    });
  });

  restoreFromAddress();
  applyFilters({ updateUrl: false });
})();
