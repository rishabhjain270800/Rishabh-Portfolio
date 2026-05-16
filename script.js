document.addEventListener("DOMContentLoaded", () => {
    // 1. Initialize Lenis Smooth Scrolling
    const lenis = new Lenis({
        duration: 1.2,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        direction: 'vertical',
        gestureDirection: 'vertical',
        smooth: true,
        mouseMultiplier: 1,
        smoothTouch: false,
        touchMultiplier: 2,
        infinite: false,
    });

    function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // 2. Custom Cursor Logic
    const cursor = document.querySelector('.custom-cursor');
    const hoverTargets = document.querySelectorAll('.hover-target');
    const projectItems = document.querySelectorAll('.project-item-tattoo');

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
    });

    hoverTargets.forEach(target => {
        target.addEventListener('mouseenter', () => {
            cursor.classList.add('active');
        });
        target.addEventListener('mouseleave', () => {
            cursor.classList.remove('active');
        });
    });

    // 3. Project Hover Reveal Logic
    const bgItems = document.querySelectorAll('.hover-bg-item');
    const projectList = document.getElementById('projectList');

    projectItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            // Expand cursor differently when over a project
            cursor.classList.remove('active');
            cursor.classList.add('active-bg');

            const index = item.getAttribute('data-index');
            
            // Remove active from all bgs
            bgItems.forEach(bg => bg.classList.remove('active'));
            
            // Add active to targeted bg
            const targetBg = document.getElementById(`bg-${index}`);
            if (targetBg) {
                targetBg.classList.add('active');
            }
        });

        item.addEventListener('mouseleave', () => {
            cursor.classList.remove('active-bg');
            // We do not immediately remove the active background so it doesn't flicker,
            // we let the parent container's mouseleave handle hiding it.
        });
    });

    // Hide background when leaving the entire list
    if(projectList) {
        projectList.addEventListener('mouseleave', () => {
            bgItems.forEach(bg => bg.classList.remove('active'));
        });
    }

    // Modal Logic & Data
    const projectData = [
        {
            title: "Study Abroad Platform",
            whatItDoes: "A complete study abroad ecosystem designed to simplify the student journey from discovery to admission. Includes University search, application tracking, and visa guidance.",
            contribution: [
                "Designed Student + Counselor dashboards",
                "Built interconnected workflows",
                "Created real-time tracking systems",
                "Defined structure for end-to-end journey"
            ],
            impact: [
                "Simplified a complex process into a guided experience",
                "Improved student engagement & task completion",
                "Enabled counselors to manage multiple students efficiently"
            ]
        },
        {
            title: "PropTech Sales Platform",
            whatItDoes: "A real estate sales and marketing platform focused on managing leads, nurturing prospects, and driving conversions.",
            contribution: [
                "Designed lead lifecycle & pipeline system",
                "Built Kanban-based task & deal tracking",
                "Created automation workflows",
                "Structured dashboards for sales insights"
            ],
            impact: [
                "Increased lead-to-conversion efficiency",
                "Reduced manual follow-ups through automation",
                "Improved visibility into sales pipeline"
            ]
        },
        {
            title: "Banking Engagement CRM",
            whatItDoes: "A consumer-facing customer engagement product and agent-facing CRM for a leading private sector bank. Enables personalised WhatsApp communication journeys.",
            contribution: [
                "Wrote PRD, defined use cases & wireframes",
                "Mapped end-to-end customer lifecycle",
                "Defined agent CRM workflows & triggers",
                "Collaborated with compliance & marketing"
            ],
            impact: [
                "Delivered personalised communication journeys at scale",
                "Streamlined lead assignment and escalations",
                "Bridged the gap between acquisition and conversion"
            ]
        },
        {
            title: "WhatsApp Automation Engine",
            whatItDoes: "A WhatsApp & Meta-based marketing automation platform enabling businesses to run and manage campaigns seamlessly.",
            contribution: [
                "Built campaign creation flows",
                "Designed Flow Builder for automation",
                "Structured template management system",
                "Worked on Meta integration & setup"
            ],
            impact: [
                "Enabled brands to scale WhatsApp marketing",
                "Reduced campaign execution time",
                "Improved customer engagement rates"
            ]
        },
        {
            title: "Omnichannel Execution Engine",
            whatItDoes: "An execution engine that allows brands to run campaigns across multiple channels (WhatsApp, SMS, Email).",
            contribution: [
                "Designed end-to-end campaign workflows",
                "Built automation journey logic",
                "Defined multi-channel integration",
                "Created engagement tracking dashboards"
            ],
            impact: [
                "Unified communication channels",
                "Improved campaign efficiency & personalization",
                "Enabled real-time engagement tracking"
            ]
        },
        {
            title: "Strategy & Insights Engine",
            whatItDoes: "Helps brands understand market trends, audience behavior, and shifts using data sources like search trends and social chatter.",
            contribution: [
                "Defined product flow and insight structure",
                "Designed dashboards for real-time insights",
                "Connected multiple data inputs into one system"
            ],
            impact: [
                "Reduced guesswork in marketing decisions",
                "Enabled faster strategy planning"
            ]
        },
        {
            title: "Content & Keyword Intelligence",
            whatItDoes: "A discovery engine where users explore content based on keywords & brands. Shows articles, trends, and keyword clusters.",
            contribution: [
                "Built the concept of brand-based content search",
                "Designed keyword-driven UI experience",
                "Structured content discovery logic"
            ],
            impact: [
                "Improved content strategy efficiency",
                "Helped teams identify high-performing themes"
            ]
        }
    ];

    const projectModal = document.getElementById('projectModal');
    const closeModal = document.getElementById('closeModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalWhatItDoes = document.getElementById('modalWhatItDoes');
    const modalContribution = document.getElementById('modalContribution');
    const modalImpact = document.getElementById('modalImpact');

    projectItems.forEach(item => {
        item.addEventListener('click', () => {
            const index = item.getAttribute('data-index');
            const data = projectData[index];
            
            modalTitle.textContent = data.title;
            modalWhatItDoes.textContent = data.whatItDoes;
            
            modalContribution.innerHTML = '';
            data.contribution.forEach(c => {
                const li = document.createElement('li');
                li.textContent = c;
                modalContribution.appendChild(li);
            });
            
            modalImpact.innerHTML = '';
            data.impact.forEach(i => {
                const li = document.createElement('li');
                li.textContent = i;
                modalImpact.appendChild(li);
            });

            projectModal.classList.add('active');
            lenis.stop(); // Prevent scrolling while modal is open
        });
    });

    closeModal.addEventListener('click', () => {
        projectModal.classList.remove('active');
        lenis.start();
    });

    // Close on click outside
    projectModal.addEventListener('click', (e) => {
        if (e.target === projectModal) {
            projectModal.classList.remove('active');
            lenis.start();
        }
    });

    // Make modal close button trigger cursor active state
    closeModal.addEventListener('mouseenter', () => cursor.classList.add('active'));
    closeModal.addEventListener('mouseleave', () => cursor.classList.remove('active'));

    // 4. GSAP & ScrollTrigger Setup
    gsap.registerPlugin(ScrollTrigger);
    lenis.on('scroll', ScrollTrigger.update);

    gsap.ticker.add((time)=>{
      lenis.raf(time * 1000)
    });
    gsap.ticker.lagSmoothing(0);

    // Hero Animation
    const heroTl = gsap.timeline();
    
    heroTl.to('.hero .line', {
        y: 0,
        duration: 1.2,
        stagger: 0.1,
        ease: 'power4.out',
        delay: 0.2
    })
    .fromTo('.fade-up', 
        { y: 30, opacity: 0 },
        { y: 0, opacity: 1, duration: 1, stagger: 0.2, ease: 'power3.out' },
        "-=0.8"
    );

    // Reveal Text on Scroll
    const revealTexts = document.querySelectorAll('.reveal-text');
    revealTexts.forEach(text => {
        gsap.to(text, {
            scrollTrigger: {
                trigger: text,
                start: "top 85%",
                toggleActions: "play none none reverse"
            },
            y: 0,
            opacity: 1,
            duration: 1,
            ease: 'power3.out'
        });
    });

    // Contact CTA
    const contactBtn = document.getElementById('contactBtn');
    if(contactBtn) {
        contactBtn.addEventListener('click', () => {
            window.location.href = "mailto:rishabhjain3615@gmail.com";
        });
    }
});
