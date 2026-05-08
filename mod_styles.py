import sys

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add data-theme=dark
css = css.replace(''':root {
    --bg-color: #f5f5f5;
    --surface-color: #ffffff;
    --surface-border: rgba(0, 0, 0, 0.05);
    --text-primary: #1a1a1a;
    --text-secondary: #666666;
    --accent-1: #ff8a65;
    --accent-2: #4a90e2;
}''', ''':root {
    --bg-color: #f5f5f5;
    --surface-color: #ffffff;
    --surface-border: rgba(0, 0, 0, 0.05);
    --text-primary: #1a1a1a;
    --text-secondary: #666666;
    --accent-1: #ff8a65;
    --accent-2: #4a90e2;
}

[data-theme="dark"] {
    --bg-color: #0f0f11;
    --surface-color: #18181c;
    --surface-border: rgba(255, 255, 255, 0.08);
    --text-primary: #ffffff;
    --text-secondary: #9ca3af;
    --accent-1: #ff8a65;
    --accent-2: #60a5fa;
}''')

# Append styles for new components
new_styles = '''
/* Theme Toggle */
.theme-toggle {
    background: transparent;
    border: none;
    color: var(--text-primary);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    transition: background 0.3s;
}

.theme-toggle:hover {
    background: var(--surface-border);
}

.theme-toggle .moon-icon {
    display: none;
}

[data-theme="dark"] .theme-toggle .sun-icon {
    display: none;
}

[data-theme="dark"] .theme-toggle .moon-icon {
    display: block;
}

[data-theme="dark"] .nav-pill {
    background: rgba(24, 24, 28, 0.85);
}

[data-theme="dark"] .noise-overlay {
    opacity: 0.03;
}

/* Portfolio Filters */
.portfolio-filters {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 4rem;
    flex-wrap: wrap;
}

.filter-btn {
    background: transparent;
    border: 1px solid var(--surface-border);
    color: var(--text-secondary);
    padding: 0.8rem 1.5rem;
    border-radius: 50px;
    font-family: inherit;
    font-size: 0.95rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
}

.filter-btn:hover {
    border-color: var(--text-primary);
    color: var(--text-primary);
}

.filter-btn.active {
    background: var(--text-primary);
    color: var(--bg-color);
    border-color: var(--text-primary);
}

.portfolio-grid {
    display: flex;
    flex-direction: column;
}

/* Hidden elements for filtering */
.product-card.hidden {
    display: none;
}

/* Parallax Image */
.parallax-img {
    transition: transform 0.1s ease-out;
}

/* Magnetic Button Base */
.magnetic-btn {
    position: relative;
    display: inline-block;
}
'''

css += new_styles

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
