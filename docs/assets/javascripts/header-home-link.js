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

function wwcaMarkExternalLinks() {
  const contentLinks = document.querySelectorAll(".md-content a[href]");

  for (const link of contentLinks) {
    const href = link.getAttribute("href");
    if (!href) {
      continue;
    }

    if (
      href.startsWith("#") ||
      href.startsWith("mailto:") ||
      href.startsWith("tel:")
    ) {
      continue;
    }

    let targetUrl;
    try {
      targetUrl = new URL(href, window.location.origin);
    } catch (_error) {
      continue;
    }

    if (targetUrl.origin === window.location.origin) {
      continue;
    }

    link.classList.add("wwca-external-link");

    const existingRel = (link.getAttribute("rel") || "")
      .split(/\s+/)
      .filter(Boolean);
    const relSet = new Set(existingRel);
    relSet.add("external");
    relSet.add("nofollow");
    relSet.add("noopener");
    relSet.add("noreferrer");
    link.setAttribute("rel", Array.from(relSet).join(" "));
  }
}

function wwcaApplyEnhancements() {
  wwcaMakeHeaderTitleClickable();
  wwcaMarkExternalLinks();
}

if (typeof window.document$ !== "undefined") {
  window.document$.subscribe(wwcaApplyEnhancements);
} else {
  document.addEventListener("DOMContentLoaded", wwcaApplyEnhancements);
}
