import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Meta tags
content = content.replace(
    '<meta name="description" content="I build data-driven product ecosystems that help brands move from insights to execution.">',
    '''<meta name="description" content="I build data-driven product ecosystems that help brands move from insights to execution.">
    <!-- Open Graph -->
    <meta property="og:title" content="Rishabh Jain | Product Portfolio">
    <meta property="og:description" content="I build data-driven product ecosystems that help brands move from insights to execution.">
    <meta property="og:type" content="website">
    <script>
        if (localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.setAttribute('data-theme', 'dark');
        }
    </script>'''
)

# 2. Theme toggle
content = content.replace(
    '''            <div class="nav-socials">
                <a href="mailto:rishabhjain3615@gmail.com">Contact</a>
            </div>''',
    '''            <div class="nav-socials">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle Dark Mode">
                    <svg class="sun-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                    <svg class="moon-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                </button>
                <a href="mailto:rishabhjain3615@gmail.com" class="magnetic-btn">Contact</a>
            </div>'''
)

# 3. Hero actions magnetic
content = content.replace(
    '''<a href="#portfolio" class="btn-primary">View Selected Work</a>''',
    '''<a href="#portfolio" class="btn-primary magnetic-btn" aria-label="View Selected Work">View Selected Work</a>'''
).replace(
    '''<a href="https://www.linkedin.com/in/rishabh-jain-99a2b11ab/" target="_blank" rel="noopener noreferrer" class="btn-secondary linkedin-btn">LinkedIn Profile</a>''',
    '''<a href="https://www.linkedin.com/in/rishabh-jain-99a2b11ab/" target="_blank" rel="noopener noreferrer" class="btn-secondary linkedin-btn magnetic-btn" aria-label="LinkedIn Profile">LinkedIn Profile</a>'''
)

# 4. Filters
content = content.replace(
    '''<h2 class="section-title text-center fade-in">Products I've Built</h2>''',
    '''<h2 class="section-title text-center fade-in">Products I've Built</h2>
                
                <div class="portfolio-filters fade-in">
                    <button class="filter-btn active" data-filter="all">All</button>
                    <button class="filter-btn" data-filter="strategy">Strategy</button>
                    <button class="filter-btn" data-filter="execution">Execution</button>
                    <button class="filter-btn" data-filter="intelligence">Intelligence</button>
                </div>
                
                <div class="portfolio-grid">'''
)

# 5. Products attributes
p1 = re.sub(r'(<!-- Product 1: GradGlobe -->\s*<div class="product-card fade-in)(">)', r'\1" data-category="execution strategy">', content)
p1 = re.sub(r'(alt="GradGlobe Ecosystem")>', r'\1 loading="lazy" class="parallax-img">', p1)

p1 = re.sub(r'(<!-- Product 2: Real Estate Product -->\s*<div class="product-card fade-in)(">)', r'\1" data-category="execution">', p1)
p1 = re.sub(r'(alt="Real Estate Ecosystem Dashboard")>', r'\1 loading="lazy" class="parallax-img">', p1)

p1 = re.sub(r'(<!-- Product 3: Meta -->\s*<div class="product-card fade-in)(">)', r'\1" data-category="execution">', p1)
p1 = re.sub(r'(alt="WhatsApp Automation Engine")>', r'\1 loading="lazy" class="parallax-img">', p1)

p1 = re.sub(r'(<!-- Product 4: Pulse Engage -->\s*<div class="product-card fade-in)(">)', r'\1" data-category="execution">', p1)
p1 = re.sub(r'(alt="Pulse Engage Screen")>', r'\1 loading="lazy" class="parallax-img">', p1)

p1 = re.sub(r'(<!-- Product 5: Brand Book Tool -->\s*<div class="product-card fade-in)(">)', r'\1" data-category="intelligence strategy">', p1)
p1 = re.sub(r'(alt="Brand Book Tool Screen")>', r'\1 loading="lazy" class="parallax-img">', p1)

p1 = re.sub(r'(<!-- Product 6: Pulse Shift -->\s*<div class="product-card fade-in)(">)', r'\1" data-category="intelligence strategy">', p1)
p1 = re.sub(r'(alt="Pulse Shift Screen")>', r'\1 loading="lazy" class="parallax-img">', p1)

p1 = re.sub(r'(<!-- Product 7: Pulse Scout -->\s*<div class="product-card fade-in)(">)', r'\1" data-category="intelligence">', p1)
p1 = re.sub(r'(alt="Pulse Scout Screen")>', r'\1 loading="lazy" class="parallax-img">', p1)

p1 = re.sub(r'(<!-- Product 8: Pulse Plan -->\s*<div class="product-card fade-in)(">)', r'\1" data-category="strategy">', p1)
p1 = re.sub(r'(alt="Pulse Plan Screen")>', r'\1 loading="lazy" class="parallax-img">', p1)

# close portfolio-grid
p1 = p1.replace(
    '''            </div>\n        </section>''',
    '''                </div>\n            </div>\n        </section>'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(p1)
