/* @ds-bundle: {"format":4,"namespace":"DHKDesignSystem_c5bcb5","components":[{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Card","sourcePath":"components/core/Card.jsx"},{"name":"FeatureGrid","sourcePath":"components/core/FeatureGrid.jsx"},{"name":"FeatureCard","sourcePath":"components/core/FeatureGrid.jsx"},{"name":"Meta","sourcePath":"components/core/Meta.jsx"},{"name":"NavLink","sourcePath":"components/core/NavLink.jsx"},{"name":"PostHeader","sourcePath":"components/core/PostHeader.jsx"},{"name":"PullQuote","sourcePath":"components/core/PullQuote.jsx"},{"name":"SectionDivider","sourcePath":"components/core/SectionDivider.jsx"},{"name":"Tag","sourcePath":"components/core/Tag.jsx"}],"sourceHashes":{"components/core/Button.jsx":"dd2f39a842c1","components/core/Card.jsx":"86bed7d17621","components/core/FeatureGrid.jsx":"a95faa220c69","components/core/Meta.jsx":"ad60616876cc","components/core/NavLink.jsx":"81e854589258","components/core/PostHeader.jsx":"c84a5b4381a4","components/core/PullQuote.jsx":"508daf705579","components/core/SectionDivider.jsx":"d660bcf42f1b","components/core/Tag.jsx":"f05021f63188","ui_kits/dhk-website/Chrome.jsx":"9b2310c6e30f","ui_kits/dhk-website/Screens.jsx":"c4c35c1e57c9","ui_kits/dhk-website/data.js":"c64d6f30d4e0"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.DHKDesignSystem_c5bcb5 = window.DHKDesignSystem_c5bcb5 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/core/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Button — DHK's mono-chrome action control.
 * Two variants: solid Electric Cobalt (`primary`) and outlined (`ghost`).
 * Label is always mono, uppercase, tracked — never sentence case.
 */
function Button({
  variant = "primary",
  as = "button",
  children,
  style,
  ...rest
}) {
  const base = {
    fontFamily: "var(--font-mono)",
    fontSize: "var(--fs-tag)",
    fontWeight: 500,
    textTransform: "uppercase",
    letterSpacing: "var(--ls-nav)",
    padding: "var(--sp3) var(--sp5)",
    borderRadius: "var(--radius)",
    cursor: "pointer",
    display: "inline-block",
    lineHeight: 1,
    transition: "opacity 0.15s, border-color 0.15s, color 0.15s",
    textDecoration: "none"
  };
  const variants = {
    primary: {
      background: "var(--accent)",
      color: "#fff",
      border: "1px solid var(--accent)"
    },
    ghost: {
      background: "transparent",
      color: "var(--text-muted)",
      border: "1px solid var(--border)"
    }
  };
  const Tag = as;
  return /*#__PURE__*/React.createElement(Tag, _extends({
    style: {
      ...base,
      ...variants[variant],
      ...style
    },
    onMouseEnter: e => {
      if (variant === "primary") e.currentTarget.style.opacity = "0.85";else {
        e.currentTarget.style.borderColor = "var(--accent)";
        e.currentTarget.style.color = "var(--text)";
      }
    },
    onMouseLeave: e => {
      if (variant === "primary") e.currentTarget.style.opacity = "1";else {
        e.currentTarget.style.borderColor = "var(--border)";
        e.currentTarget.style.color = "var(--text-muted)";
      }
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/FeatureGrid.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * FeatureGrid — the DHK "border-gap" grid. Cells sit on a 1px gap that
 * shows the parent's border colour, giving hairline dividers with no
 * per-cell borders. Auto-fills columns at a 220px minimum.
 */
function FeatureGrid({
  minColWidth = 220,
  children,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      display: "grid",
      gridTemplateColumns: `repeat(auto-fill, minmax(${minColWidth}px, 1fr))`,
      gap: "1px",
      background: "var(--border)",
      border: "1px solid var(--border)",
      borderRadius: "var(--radius)",
      overflow: "hidden",
      ...style
    }
  }, rest), children);
}

/** A single cell of a FeatureGrid. Title is cobalt 13px; body is muted 14px. */
function FeatureCard({
  title,
  children,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      background: "var(--bg)",
      padding: "var(--sp5)",
      transition: "background 0.15s",
      ...style
    },
    onMouseEnter: e => {
      e.currentTarget.style.background = "var(--bg3)";
    },
    onMouseLeave: e => {
      e.currentTarget.style.background = "var(--bg)";
    }
  }, rest), title && /*#__PURE__*/React.createElement("h3", {
    style: {
      fontSize: "13px",
      fontWeight: 600,
      color: "var(--accent)",
      marginBottom: "var(--sp2)"
    }
  }, title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-sm)",
      color: "var(--text-muted)",
      lineHeight: "var(--lh-snug)",
      margin: 0
    }
  }, children));
}
Object.assign(__ds_scope, { FeatureGrid, FeatureCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/FeatureGrid.jsx", error: String((e && e.message) || e) }); }

// components/core/Meta.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Meta — mono metadata line: dates, labels, breadcrumbs, counts.
 * Use `accent` to colour it Electric Cobalt (breadcrumbs), otherwise it
 * reads in --text-dim.
 */
function Meta({
  accent = false,
  children,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-meta)",
      letterSpacing: "var(--ls-meta)",
      color: accent ? "var(--accent)" : "var(--text-dim)",
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Meta });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Meta.jsx", error: String((e && e.message) || e) }); }

// components/core/NavLink.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * NavLink — header navigation item. Mono, uppercase, tracked, 11px.
 * Dim by default, darkens on hover, and turns Electric Cobalt with an
 * underline when `active`.
 */
function NavLink({
  active = false,
  children,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("a", _extends({
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-tag)",
      textTransform: "uppercase",
      letterSpacing: "var(--ls-nav)",
      color: active ? "var(--accent)" : "var(--text-dim)",
      borderBottom: active ? "2px solid var(--accent)" : "2px solid transparent",
      paddingBottom: "2px",
      transition: "color 0.15s",
      ...style
    },
    onMouseEnter: e => {
      if (!active) e.currentTarget.style.color = "var(--text)";
    },
    onMouseLeave: e => {
      if (!active) e.currentTarget.style.color = "var(--text-dim)";
    }
  }, rest), children);
}
Object.assign(__ds_scope, { NavLink });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/NavLink.jsx", error: String((e && e.message) || e) }); }

// components/core/PostHeader.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * PostHeader — the article / product-page header block. A cobalt breadcrumb,
 * a large title, an optional lead excerpt, closed by a bottom hairline.
 * Mirrors the site's `.post-header` pattern.
 */
function PostHeader({
  breadcrumb,
  title,
  excerpt,
  children,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("header", _extends({
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp4)",
      paddingTop: "var(--sp7)",
      paddingBottom: "var(--sp6)",
      borderBottom: "1px solid var(--border)",
      marginBottom: "var(--sp6)",
      ...style
    }
  }, rest), breadcrumb && /*#__PURE__*/React.createElement(__ds_scope.Meta, {
    accent: true
  }, breadcrumb), children /* optional tag/date row */, title && /*#__PURE__*/React.createElement("h1", {
    style: {
      fontSize: "clamp(34px, 4.5vw, 52px)"
    }
  }, title), excerpt && /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-lead)",
      color: "var(--text-dim)",
      lineHeight: 1.65,
      maxWidth: 720,
      margin: 0
    }
  }, excerpt));
}
Object.assign(__ds_scope, { PostHeader });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/PostHeader.jsx", error: String((e && e.message) || e) }); }

// components/core/PullQuote.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * PullQuote — accent left-border quotation. Italic, muted, slightly larger
 * than body. The site's `.prose blockquote` / `.pull-quote` pattern.
 */
function PullQuote({
  cite,
  children,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("blockquote", _extends({
    style: {
      borderLeft: "3px solid var(--accent)",
      paddingLeft: "var(--sp5)",
      margin: "var(--sp6) 0",
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp2)",
      ...style
    }
  }, rest), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-lead)",
      lineHeight: 1.6,
      fontStyle: "italic",
      color: "var(--text-muted)",
      margin: 0
    }
  }, children), cite && /*#__PURE__*/React.createElement("cite", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-meta)",
      fontStyle: "normal",
      color: "var(--text-dim)",
      letterSpacing: "var(--ls-meta)"
    }
  }, cite));
}
Object.assign(__ds_scope, { PullQuote });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/PullQuote.jsx", error: String((e && e.message) || e) }); }

// components/core/SectionDivider.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * SectionDivider — a mono label on the left with a hairline rule running
 * to the right edge. The DHK site's primary way of opening a section.
 */
function SectionDivider({
  children,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      display: "flex",
      alignItems: "center",
      gap: "20px",
      padding: "var(--sp7) 0 var(--sp6)",
      borderTop: "1px solid var(--border)",
      ...style
    }
  }, rest), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-tag)",
      color: "var(--text-dim)",
      textTransform: "uppercase",
      letterSpacing: "var(--ls-nav)",
      whiteSpace: "nowrap"
    }
  }, children), /*#__PURE__*/React.createElement("span", {
    style: {
      flex: 1,
      height: "1px",
      background: "var(--border)"
    }
  }));
}
Object.assign(__ds_scope, { SectionDivider });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/SectionDivider.jsx", error: String((e && e.message) || e) }); }

// components/core/Tag.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const TINTS = {
  essay: {
    background: "var(--tint-essay)",
    color: "var(--accent)"
  },
  commentary: {
    background: "var(--tint-commentary)",
    color: "var(--accent-purple)"
  },
  tool: {
    background: "var(--tint-tool)",
    color: "var(--accent-purple)"
  },
  study: {
    background: "var(--tint-study)",
    color: "var(--accent-teal)"
  },
  project: {
    background: "var(--tint-project)",
    color: "var(--accent-orange)"
  }
};

/**
 * Tag — content-type pill. Mono, uppercase, tracked, tinted by kind.
 * The tint is a ~10% alpha of the semantic accent for that content type.
 */
function Tag({
  kind = "essay",
  children,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-tag)",
      textTransform: "uppercase",
      letterSpacing: "var(--ls-tag)",
      padding: "3px 8px",
      borderRadius: "var(--radius)",
      display: "inline-block",
      whiteSpace: "nowrap",
      lineHeight: 1.4,
      ...TINTS[kind],
      ...style
    }
  }, rest), children ?? kind);
}
Object.assign(__ds_scope, { Tag });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Tag.jsx", error: String((e && e.message) || e) }); }

// components/core/Card.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Card — the DHK content-list surface. Background lifts to --bg3 on hover
 * and shows an accent focus ring when tabbed to. Used identically across
 * writing, work, and signal lists (keep DRY).
 *
 * Pass `title`/`excerpt`/`tagKind`/`date` for the standard content row,
 * or pass `children` to use it as a bare hover surface.
 */
function Card({
  as = "article",
  title,
  excerpt,
  tagKind,
  tagLabel,
  date,
  href,
  children,
  style,
  ...rest
}) {
  const Tag_ = href ? "a" : as;
  const surface = {
    display: "block",
    background: "var(--bg)",
    borderBottom: "1px solid var(--border)",
    padding: "var(--sp5) 0",
    transition: "background 0.15s",
    color: "inherit",
    ...style
  };
  const hover = on => e => {
    e.currentTarget.style.background = on ? "var(--bg3)" : "var(--bg)";
  };
  return /*#__PURE__*/React.createElement(Tag_, _extends({
    href: href,
    style: surface,
    onMouseEnter: hover(true),
    onMouseLeave: hover(false)
  }, rest), children ?? /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp2)",
      paddingInline: "var(--sp4)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: "var(--sp3)"
    }
  }, tagKind && /*#__PURE__*/React.createElement(__ds_scope.Tag, {
    kind: tagKind
  }, tagLabel), date && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-meta)",
      color: "var(--text-dim)",
      letterSpacing: "var(--ls-meta)"
    }
  }, date)), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontSize: var_h3,
      fontWeight: 600,
      color: "var(--text)"
    }
  }, title), excerpt && /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-sm)",
      color: "var(--text-muted)",
      lineHeight: "var(--lh-snug)",
      margin: 0
    }
  }, excerpt)));
}
const var_h3 = "var(--fs-h3)";
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Card.jsx", error: String((e && e.message) || e) }); }

// ui_kits/dhk-website/Chrome.jsx
try { (() => {
// DHK website — shared chrome (Header + Footer). Composes DS components.
const DS = window.DHKDesignSystem_c5bcb5;
function Wordmark({
  size = 22,
  onClick
}) {
  return /*#__PURE__*/React.createElement("a", {
    href: "#",
    onClick: onClick,
    style: {
      display: "flex",
      alignItems: "center",
      gap: 9,
      textDecoration: "none"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      width: 7,
      height: 7,
      borderRadius: "50%",
      background: "var(--accent)",
      flexShrink: 0
    }
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 700,
      fontSize: size,
      letterSpacing: "-0.02em",
      color: "var(--text)"
    }
  }, "DHK"));
}
const NAV = [{
  key: "writing",
  label: "Writing"
}, {
  key: "lab",
  label: "Lab"
}, {
  key: "listen",
  label: "Listen"
}, {
  key: "signal",
  label: "Signal"
}, {
  key: "about",
  label: "About"
}];
function Header({
  route,
  go
}) {
  return /*#__PURE__*/React.createElement("header", {
    style: {
      position: "sticky",
      top: 0,
      zIndex: 50,
      height: "var(--header-height)",
      background: "rgba(245,246,250,0.88)",
      backdropFilter: "blur(10px)",
      borderBottom: "1px solid var(--border)",
      display: "flex",
      alignItems: "center"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--max-width)",
      margin: "0 auto",
      padding: "0 var(--sp5)",
      width: "100%",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between"
    }
  }, /*#__PURE__*/React.createElement(Wordmark, {
    onClick: e => {
      e.preventDefault();
      go("home");
    }
  }), /*#__PURE__*/React.createElement("nav", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: "var(--sp7)"
    }
  }, NAV.map(n => /*#__PURE__*/React.createElement(DS.NavLink, {
    key: n.key,
    href: "#",
    active: route === n.key || route === "article" && n.key === "writing",
    onClick: e => {
      e.preventDefault();
      go(n.key);
    }
  }, n.label)))));
}
function Footer({
  go
}) {
  return /*#__PURE__*/React.createElement("footer", {
    style: {
      borderTop: "1px solid var(--border)",
      padding: "var(--sp6) 0",
      marginTop: "var(--sp10)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--max-width)",
      margin: "0 auto",
      padding: "0 var(--sp5)",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between"
    }
  }, /*#__PURE__*/React.createElement(Wordmark, {
    size: 18,
    onClick: e => {
      e.preventDefault();
      go("home");
    }
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-meta)",
      color: "var(--text-dim)",
      letterSpacing: "var(--ls-meta)"
    }
  }, "Thinking, made portable. \xA9 2026 \xB7 dhk.io")));
}
Object.assign(window, {
  Wordmark,
  Header,
  Footer,
  NAV
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/dhk-website/Chrome.jsx", error: String((e && e.message) || e) }); }

// ui_kits/dhk-website/Screens.jsx
try { (() => {
// DHK website — page views. Each composes DS primitives + chrome.
const _DS = window.DHKDesignSystem_c5bcb5;
const D = () => window.DHK_DATA;
function Container({
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--max-width)",
      margin: "0 auto",
      padding: "0 var(--sp5)",
      ...style
    }
  }, children);
}

// Shared content-list (writing / signal)
function PostList({
  items,
  go
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column"
    }
  }, items.map((p, i) => /*#__PURE__*/React.createElement(_DS.Card, {
    key: i,
    href: "#",
    tagKind: p.type,
    tagLabel: p.tag,
    date: p.date,
    title: p.title,
    excerpt: p.excerpt,
    onClick: e => {
      e.preventDefault();
      go("article", p);
    }
  })));
}

// ---- HOME ----
function Home({
  go
}) {
  const d = D();
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("section", {
    style: {
      padding: "var(--sp10) 0 var(--sp8)"
    }
  }, /*#__PURE__*/React.createElement(Container, null, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 760,
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp5)"
    }
  }, /*#__PURE__*/React.createElement(_DS.Meta, {
    accent: true
  }, "DHK \xB7 Data, thinking & AI"), /*#__PURE__*/React.createElement("h1", null, "Thinking, made portable."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-lead)",
      color: "var(--text-dim)",
      lineHeight: 1.65,
      maxWidth: 620
    }
  }, "Essays, small tools, and field notes on doing real work with AI \u2014 where the leverage is, where the hype isn't, and what actually ships."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "var(--sp4)",
      marginTop: "var(--sp2)"
    }
  }, /*#__PURE__*/React.createElement(_DS.Button, {
    variant: "primary",
    as: "a",
    href: "#",
    onClick: e => {
      e.preventDefault();
      go("writing");
    }
  }, "Read the writing"), /*#__PURE__*/React.createElement(_DS.Button, {
    variant: "ghost",
    as: "a",
    href: "#",
    onClick: e => {
      e.preventDefault();
      go("lab");
    }
  }, "See the lab"))))), /*#__PURE__*/React.createElement(Container, null, /*#__PURE__*/React.createElement(_DS.SectionDivider, null, "Latest"), /*#__PURE__*/React.createElement(PostList, {
    items: d.writing.slice(0, 3),
    go: go
  }), /*#__PURE__*/React.createElement(_DS.SectionDivider, null, "From the lab"), /*#__PURE__*/React.createElement(_DS.FeatureGrid, {
    minColWidth: 260
  }, d.work.slice(0, 3).map((w, i) => /*#__PURE__*/React.createElement(_DS.FeatureCard, {
    key: i,
    title: w.title
  }, w.excerpt)))));
}

// ---- WRITING ----
function Writing({
  go
}) {
  const d = D();
  return /*#__PURE__*/React.createElement(Container, {
    style: {
      paddingTop: "var(--sp7)"
    }
  }, /*#__PURE__*/React.createElement(PageHead, {
    kicker: "Writing",
    title: "Essays & commentary",
    sub: "Long-form thinking on AI, data, and how work actually gets done."
  }), /*#__PURE__*/React.createElement(PostList, {
    items: d.writing,
    go: go
  }));
}

// ---- LAB ----
function Lab({
  go
}) {
  const d = D();
  return /*#__PURE__*/React.createElement(Container, {
    style: {
      paddingTop: "var(--sp7)"
    }
  }, /*#__PURE__*/React.createElement(PageHead, {
    kicker: "Lab",
    title: "Tools, studies & projects",
    sub: "Things built to test an idea. Most are working, not finished \u2014 that's the point."
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column"
    }
  }, d.work.map((w, i) => /*#__PURE__*/React.createElement(_DS.Card, {
    key: i,
    href: "#",
    tagKind: w.type,
    tagLabel: w.tag,
    date: w.date,
    title: w.title,
    excerpt: w.excerpt,
    onClick: e => {
      e.preventDefault();
      go("article", {
        ...w,
        isWork: true
      });
    }
  }))));
}

// ---- LISTEN ----
function Listen() {
  const d = D();
  return /*#__PURE__*/React.createElement(Container, {
    style: {
      paddingTop: "var(--sp7)"
    }
  }, /*#__PURE__*/React.createElement(PageHead, {
    kicker: "Listen",
    title: "Reading With Ears",
    sub: "Newsletters, turned into a daily podcast by an automated pipeline. Four shows, three fresh episodes most mornings."
  }), /*#__PURE__*/React.createElement("ul", {
    style: {
      listStyle: "none",
      display: "flex",
      flexDirection: "column",
      gap: 1,
      background: "var(--border)",
      border: "1px solid var(--border)",
      borderRadius: "var(--radius)",
      overflow: "hidden"
    }
  }, d.podcasts.map((ep, i) => /*#__PURE__*/React.createElement(EpisodeRow, {
    key: i,
    ep: ep
  }))));
}
function EpisodeRow({
  ep
}) {
  const [playing, setPlaying] = React.useState(false);
  return /*#__PURE__*/React.createElement("li", {
    onClick: () => setPlaying(p => !p),
    role: "button",
    tabIndex: 0,
    style: {
      display: "flex",
      alignItems: "center",
      gap: "var(--sp4)",
      padding: "var(--sp4) var(--sp5)",
      background: playing ? "var(--bg3)" : "var(--bg)",
      cursor: "pointer",
      transition: "background 0.15s"
    },
    onMouseEnter: e => {
      if (!playing) e.currentTarget.style.background = "var(--bg2)";
    },
    onMouseLeave: e => {
      if (!playing) e.currentTarget.style.background = "var(--bg)";
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      width: 30,
      height: 30,
      borderRadius: "50%",
      flexShrink: 0,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      background: playing ? "var(--accent)" : "var(--bg3)",
      color: playing ? "#fff" : "var(--text-dim)"
    }
  }, playing ? /*#__PURE__*/React.createElement("svg", {
    width: "9",
    height: "9",
    viewBox: "0 0 8 8"
  }, /*#__PURE__*/React.createElement("rect", {
    x: "1",
    y: "1",
    width: "2",
    height: "6",
    fill: "currentColor"
  }), /*#__PURE__*/React.createElement("rect", {
    x: "5",
    y: "1",
    width: "2",
    height: "6",
    fill: "currentColor"
  })) : /*#__PURE__*/React.createElement("svg", {
    width: "9",
    height: "9",
    viewBox: "0 0 8 8"
  }, /*#__PURE__*/React.createElement("polygon", {
    points: "1,1 7,4 1,7",
    fill: "currentColor"
  }))), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      display: "flex",
      flexDirection: "column",
      gap: 3
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "var(--sp3)",
      alignItems: "center"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: 11,
      textTransform: "uppercase",
      letterSpacing: "0.08em",
      color: "var(--accent)"
    }
  }, ep.show), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: 11,
      color: "var(--text-dim)"
    }
  }, ep.dur)), /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: "var(--fs-sm)",
      color: "var(--text)",
      fontWeight: 500
    }
  }, ep.title)));
}

// ---- SIGNAL ----
function Signal() {
  const d = D();
  return /*#__PURE__*/React.createElement(Container, {
    style: {
      paddingTop: "var(--sp7)"
    }
  }, /*#__PURE__*/React.createElement(PageHead, {
    kicker: "Signal",
    title: "Short takes",
    sub: "One idea, fully formed, no essay attached."
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp5)",
      maxWidth: 720
    }
  }, d.signal.map((s, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    style: {
      borderLeft: "3px solid var(--accent)",
      paddingLeft: "var(--sp5)",
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp3)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "var(--sp3)",
      alignItems: "center"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: 11,
      textTransform: "uppercase",
      letterSpacing: "0.08em",
      color: "var(--accent-purple)"
    }
  }, s.tag), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: 11,
      color: "var(--text-dim)"
    }
  }, s.date)), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-lead)",
      color: "var(--text-muted)",
      lineHeight: 1.6,
      margin: 0
    }
  }, s.content)))));
}

// ---- ABOUT ----
function About() {
  return /*#__PURE__*/React.createElement(Container, {
    style: {
      paddingTop: "var(--sp7)"
    }
  }, /*#__PURE__*/React.createElement(PageHead, {
    kicker: "About",
    title: "DHK",
    sub: "Independent work at the intersection of data, thinking, and AI tooling."
  }), /*#__PURE__*/React.createElement("div", {
    className: "prose",
    style: {
      maxWidth: "var(--prose-width)",
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp5)"
    }
  }, /*#__PURE__*/React.createElement("p", null, "DHK is a one-person studio. The output is essays, small sharp tools, and the occasional data study \u2014 all pointed at the same question: how do you actually get leverage from AI, past the demo?"), /*#__PURE__*/React.createElement("p", null, "The bias here is toward ", /*#__PURE__*/React.createElement("em", null, "equipping"), " over impressing. A tool that runs every morning without being asked beats a slide that wows a room once. Most things shipped here are working, not finished \u2014 and they say so."), /*#__PURE__*/React.createElement(_DS.SectionDivider, null, "Elsewhere"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "var(--sp4)"
    }
  }, /*#__PURE__*/React.createElement(_DS.Button, {
    variant: "ghost",
    as: "a",
    href: "#"
  }, "Substack \u2197"), /*#__PURE__*/React.createElement(_DS.Button, {
    variant: "ghost",
    as: "a",
    href: "#"
  }, "GitHub \u2197"))));
}

// ---- ARTICLE ----
function Article({
  post,
  go
}) {
  const p = post || D().writing[0];
  return /*#__PURE__*/React.createElement(Container, {
    style: {
      paddingTop: "var(--sp7)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--prose-width)",
      display: "flex",
      flexDirection: "column"
    }
  }, /*#__PURE__*/React.createElement("a", {
    href: "#",
    onClick: e => {
      e.preventDefault();
      go(p.isWork ? "lab" : "writing");
    },
    style: {
      marginBottom: "var(--sp4)"
    }
  }, /*#__PURE__*/React.createElement(_DS.Meta, {
    accent: true
  }, p.isWork ? "Lab" : "Writing", " /")), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: "var(--sp3)",
      marginBottom: "var(--sp4)"
    }
  }, /*#__PURE__*/React.createElement(_DS.Tag, {
    kind: p.type
  }, p.tag), /*#__PURE__*/React.createElement(_DS.Meta, null, p.date)), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontSize: "clamp(34px, 4vw, 46px)",
      marginBottom: "var(--sp5)"
    }
  }, p.title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-lead)",
      color: "var(--text-dim)",
      lineHeight: 1.65,
      marginBottom: "var(--sp7)"
    }
  }, p.excerpt), /*#__PURE__*/React.createElement("div", {
    className: "prose",
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp5)",
      borderTop: "1px solid var(--border)",
      paddingTop: "var(--sp6)"
    }
  }, /*#__PURE__*/React.createElement("p", null, "Most work in this space shares a hidden assumption: that the interesting part is the model. It isn't. The interesting part is the context you hand it and the shape of the problem you've defined."), /*#__PURE__*/React.createElement("h2", null, "What emerges"), /*#__PURE__*/React.createElement("p", null, "The structure is rarely random. The nodes that matter \u2014 the ones that hold everything together \u2014 are almost never the loudest. They're the connective tissue you only notice when they disappear."), /*#__PURE__*/React.createElement("blockquote", {
    style: {
      borderLeft: "3px solid var(--accent)",
      paddingLeft: "var(--sp5)",
      fontStyle: "italic",
      color: "var(--text-muted)"
    }
  }, "The most connected node is not always the most influential. The most critical node is often invisible until it's gone."), /*#__PURE__*/React.createElement("p", null, "That has real implications for how we build, measure, and govern these systems. The hard work is definitional, not political."))));
}

// Shared page header
function PageHead({
  kicker,
  title,
  sub
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp4)",
      paddingBottom: "var(--sp7)",
      borderBottom: "1px solid var(--border)",
      marginBottom: "var(--sp6)"
    }
  }, /*#__PURE__*/React.createElement(_DS.Meta, {
    accent: true
  }, kicker), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontSize: "clamp(34px, 4.5vw, 52px)"
    }
  }, title), sub && /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-lead)",
      color: "var(--text-dim)",
      lineHeight: 1.6,
      maxWidth: 640
    }
  }, sub));
}
Object.assign(window, {
  Home,
  Writing,
  Lab,
  Listen,
  Signal,
  About,
  Article,
  Container,
  PageHead
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/dhk-website/Screens.jsx", error: String((e && e.message) || e) }); }

// ui_kits/dhk-website/data.js
try { (() => {
// Content for the DHK website UI kit — drawn from the real site collections.
window.DHK_DATA = {
  writing: [{
    type: "essay",
    tag: "Essay",
    date: "Nov 15, 2024",
    title: "The Hidden Structure of Policy Networks",
    excerpt: "How lobbying coalitions self-organize — and what graph theory reveals about their durability.",
    featured: true
  }, {
    type: "commentary",
    tag: "Commentary",
    date: "Dec 3, 2024",
    title: "The AI Governance Gap Is a Measurement Problem",
    excerpt: "Every governance framework assumes we can measure what we're governing. We can't."
  }, {
    type: "essay",
    tag: "Essay",
    date: "Apr 7, 2026",
    title: "Showing vs. Shipping",
    excerpt: "Demos are impressive. Equipping is impactful.",
    substack: true
  }, {
    type: "essay",
    tag: "Essay",
    date: "Mar 30, 2026",
    title: "Writing Isn't Hard. Thinking Is.",
    excerpt: "The blank page isn't a writing problem. It's an unfinished-thinking problem."
  }, {
    type: "commentary",
    tag: "Commentary",
    date: "Mar 12, 2026",
    title: "Don't Let Your AI Session Eat Itself",
    excerpt: "Why long sessions degrade — and the discipline that keeps them sharp."
  }, {
    type: "essay",
    tag: "Essay",
    date: "Feb 20, 2026",
    title: "From Nouns to Verbs",
    excerpt: "How to make AI do things, not just say things."
  }],
  work: [{
    type: "tool",
    tag: "Tool",
    date: "May 29, 2026",
    title: "Twine",
    excerpt: "Pool LinkedIn connection exports from multiple people into a single force-directed network graph. Find your warmest path to anyone at any company.",
    tools: ["D3.js", "PapaParse", "HTML"],
    viz: "purple"
  }, {
    type: "tool",
    tag: "Tool",
    date: "Apr 18, 2026",
    title: "Captain's Log",
    excerpt: "A Claude skill that keeps a daily working diary — automatically. Not what you did. What it meant.",
    tools: ["Claude", "Markdown", "Git"],
    viz: "blue"
  }, {
    type: "tool",
    tag: "Tool",
    date: "Apr 5, 2026",
    title: "Reading With Ears",
    excerpt: "A personal AI pipeline that turns newsletters into a podcast — three episodes a day, fully automated.",
    tools: ["Claude", "NotebookLM", "Python"],
    viz: "orange"
  }, {
    type: "study",
    tag: "Study",
    date: "Mar 2, 2026",
    title: "The Life Expectancy Misconception",
    excerpt: "An interactive explorer of why 'people used to die at 40' is a statistical illusion.",
    tools: ["React", "Recharts", "D3"],
    viz: "teal"
  }, {
    type: "tool",
    tag: "Tool",
    date: "Feb 14, 2026",
    title: "Ivy — The Archive",
    excerpt: "A living, searchable vault built on top of Evernote exports.",
    tools: ["Python", "SQLite"],
    viz: "blue"
  }, {
    type: "tool",
    tag: "Tool",
    date: "Jan 22, 2026",
    title: "Tab Tamer",
    excerpt: "A browser extension that turns tab chaos into a focused reading queue.",
    tools: ["TypeScript", "Chrome API"],
    viz: "orange"
  }],
  signal: [{
    tag: "ai",
    date: "Mar 25, 2026",
    content: "Context windows don't degrade because the model forgets. They degrade because the model has to attend across a larger haystack to find the relevant needle. The symptom looks like forgetting. The mechanism is dilution."
  }, {
    tag: "methods",
    date: "Jan 15, 2026",
    content: "The prompt engineering hype cycle peaked around the idea that better outputs required magic phrasing. It mostly doesn't. It requires giving the model the context it needs. One frames the user as wizard, the other as architect."
  }, {
    tag: "ai",
    date: "Jan 3, 2026",
    content: "Confirmation bias in AI workflows isn't the model agreeing with you. It's you only noticing the runs where it did."
  }, {
    tag: "methods",
    date: "Dec 18, 2025",
    content: "Institutional memory has layers: what happened, why it happened, and what we decided not to do. Tools capture the first. Almost nothing captures the third."
  }, {
    tag: "policy",
    date: "Dec 1, 2025",
    content: "The EU AI Act's GPAI tier is the interesting one — it regulates capability, not use. That's a bet that capability is measurable. See the governance gap essay."
  }],
  podcasts: [{
    show: "Signal",
    title: "The measurement problem in AI governance",
    dur: "12 min"
  }, {
    show: "Threads",
    title: "Why long AI sessions degrade — and what's happening",
    dur: "14 min"
  }, {
    show: "The Stack",
    title: "Shipping vs. showing: equipping over demos",
    dur: "11 min"
  }, {
    show: "Vital Signs",
    title: "Reading the life-expectancy illusion",
    dur: "13 min"
  }]
};
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/dhk-website/data.js", error: String((e && e.message) || e) }); }

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.FeatureGrid = __ds_scope.FeatureGrid;

__ds_ns.FeatureCard = __ds_scope.FeatureCard;

__ds_ns.Meta = __ds_scope.Meta;

__ds_ns.NavLink = __ds_scope.NavLink;

__ds_ns.PostHeader = __ds_scope.PostHeader;

__ds_ns.PullQuote = __ds_scope.PullQuote;

__ds_ns.SectionDivider = __ds_scope.SectionDivider;

__ds_ns.Tag = __ds_scope.Tag;

})();
