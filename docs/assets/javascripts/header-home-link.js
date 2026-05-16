function wwcaMakeHeaderTitleClickable() {
  const logoLink = document.querySelector("a.md-header__button.md-logo[href]");
  if (!logoLink) {
    return;
  }

  const homeHref = logoLink.getAttribute("href");
  const siteNameNode = document.querySelector(
    ".md-header__title .md-header__topic:first-child .md-ellipsis"
  );

  if (!siteNameNode) {
    return;
  }

  if (siteNameNode.closest("a.wwca-header-home-link")) {
    return;
  }

  const homeLink = document.createElement("a");
  homeLink.className = "wwca-header-home-link";
  homeLink.href = homeHref;
  homeLink.setAttribute("aria-label", "Zur Startseite");

  const parent = siteNameNode.parentNode;
  parent.insertBefore(homeLink, siteNameNode);
  homeLink.appendChild(siteNameNode);
}

if (typeof window.document$ !== "undefined") {
  window.document$.subscribe(wwcaMakeHeaderTitleClickable);
} else {
  document.addEventListener("DOMContentLoaded", wwcaMakeHeaderTitleClickable);
}
