// 9. League Standings Switching Logic
function switchLeague(leagueId, tabElement) {
    // 1. Highlight the correct tab
    const tabs = document.querySelectorAll('.league-tab');
    tabs.forEach(tab => tab.classList.remove('active'));
    tabElement.classList.add('active');

    // 2. Switch Visibility of Tables
    const tables = document.querySelectorAll('.league-table-section');
    tables.forEach(table => {
        table.classList.remove('active');
        table.style.display = 'none';
    });
    
    const selectedTable = document.getElementById(leagueId);
    if(selectedTable) {
        selectedTable.classList.add('active');
        selectedTable.style.display = 'block';
    }

    // 3. Update Page Title and Contextual Content
    const pageTitle = document.getElementById('main-standings-title');
    const leaderName = document.getElementById('sidebar-leader-name');
    const leaderImg = document.getElementById('sidebar-leader-img');
    const leagueTag = document.getElementById('page-league-tag');

    if (leagueId === 'nbcpl') {
        pageTitle.innerText = "NBC Premier Standings";
        leagueTag.innerText = "NBC Premier League";
        leaderName.innerText = "Yanga SC";
        leaderImg.src = "images/yanga.jpg";
    } else if (leagueId === 'champ') {
        pageTitle.innerText = "Championship Table";
        leagueTag.innerText = "NBC Championship";
        leaderName.innerText = "Pamba SC";
        leaderImg.src = "images/Premier league.png"; // Placeholder
    } else if (leagueId === 'first') {
        pageTitle.innerText = "First League Standings";
        leagueTag.innerText = "First League Tier";
        leaderName.innerText = "Arusha FC";
        leaderImg.src = "images/Premier league.png"; // Placeholder
    } else if (leagueId === 'women') {
        pageTitle.innerText = "Women's League Table";
        leagueTag.innerText = "Women's Premier League";
        leaderName.innerText = "Simba Queens";
        leaderImg.src = "images/simba.jpg";
    }
}

// 10. Team Profile Logic
function openTeamProfile(teamId) {
    window.location.href = 'team-details.html?id=' + teamId;
}

function closeTeamProfile() {
    document.getElementById('team-profile-modal').style.display = 'none';
    document.body.style.overflow = 'auto';
}

// 11. Team Filter Logic
function switchTeamCategory(categoryId, element) {
    // Highlight sidebar
    const links = document.querySelectorAll('.f-link');
    links.forEach(l => l.classList.remove('active'));
    element.classList.add('active');

    console.log("Switching to competition: " + categoryId);
    // In a real app, this would fetch new clubs via AJAX
    // For now, we refresh the view to show it's interactive
    const grid = document.querySelector('.clubs-dashboard-grid');
    grid.style.opacity = '0.3';
    setTimeout(() => {
        grid.style.opacity = '1';
    }, 300);
}

function filterByRegion(regionId, element) {
    const links = document.querySelectorAll('.f-link');
    links.forEach(l => l.classList.remove('active'));
    element.classList.add('active');

    console.log("Filtering by region: " + regionId);
    const grid = document.querySelector('.clubs-dashboard-grid');
    grid.style.opacity = '0.3';
    setTimeout(() => {
        grid.style.opacity = '1';
    }, 300);
}

// 12. Player Profile Logic
function openPlayerProfile(playerId) {
    const modal = document.getElementById('player-profile-modal');
    const content = document.getElementById('player-profile-content');

    if(playerId === 'aziz-ki') {
        content.innerHTML = `
            <div style="display:grid; grid-template-columns: 350px 1fr; gap:60px;">
                <aside>
                    <div class="player-photo-wrapper" style="width:100%; height:auto; aspect-ratio:1; border-radius:25px; margin-bottom:30px;">
                        <img src="images/player.png" style="border-radius:25px;">
                    </div>
                    <div style="display:flex; flex-direction:column; gap:20px;">
                        <div class="side-module">
                            <span class="panel-heading"><i class="fa-solid fa-id-card"></i> Biography</span>
                            <div class="stat-line"><span>Nationality</span> <strong>Burkina Faso</strong></div>
                            <div class="stat-line"><span>Age</span> <strong>28 Years</strong></div>
                            <div class="stat-line"><span>Height</span> <strong>1.75 m</strong></div>
                            <div class="stat-line"><span>Foot</span> <strong>Left</strong></div>
                        </div>
                        <div class="side-module" style="background:linear-gradient(135deg, rgba(255,215,0,0.1), transparent);">
                            <span class="panel-heading" style="color:gold;"><i class="fa-solid fa-award"></i> Major Awards</span>
                            <div style="font-size:0.8rem; font-weight:800; margin-bottom:10px;"><i class="fa-solid fa-medal" style="color:gold;"></i> NBCPL Golden Boot (23/24)</div>
                            <div style="font-size:0.8rem; font-weight:800;"><i class="fa-solid fa-medal" style="color:gold;"></i> Player of the Season (22/23)</div>
                        </div>
                    </div>
                </aside>

                <div class="profile-main-data">
                    <div style="display:flex; justify-content:space-between; align-items:flex-end; border-bottom:1px solid var(--border-color); padding-bottom:30px; margin-bottom:40px;">
                        <div>
                            <span style="color:var(--primary); font-weight:950; letter-spacing:3px; font-size:0.75rem;">ATTACKING MIDFIELDER • #10</span>
                            <h1 style="font-size:4rem; font-weight:950; margin:5px 0;">STEPHANE AZIZ KI</h1>
                            <div style="display:flex; gap:25px; font-weight:800; font-size:0.9rem; color:var(--text-muted);">
                                <span><img src="images/yanga.jpg" style="height:20px; vertical-align:middle; margin-right:8px;"> Yanga SC</span>
                                <span><i class="fa-solid fa-star" style="color:gold;"></i> 8.9 Avg Rating</span>
                            </div>
                        </div>
                        <div style="text-align:right;">
                            <div style="font-size:3rem; font-weight:950; color:var(--primary); line-height:1;">18</div>
                            <div style="font-size:0.7rem; font-weight:900; color:var(--text-muted);">SEASON GOALS</div>
                        </div>
                    </div>

                    <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:25px; margin-bottom:50px;">
                        <div class="side-module" style="text-align:center;">
                            <span style="font-size:2rem; font-weight:950; display:block;">28</span>
                            <span style="font-size:0.6rem; font-weight:900; color:var(--text-muted); text-transform:uppercase;">Matches</span>
                        </div>
                        <div class="side-module" style="text-align:center;">
                            <span style="font-size:2rem; font-weight:950; display:block;">10</span>
                            <span style="font-size:0.6rem; font-weight:900; color:var(--text-muted); text-transform:uppercase;">Assists</span>
                        </div>
                        <div class="side-module" style="text-align:center;">
                            <span style="font-size:2rem; font-weight:950; display:block;">2,450</span>
                            <span style="font-size:0.6rem; font-weight:900; color:var(--text-muted); text-transform:uppercase;">Minutes Played</span>
                        </div>
                    </div>

                    <div style="margin-top:50px;">
                        <h3 class="panel-heading"><i class="fa-solid fa-clapperboard"></i> Performance Highlights</h3>
                        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
                            <video src="footall(1).mp4" style="width:100%; border-radius:20px; border:1px solid var(--border-color);" controls></video>
                            <video src="footall(4).mp4" style="width:100%; border-radius:20px; border:1px solid var(--border-color);" controls></video>
                        </div>
                    </div>

                    <div style="margin-top:50px;">
                        <h3 class="panel-heading"><i class="fa-solid fa-clock-rotate-left"></i> Transfer History</h3>
                        <div class="stats-snippet"><span>2022 - Present</span> <strong>Yanga SC</strong></div>
                        <div class="stats-snippet"><span>2020 - 2022</span> <strong>ASEC Mimosas (CIV)</strong></div>
                    </div>
                </div>
            </div>
        `;
    } else {
        content.innerHTML = `<h2 style="text-align:center; padding:100px;">Detailed Player Statistics for this profile are currently being calculated...</h2>`;
    }

    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closePlayerProfile() {
    document.getElementById('player-profile-modal').style.display = 'none';
    document.body.style.overflow = 'auto';
}

// 13. Player Filter Logic
function filterPlayersByClub(clubId, element) {
    const players = document.querySelectorAll('.player-card-pro');
    const gridContainer = document.querySelector('.players-dashboard');
    const playersGrid = document.getElementById('players-list-grid');
    const pageTitle = document.getElementById('main-players-title');
    const pageTag = document.getElementById('page-players-tag');
    
    // Toggling Elements
    const sideLeft = document.getElementById('players-side-left');
    const sideRight = document.getElementById('players-side-right');
    const potmSection = document.getElementById('players-potm-section');

    // Toggle Active State in Selector
    const chips = document.querySelectorAll('.club-filter-chip');
    chips.forEach(chip => chip.classList.remove('active'));
    if(element) element.classList.add('active');

    // Smooth transition
    playersGrid.style.opacity = '0.3';
    
    setTimeout(() => {
        // Update Titles and Visibility to simulate page change
        if(clubId === 'all') {
            pageTitle.innerText = "Official Player Database";
            pageTag.innerText = "Player Center";
            
            // Show sidebars and POTM
            if(sideLeft) sideLeft.style.display = 'flex';
            if(sideRight) sideRight.style.display = 'flex';
            if(potmSection) potmSection.style.display = 'flex';
            
            // Restore 3-column layout
            gridContainer.style.gridTemplateColumns = "280px 1fr 340px";
        } else {
            const clubName = element.innerText.trim();
            pageTitle.innerText = clubName + " | Player Squad";
            pageTag.innerText = clubName + " Center";

            // Hide sidebars and POTM for a focused view
            if(sideLeft) sideLeft.style.display = 'none';
            if(sideRight) sideRight.style.display = 'none';
            if(potmSection) potmSection.style.display = 'none';
            
            // Change to focused single column layout
            gridContainer.style.gridTemplateColumns = "1fr";
        }

        players.forEach(player => {
            if (clubId === 'all' || player.getAttribute('data-club') === clubId) {
                player.style.display = 'block';
            } else {
                player.style.display = 'none';
            }
        });
        playersGrid.style.opacity = '1';
    }, 250);

    console.log("Focused view activated for: " + clubId);
}

document.addEventListener('DOMContentLoaded', () => {

    // 0. Permanent Header Stability (Scroll Logic Removed)

    // 1. Theme Toggle
    const themeToggleBtns = [
        document.getElementById('theme-toggle'),
        document.getElementById('theme-toggle-mobile')
    ];
    const htmlElement = document.documentElement;
    const forceTheme = htmlElement.getAttribute('data-force-theme');

    let savedTheme = forceTheme || 'dark';
    if (!forceTheme) {
        try {
            savedTheme = localStorage.getItem('theme') || 'dark';
        } catch (e) {
            console.warn('localStorage is not accessible, defaulting to dark theme:', e);
        }
    }
    htmlElement.setAttribute('data-theme', savedTheme);
    updateThemeIcons(savedTheme);

    themeToggleBtns.forEach(btn => {
        if (btn) {
            btn.addEventListener('click', () => {
                const currentTheme = htmlElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'light' ? 'dark' : 'light';

                htmlElement.setAttribute('data-theme', newTheme);
                try {
                    localStorage.setItem('theme', newTheme);
                } catch (e) {
                    console.warn('localStorage is not accessible, cannot save theme choice:', e);
                }
                updateThemeIcons(newTheme);
            });
        }
    });

    function updateThemeIcons(theme) {
        themeToggleBtns.forEach(btn => {
            if (btn) {
                const themeIcon = btn.querySelector('i');
                if (themeIcon) {
                    if (theme === 'dark') {
                        themeIcon.classList.remove('fa-moon');
                        themeIcon.classList.add('fa-sun');
                    } else {
                        themeIcon.classList.remove('fa-sun');
                        themeIcon.classList.add('fa-moon');
                    }
                }
            }
        });
    }

    // 2. Scroll Animation Setup
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const elementsToReveal = document.querySelectorAll('.reveal-element');
    elementsToReveal.forEach((el, index) => {
        // Add a slight stagger delay to grid layout elements
        el.style.transitionDelay = `${index * 0.1}s`;
        observer.observe(el);
    });

    // 3. Robust Hero Slideshow (Unified & Fixed)
    const heroSlideshow = document.getElementById('hero-slideshow');
    const heroImages = [
        'images/Tuzo.JPG',
        'images/tuzo1.JPG',
        'images/tuzo2.JPG',
        'images/tuzo3.JPG'
    ];

    if (heroSlideshow) {
        // Create slide elements
        heroImages.forEach((imgUrl, index) => {
            const slide = document.createElement('div');
            slide.classList.add('hero-slide');
            if (index === 0) slide.classList.add('active');
            slide.style.backgroundImage = `url('${imgUrl}')`;
            heroSlideshow.appendChild(slide);
        });

        const slides = heroSlideshow.querySelectorAll('.hero-slide');
        let currentSlideIdx = 0;

        function nextSlide() {
            slides[currentSlideIdx].classList.remove('active');
            currentSlideIdx = (currentSlideIdx + 1) % slides.length;
            slides[currentSlideIdx].classList.add('active');
        }

        // Cycle through slides every 5 seconds
        setInterval(nextSlide, 5000);
    }

    // 4. Full-Screen Modern Mobile Menu Logic
    const mobileToggleBtn = document.getElementById('mobile-toggle-btn');
    const fullMenu = document.getElementById('full-menu');
    const closeMenuBtn = document.getElementById('close-menu-btn');

    function toggleMenu() {
        fullMenu.classList.toggle('active');
        // Prevent body scroll when menu is active
        if (fullMenu.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    }

    if (mobileToggleBtn && fullMenu && closeMenuBtn) {
        mobileToggleBtn.addEventListener('click', toggleMenu);
        closeMenuBtn.addEventListener('click', toggleMenu);

        // Close menu when a link is clicked
        const menuLinks = fullMenu.querySelectorAll('.main-nav-links a');
        menuLinks.forEach(link => {
            link.addEventListener('click', () => {
                fullMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Close menu when clicking outside the drawer
        fullMenu.addEventListener('click', (e) => {
            if (e.target === fullMenu) {
                toggleMenu();
            }
        });
    }

    // 5. Countdown Timer for Next Big Match
    const countdownElement = document.getElementById('countdown-timer');
    if (countdownElement) {
        // Set target date (e.g., 2 days from now for demo)
        const targetDate = new Date();
        targetDate.setDate(targetDate.getDate() + 2);
        targetDate.setHours(19, 0, 0);

        function updateCountdown() {
            const now = new Date().getTime();
            const distance = targetDate - now;

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));

            countdownElement.innerHTML = `
                <div class="time-block"><span>${days}</span>Days</div>
                <div class="time-block"><span>${hours}</span>Hours</div>
                <div class="time-block"><span>${minutes}</span>Min</div>
            `;

            if (distance < 0) {
                clearInterval(timerInterval);
                countdownElement.innerHTML = "MATCH LIVE";
            }
        }

        const timerInterval = setInterval(updateCountdown, 60000); // Update every minute
        updateCountdown(); // Initial call
    }
    // 6. TikTok Style Video Playback Logic
    const momentVideos = document.querySelectorAll('.moment-video');

    // Intersection Observer for videos (auto-play when in view)
    const videoObserverOptions = {
        threshold: 0.7 // Trigger when 70% of video is visible
    };

    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const video = entry.target;
            if (entry.isIntersecting) {
                video.play().catch(error => {
                    // Autoplay might be blocked by browser until user interacts
                    console.log("Autoplay prevented:", error);
                });
            } else {
                video.pause();
            }
        });
    }, videoObserverOptions);

    momentVideos.forEach(video => {
        videoObserver.observe(video);

        // Toggle Play/Pause on Click
        const container = video.parentElement;
        container.addEventListener('click', (e) => {
            // Prevent play/pause if clicking on actions sidebar or follow button
            if (e.target.closest('.mv-actions-sidebar') || e.target.closest('.mv-follow')) {
                return;
            }

            if (video.paused) {
                video.muted = false; // Unmute on first click for better experience
                video.play();
                container.classList.remove('video-paused');
            } else {
                video.pause();
                container.classList.add('video-paused');
            }
        });

        // Optional: Manual hover logic (Keeping it for desktop engagement)
        container.addEventListener('mouseenter', () => {
            if (video.paused && !container.classList.contains('video-paused')) {
                video.play();
            }
        });
    });

    // 7. Calendar View Toggle
    const calBtns = document.querySelectorAll('.cal-btn');
    calBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            calBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });

    // 8. Animate Record Watch progress bars on scroll
    const recordBars = document.querySelectorAll('.rec-fill');
    const recordObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.transition = 'width 1.5s ease';
                const width = entry.target.style.width;
                entry.target.style.width = '0%';
                setTimeout(() => { entry.target.style.width = width; }, 100);
                recordObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    recordBars.forEach(bar => recordObserver.observe(bar));

    // 9. Premium Dropdown Click Logic
    const dropdowns = document.querySelectorAll('.nav-item-dropdown');
    
    dropdowns.forEach(dropdown => {
        const toggle = dropdown.querySelector('a');
        
        toggle.addEventListener('click', (e) => {
            // Only stop default if on desktop navigation (or if you want same behavior on mobile)
            if (window.innerWidth > 1024) { 
                e.preventDefault();
                e.stopPropagation();

                const isActive = dropdown.classList.contains('active');

                // Close all other dropdowns
                dropdowns.forEach(d => d.classList.remove('active'));

                // Toggle this one
                if (!isActive) {
                    dropdown.classList.add('active');
                }
            }
        });

        // Close when clicking a sublink
        const subLinks = dropdown.querySelectorAll('.dropdown-menu a');
        subLinks.forEach(link => {
            link.addEventListener('click', () => {
                dropdown.classList.remove('active');
            });
        });
    });

    // Close dropdowns when clicking anywhere else on the document
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-item-dropdown')) {
            dropdowns.forEach(d => d.classList.remove('active'));
        }
    });

    // ==========================================
    // 14. Swahili Language Translation System
    // ==========================================
    const TRANSLATIONS = {
        // Navigation & Menu
        "home": "Nyumbani",
        "news": "Habari",
        "latest news": "Habari Mpya",
        "transfers": "Uhamisho",
        "interviews": "Mahojiano",
        "features": "Makala",
        "reports": "Taarifa",
        "videos": "Video",
        "matches": "Mechi",
        "fixtures": "Ratiba",
        "results": "Matokeo",
        "standings": "Msimamo",
        "live scores": "Matokeo Mubashara",
        "hub": "Kituo",
        "teams": "Timu",
        "players": "Wachezaji",
        "statistics": "Takwimu",
        "ligi kuu": "Ligi Kuu",
        "nbc premier league": "Ligi Kuu ya NBC",
        "championship": "Championship",
        "first league": "Ligi Daraja la Kwanza",
        "women's league": "Ligi ya Wanawake",
        "kanuni": "Kanuni za Mashindano",
        "board": "Bodi",
        "about board": "Kuhusu Bodi",
        "history": "Historia",
        "members": "Wajumbe",
        "secretariat": "Sekretarieti",
        "contact": "Wasiliana Nasi",
        "contact us": "Wasiliana Nasi",
        "member login": "Ingia Mwanachama",
        "search for players, matches, or news...": "Tafuta wachezaji, mechi, au habari...",
        "search...": "Tafuta...",
        "menu": "MENU",
        "fcms/cms login": "Ingia FCMS/CMS",
        "login": "Ingia",
        "register": "Jisajili",
        "privacy policy": "Sera ya Faragha",
        "terms of use": "Masharti ya Matumizi",
        "accessibility": "Upatikanaji",
        "stay updated": "Pata Habari Mpya",
        "subscribe": "Jiunge",
        "enter email": "Ingiza Barua Pepe",
        "tanzania football federation (tff). all rights reserved.": "Shirikisho la Mpira wa Miguu Tanzania (TFF). Haki zote zimehifadhiwa.",

        // index.html
        "welcome to tanzania football hub": "KARIBU KITUO CHA SOKA TANZANIA",
        "explore teams": "Gundua Timu",
        "view matches": "Angalia Mechi",
        "competitions": "Mashindano",
        "news & features": "Habari na Makala",
        "view more": "Angalia Zaidi",
        "view more quizzes": "Angalia Maswali Zaidi",
        "start quiz now": "Anza Maswali Sasa",
        "full season incawards": "Tuzo za Msimu Mzima",
        "player of the season": "Mchezaji Bora wa Msimu",
        "manager of the season": "Kocha Bora wa Msimu",
        "young player": "Mchezaji Kinda Bora",
        "goal of the season": "Goli Bora la Msimu",
        "save of the season": "Okoa Bora ya Msimu",
        "league table": "Msimamo wa Ligi",
        "view full table": "Angalia Msimamo Kamili",
        "club form guide": "Fomu ya Klabu",
        "recent form": "Fomu ya Hivi Karibuni",
        "view full form →": "Angalia Fomu Kamili →",
        "match predictions": "Utabiri wa Mechi",
        "vote now →": "Piga Kura Sasa →",
        "upcoming fixtures": "Ratiba Inayofuata",
        "view all fixtures": "Angalia Ratiba Zote",
        "unmissable moments 🔥": "Matukio ya Kusisimua 🔥",
        "test your knowledge": "PIMA MAARIFA YAKO",
        "how much do you know about tanzanian football history?": "Unajua kiasi gani kuhusu Historia ya Soka la Tanzania?",
        "transfer watch ⭐": "Ufuatiliaji wa Uhamisho ⭐",
        "on this day ⭐": "Siku kama ya Leo ⭐",
        "football calendar 📅": "Kalenda ya Soka 📅",
        "all competitions": "Mashindano Yote",
        "all clubs": "Klabu Zote",
        "day": "Siku",
        "week": "Wiki",
        "month": "Mwezi",
        "upcoming": "Inayokuja",
        "live": "MUBASHARA",
        "record watch 🏅": "Ufuatiliaji wa Rekodi 🏅",
        "most goals in a season": "Magoli Mengi Zaidi kwa Msimu",
        "most clean sheets": "Mechi Nyingi Bila Kuruhusu Goli",
        "longest winning streak": "Mfululizo Mrefu Zaidi wa Ushindi",
        "most assists": "Pasi Nyingi Zaidi za Magoli",
        "record: 30 goals by mbwana samatta (2018/19). 2 goals away!": "Rekodi: Mabao 30 ya Mbwana Samatta (2018/19). Mabao 2 yamebaki!",
        "record: 22 clean sheets (2016/17). 3 away!": "Rekodi: Mechi 22 bila kuruhusu bao (2016/17). Mechi 3 zamebaki!",
        "record: 18 consecutive wins (2014/15). 4 away!": "Rekodi: Ushindi 18 mfululizo (2014/15). Ushindi 4 umebaki!",
        "record: 17 assists by fiston mayele. 2 away!": "Rekodi: Pasi 17 za magoli za Fiston Mayele. Pasi 2 zimebaki!",
        "rumour": "Uvumi",
        "confirmed": "Imethibitishwa",
        "confidence": "Uhakika",
        "official news →": "Habari Rasmi →",
        "view details": "Angalia Maelezo",
        "did you forget something, stephane? ⚽️✨": "Je, umesahau kitu, Stephane? ⚽️✨",
        "all-access to every moment of yanga's win! 🏆": "Kila wakati wa ushindi wa Yanga! 🏆",
        "slo-mo: aziz ki's masterclass finish. pure class! 🎯": "Slo-Mo: Ufungaji bora wa Aziz Ki. Ustadi wa hali ya juu! 🎯",
        "matchday atmosphere is unreal! 🏟️✨": "Hali ya uwanja wa mechi ni ya kushangaza! 🏟️✨",
        "quiz: can you spot the ball?": "Maswali: Je, unaweza kuona mpira?",
        "quiz: which players' faces have we combined?": "Maswali: Tumeunganisha sura za wachezaji gani?",
        "quiz: guess the player from their baby photo": "Maswali: Mvue mchezaji kutoka picha yake ya utotoni",
        "quiz: can you match the player to the celebration?": "Maswali: Je, unaweza kulinganisha mchezaji na sherehe yake?",
        //news in home part//
        "One of the player who played in Tanzania appearing at fifa world cup 2026 by nation": "Moja ya Mchezaji mchezaji alie wai kucheza ligi ya Tanzania ataonekana kwenye Kombe la Dunia la FIFA 2026 kwa mataifa",
        "summer 2026: key football dates for your calendar": "Msimu wa joto 2026: Tarehe muhimu za soka kwenye kalenda yako",
        "when will the 2026/27 premier league fixtures be released?": "Je, ratiba za Ligi Kuu ya 2026/27 zitatolewa lini?",
        "ten reasons why 2025/26 was the most competitive season ever": "Sababu KUMI kwa nini 2025/26 ulikuwa msimu wa ushindani zaidi RATINGI",
        "revealed: premier league fan team of the season 2025/26": "Imefichuliwa: Timu ya mashabiki ya Ligi Kuu ya Msimu wa 2025/26",
        "crdb fa cup — round of 16": "Kombe la CRDB la FA — Raundi ya 16",
        "national stadium - ambience": "Uwanja wa Taifa - Mazingira",
        "stadium crowd roar": "Mngurumo wa Umati wa Uwanja",
        "yanga sc championship night": "Usiku wa Bingwa wa Yanga SC",
        "fresh content every day.": "Maudhui mapya kila siku.",
        "read more →": "Soma Zaidi →",
        "saturday | 16:00": "Jumamosi | 10:00 Jioni",

        // standings.html
        "nbc premier standings": "Msimamo wa Ligi Kuu ya NBC",
        "championship table": "Msimamo wa Championship",
        "first league standings": "Msimamo wa Ligi Daraja la Kwanza",
        "women's league table": "Msimamo wa Ligi ya Wanawake",
        "nbc premier": "Ligi Kuu ya NBC",
        "women's": "Ligi ya Wanawake",
        "live updates": "HABARI MUBASHARA",
        "season 2026/27 • matchday 28": "Msimu wa 2026/27 • Siku ya Mechi 28",
        "rank": "Nafasi",
        "club": "Klabu",
        "mp": "Mechi",
        "w": "W",
        "d": "D",
        "l": "L",
        "gf": "Goli-F",
        "ga": "Goli-A",
        "gd": "Tofauti",
        "pts": "Pointi",
        "cl slot": "Nafasi ya Klabu Bingwa",
        "confed cup": "Kombe la Shirikisho",
        "relegation": "Kushuka Daraja",
        "rules & regulations": "Kanuni na Sheria",
        "table leaders": "Viongozi wa Msimamo",
        "efficiency stats": "Takwimu za Ufanisi",
        "attack rating": "Kiwango cha Mashambulizi",
        "def. clean sheets": "Kuzuia Magoli",
        "home wins": "Ushindi wa Nyumbani",
        "danger zone": "Eneo la Hatari",
        "clubs in": "Klabu katika",
        "positions 15 & 16": "Nafasi ya 15 na 16",
        "will be automatically relegated to the championship.": "zitashuka daraja moja kwa moja hadi Championship.",

        // about.html
        "about board": "Kuhusu Bodi",
        "history of tplb": "Historia ya TPLB",
        "board members": "Wajumbe wa Bodi",
        "tplb executive committee": "Kamati ya Utendaji ya TPLB",
        "secretariat team": "Timu ya Sekretarieti",
        "biography": "Wasifu",
        "established to manage professional football league competitions in tanzania.": "Iliundwa kusimamia mashindano ya ligi ya soka ya kitaalamu nchini Tanzania.",

        // news.html & media
        "latest news": "Habari za Hivi Karibuni",
        "videos": "Video",
        "interviews": "Mahojiano",
        "reports": "Taarifa za Mechi",
        "gallery": "Picha",

        // contact.html
        "get in touch": "Wasiliana Nasi",
        "send message": "Tuma Ujumbe",
        "full name": "Majina Kamili",
        "email address": "Barua Pepe",
        "subject": "Mada",
        "message": "Ujumbe",
        "phone number": "Nambari ya Simu",

        // statistics.html
        "top goalscorers": "Wafungaji Bora",
        "top assists": "Pasi Nyingi za Magoli",
        "clean sheets": "Bila Kuruhusu Goli",
        "yellow cards": "Kadi za Njano",
        "red cards": "Kadi Nyekundu",
        "player statistics": "Takwimu za Wachezaji",

        // team-details.html
        "squad": "Kikosi",
        "trophy cabinet": "Kabati la Vikombe",
        "squad value": "Thamani ya Kikosi",
        "recent videos & moments": "Video na Matukio ya Hivi Karibuni",
        "season stats": "Takwimu za Msimu",
        "attacking strength": "Nguvu ya Mashambulizi",
        "clean sheet ratio": "Kiwango cha Kuzuia Magoli",
        "avg. attendance": "Watazamaji Wastani",
        "squad - featured players": "Kikosi - Wachezaji Nyota",

        // player-details.html
        "nationality": "Utaifa",
        "age": "Umri",
        "height": "Urefu",
        "foot": "Mguu",
        "major awards": "Tuzo Kuu",
        "season goals": "Magoli ya Msimu",
        "matches": "Mechi",
        "assists": "Pasi za Magoli",
        "minutes played": "Dakika za Mchezo",
        "performance highlights": "Matukio ya Kipekee",
        "transfer history": "Historia ya Uhamisho",
        "player center": "Kituo cha Wachezaji",
        "official player database": "Hifadhidata Rasmi ya Wachezaji",
        "player squad": "Kikosi cha Wachezaji",
        "current position": "Nafasi ya Sasa",

        // Additional Layout phrases
        "news center": "Kituo cha Habari",
        "interviews center": "Kituo cha Mahojiano",
        "reports center": "Kituo cha Ripoti",
        "videos center": "Kituo cha Video",
        "gallery center": "Kituo cha Nyumba ya Picha",
        "about board center": "Kuhusu Bodi Center",
        "contact center": "Kituo cha Mawasiliano",
        "live scores center": "Kituo cha Matokeo Mubashara",
        "womens league center": "Kituo cha Ligi ya Wanawake",
        "first league center": "Kituo cha Ligi Daraja la Kwanza",
        "championship center": "Kituo cha Championship",
        "crdb cup center": "Kituo cha Kombe la CRDB",
        "caf matches center": "Kituo cha Mechi za CAF",
        "fixtures center": "Kituo cha Ratiba",
        "results center": "Kituo cha Matokeo",
        "standings center": "Kituo cha Msimamo",
        "rules center": "Kituo cha Kanuni",
        "board center": "Kituo cha Bodi",

        "latest results": "Matokeo ya Hivi Karibuni",
        "official fixtures": "Ratiba Rasmi",
        "live results": "Matokeo Mubashara",
        "league standings": "Msimamo wa Ligi",
        "player statistics": "Takwimu za Wachezaji",
        "transfers tracker": "Kifuatilia Uhamisho",
        "about tplb": "Kuhusu TPLB",
        "about tff": "Kuhusu TFF",
        "history of tplb": "Historia ya TPLB",
        "board members": "Wajumbe wa Bodi",
        "secretariat": "Sekretarieti",
        "contact us": "Wasiliana Nasi",
        "official digital portal for the nbc premier league and tanzanian football.": "Tovuti rasmi ya Ligi Kuu ya NBC na soka la Tanzania.",
        "stay connected with every goal, every moment, and every hero.": "Endelea kuunganishwa na kila goli, kila wakati, na kila shujaa.",
        "tanzania football federation": "Shirikisho la Mpira wa Miguu Tanzania",
        "tanzania premier league board": "Bodi ya Ligi Kuu Tanzania",
        "tplb secretariat": "Sekretarieti ya TPLB",
        "tplb executive committee": "Kamati ya Utendaji ya TPLB",
        "board members & delegates": "Wajumbe wa Bodi & Wajumbe",
        "the board": "Bodi",
        "the executive committee": "Kamati ya Utendaji",
        "the secretariat": "Sekretarieti",
        "the history": "Historia",

        "crdb bank federation cup": "Kombe la Shirikisho la Benki ya CRDB",
        "crdb cup": "Kombe la CRDB",
        "crdb federation cup": "Kombe la Shirikisho la CRDB",
        "caf champions league": "Ligi ya Mabingwa wa CAF",
        "caf confederation cup": "Kombe la Shirikisho la CAF",
        "caf competitions": "Mashindano ya CAF",
        "crdb fa cup": "Kombe la FA la CRDB",
        "caf matches": "Mechi za CAF",
        "match day": "Siku ya Mechi",
        "round of 16": "Raundi ya 16",
        "quarter finals": "Robo Fainali",
        "semi finals": "Nusu Fainali",
        "final": "Fainali",
        "stadium": "Uwanja",
        "venue": "Uwanja",
        "kick off": "Muda wa Kuanza",
        "referee": "Mwamuzi",
        "attendance": "Mahudhurio",

        "general rules": "Kanuni za Jumla",
        "disciplinary rules": "Kanuni za Nidhamu",
        "registration rules": "Kanuni za Usajili",
        "match operations": "Uendeshaji wa Mechi",
        "financial regulations": "Kanuni za Fedha",
        "protests & appeals": "Malalamiko na Rufaa",
        "download official pdf": "Pakua PDF Rasmi",
        "view interactive rules": "Angalia Kanuni za Kuingiliana",
        "key regulation": "Kanuni Muhimu",
        "season timeline": "Muda wa Msimu",
        "season start": "Kuanza kwa Msimu",
        "transfer window": "Dirisha la Usajili",
        "mid-season break": "Mapumziko ya Katikati ya Msimu",
        "season end": "Mwisho wa Msimu",
        "all competitions overview": "Muhtasari wa Mashindano Yote",
        "download pdf": "Pakua PDF",
        "read online": "Soma Mtandaoni",
        "close document": "Funga Hati",

        "filter by competition": "Chuja kwa Mashindano",
        "filter by status": "Chuja kwa Hali",
        "all matches": "Mechi Zote",
        "live now": "Mubashara Sasa",
        "finished": "Imemalizika",
        "scheduled": "Imepangwa",
        "possession": "Umiliki wa Mpira",
        "shots on target": "Mashuti Lengo",
        "shots off target": "Mashuti Nje ya Lengo",
        "corners": "Kona",
        "fouls": "Madambi",
        "offsides": "Kuotea",
        "goalkeeper saves": "Okoa za Kipa",
        "match details": "Maelezo ya Mechi",
        "lineups": "Vikosi",
        "stats": "Takwimu",
        "events": "Matukio",

        "active quiz": "Maswali Yanayoendelea",
        "completed quizzes": "Maswali Yaliyokamilika",
        "score": "Alama",
        "correct": "Sahihi",
        "incorrect": "Sio Sahihi",
        "time left": "Muda Uliobaki",
        "submit answers": "Wasilisha Majibu",
        "restart quiz": "Anza Upya Maswali",
        "correct answers": "Majibu Sahihi",
        "your rank": "Nafasi Yako",
        "leaderboard": "Ubao wa Wanaoongoza",

        "search articles": "Tafuta Habari",
        "filter by category": "Chuja kwa Jamii",
        "latest news articles": "Makala ya Habari Mpya",
        "published": "Imechapishwa",
        "author": "Mwandishi",
        "read full article": "Soma Makala Kamili",
        "related articles": "Makala Yanayohusiana",
        "share article": "Shiriki Makala",

        "all photos": "Picha Zote",
        "match action": "Matukio ya Mechi",
        "training sessions": "Mazoezi",
        "behind the scenes": "Nyuma ya Sura",
        "celebrations": "Sherehe",
        "stadium views": "Mitazamo ya Uwanja",
        "view full image": "Angalia Picha Kamili",

        "all teams": "Timu Zote",
        "filter by region": "Chuja kwa Mkoa",
        "club profile": "Wasifu wa Klabu",
        "founded": "Imaraishwa",
        "stadium capacity": "Uwezo wa Uwanja",
        "head coach": "Kocha Mkuu",
        "official website": "Tovuti Rasmi",
        "view team squad": "Angalia Kikosi cha Timu",
        "view stats": "Angalia Takwimu",

        "latest transfers": "Uhamisho wa Hivi Karibuni",
        "transfer window details": "Maelezo ya Dirisha la Uhamisho",
        "buying club": "Klabu Inayonunua",
        "selling club": "Klabu Inayouza",
        "transfer fee": "Ada ya Uhamisho",
        "contract length": "Muda wa Mkataba",
        "confirmed deals": "Mikataba Iliyothibitishwa",
        "rumours tracker": "Kifuatilia Uvumi",
        "official announcement": "Tangazo Rasmi",

        "all videos": "Video Zote",
        "match highlights": "Muhtasari wa Mechi",
        "player interviews": "Mahojiano ya Wachezaji",
        "coach press conferences": "Mikutano ya Waandishi wa Habari wa Kocha",
        "special features": "Makala Maalum",
        "play video": "Cheza Video",

        // Calendar Terms
        "calendar": "Kalenda",
        "all competitions": "Mashindano Yote",
        "filter by club": "Chuja kwa Klabu",
        "matches by competition": "Mechi kwa Mashindano",
        "upcoming highlights": "Vivutio Vijavyo",
        "day": "Siku",
        "week": "Wiki",
        "month": "Mwezi",
        "fixtures for": "Mechi za",
        "legend": "Maelezo",
        "live match": "Mechi ya Moja kwa Moja",
        "match today": "Mechi ya Leo",
        "upcoming match": "Mechi Ijayo",
        "completed match": "Mechi Iliyomalizika",
        "venue": "Uwanja",
        "all clubs": "Klabu Zote",
        "export": "Pakua",
        "view": "Angalia",
        "view details": "Angalia Maelezo",
        "championship league": "Championship League",
        "first league": "First League",
        "women's league": "Ligi ya Wanawake",
        "fa cup": "CRDB FA Cup",
        "caf competitions": "Mashindano ya CAF",
        "international": "Kimataifa",
        "friendly": "Kirafiki"
    };

    function translatePhrase(text) {
        let normalized = text.replace(/\s+/g, ' ').trim();
        if (!normalized) return null;

        // 1. Direct match (exact or case-insensitive)
        if (TRANSLATIONS[normalized]) {
            return TRANSLATIONS[normalized];
        }
        let lower = normalized.toLowerCase();
        if (TRANSLATIONS[lower]) {
            return TRANSLATIONS[lower];
        }

        // 2. Regex / Dynamic patterns
        let matchesMatch = normalized.match(/^(\d+)\s+matches$/i);
        if (matchesMatch) return "Mechi " + matchesMatch[1];

        let goalsMatch = normalized.match(/^(\d+)\s+goals$/i);
        if (goalsMatch) return "Magoli " + goalsMatch[1];

        let assistsMatch = normalized.match(/^(\d+)\s+assists$/i);
        if (assistsMatch) return "Pasi " + assistsMatch[1];

        let cleanSheetsMatch = normalized.match(/^(\d+)\s+clean\s+sheets$/i);
        if (cleanSheetsMatch) return "Kuzuia Magoli " + cleanSheetsMatch[1];

        // 3. Fallbacks for compound strings using separators
        if (normalized.includes('|')) {
            let segments = normalized.split('|');
            let translatedSegments = segments.map(seg => {
                let trimSeg = seg.trim();
                let transSeg = translatePhrase(trimSeg);
                return transSeg ? transSeg : trimSeg;
            });
            return translatedSegments.join(' | ');
        }
        if (normalized.includes('•')) {
            let segments = normalized.split('•');
            let translatedSegments = segments.map(seg => {
                let trimSeg = seg.trim();
                let transSeg = translatePhrase(trimSeg);
                return transSeg ? transSeg : trimSeg;
            });
            return translatedSegments.join(' • ');
        }
        if (normalized.includes('—')) {
            let segments = normalized.split('—');
            let translatedSegments = segments.map(seg => {
                let trimSeg = seg.trim();
                let transSeg = translatePhrase(trimSeg);
                return transSeg ? transSeg : trimSeg;
            });
            return translatedSegments.join(' — ');
        }
        
        return null;
    }

    function applyLanguage(lang) {
        function walk(node) {
            if (node.nodeType === Node.TEXT_NODE) {
                const text = node.nodeValue.trim();
                if (text.length > 0) {
                    if (node.originalText === undefined) {
                        node.originalText = node.nodeValue;
                    }

                    if (lang === 'sw') {
                        const translated = translatePhrase(text);
                        if (translated) {
                            const leading = node.nodeValue.match(/^\s*/)[0];
                            const trailing = node.nodeValue.match(/\s*$/)[0];
                            node.nodeValue = leading + translated + trailing;
                        }
                    } else {
                        node.nodeValue = node.originalText;
                    }
                }
            } else if (node.nodeType === Node.ELEMENT_NODE) {
                const tagName = node.tagName.toLowerCase();
                if (tagName !== 'script' && 
                    tagName !== 'style' && 
                    !node.classList.contains('notranslate') && 
                    node.getAttribute('translate') !== 'no') {
                    
                    if (node.placeholder) {
                        if (node.originalPlaceholder === undefined) {
                            node.originalPlaceholder = node.placeholder;
                        }
                        if (lang === 'sw') {
                            const translated = translatePhrase(node.placeholder.trim());
                            if (translated) {
                                node.placeholder = translated;
                            }
                        } else {
                            node.placeholder = node.originalPlaceholder;
                        }
                    }
                    
                    for (let child of node.childNodes) {
                        walk(child);
                    }
                }
            }
        }

        if (document.body) {
            walk(document.body);
        }
    }

    // Initialize Language Selection
    const savedLang = localStorage.getItem('lang') || 'en';
    const langSelectors = document.querySelectorAll('.lang-selector-mini select, .lang-selector select');

    langSelectors.forEach(select => {
        select.value = savedLang;
        select.addEventListener('change', (e) => {
            const newLang = e.target.value;
            localStorage.setItem('lang', newLang);
            
            // Sync all language selectors
            langSelectors.forEach(s => {
                s.value = newLang;
            });
            
            applyLanguage(newLang);
        });
    });

    // Run translation logic initially
    applyLanguage(savedLang);

    // --- GLOBAL SEARCH ENGINE ---
    const GLOBAL_SEARCH_INDEX = [
        // Players
        { name: "Stephane Aziz Ki", category: "Player", url: "player-details.html?id=aziz-ki", desc: "Yanga SC - Attacking Midfielder" },
        { name: "Feisal Salum", category: "Player", url: "player-details.html?id=feisal-salum", desc: "Azam FC - Midfielder" },
        { name: "Clement Mzize", category: "Player", url: "player-details.html?id=mzize", desc: "Yanga SC - Forward" },
        { name: "Clatous Chama", category: "Player", url: "player-details.html?id=chama", desc: "Simba SC - Midfielder" },
        { name: "Djigui Diarra", category: "Player", url: "player-details.html?id=diarra", desc: "Yanga SC - Goalkeeper" },

        // Coaches
        { name: "Miguel Gamondi", category: "Coach", url: "coach-details.html?id=gamondi", desc: "Yanga SC - Head Coach" },
        { name: "Fadlu Davids", category: "Coach", url: "coach-details.html?id=fadlu", desc: "Simba SC - Head Coach" },
        { name: "Youssouph Dabo", category: "Coach", url: "coach-details.html?id=dabo", desc: "Azam FC - Head Coach" },

        // Clubs
        { name: "Yanga SC (Young Africans)", category: "Club", url: "team-details.html?id=yanga", desc: "Ligi Kuu Champions" },
        { name: "Simba SC", category: "Club", url: "team-details.html?id=simba", desc: "Ligi Kuu Runners-up" },
        { name: "Azam FC", category: "Club", url: "team-details.html?id=azam", desc: "Ligi Kuu 3rd Place" },
        { name: "Singida BS", category: "Club", url: "team-details.html?id=singida", desc: "NBC Premier League Club" },
        { name: "Coastal Union", category: "Club", url: "team-details.html?id=coastal", desc: "NBC Premier League Club" },
        { name: "KMC FC", category: "Club", url: "team-details.html?id=kmc", desc: "NBC Premier League Club" },
        { name: "Tanzania Prisons", category: "Club", url: "team-details.html?id=prisons", desc: "NBC Premier League Club" },
        { name: "Mashujaa FC", category: "Club", url: "team-details.html?id=mashujaa", desc: "NBC Premier League Club" },
        { name: "Namungo FC", category: "Club", url: "team-details.html?id=namungo", desc: "NBC Premier League Club" },
        { name: "Dodoma Jiji FC", category: "Club", url: "team-details.html?id=dodoma", desc: "NBC Premier League Club" },
        { name: "Kagera Sugar", category: "Club", url: "team-details.html?id=kagera", desc: "NBC Premier League Club" },
        { name: "Ihefu FC", category: "Club", url: "team-details.html?id=ihefu", desc: "NBC Premier League Club" },
        { name: "JKT Tanzania", category: "Club", url: "team-details.html?id=jkt", desc: "NBC Premier League Club" },
        { name: "Tabora United", category: "Club", url: "team-details.html?id=tabora", desc: "NBC Premier League Club" },
        { name: "Mtibwa Sugar", category: "Club", url: "team-details.html?id=mtibwa", desc: "NBC Premier League Club" },
        { name: "Geita Gold FC", category: "Club", url: "team-details.html?id=geita", desc: "NBC Premier League Club" },

        // News Articles
        { name: "OKELLO KINARA WA MABAO YA MGUU YA KUSHOTO LIGI KUU YA NBC", category: "News", url: "news-details.html?id=1", desc: "Allan Okello left-footed goals analysis" },
        { name: "GEITA ‘WAKALI’ WA KUTUPIA NBC CHAMPIONSHIP", category: "News", url: "news-details.html?id=2", desc: "Geita Gold scoring prowess in Championship" },
        { name: "CHIRWA HAKAMATIKI NBC CHAMPIONSHIP", category: "News", url: "news-details.html?id=3", desc: "Obrey Chirwa's scoring streak" },
        { name: "‘WALINDA LANGO’ LA AZAM NI MOTO WA KUOTEA MBALI LIGI KUU YA NBC", category: "News", url: "news-details.html?id=4", desc: "Azam FC goalkeepers feature" },
        { name: "YOUNG AFRICANS, AZAM ZATAKATA NYUMBANI LIGI KUU YA NBC", category: "News", url: "news-details.html?id=5", desc: "Home wins for Yanga and Azam" },
        { name: "LIGI KUU YA NBC YAENDELEA KUTIMUA ‘VUMBI’", category: "News", url: "news-details.html?id=6", desc: "NBC Premier League matchday roundup" }
    ];

    const searchBoxes = document.querySelectorAll('.header-search-box, .search-bar-mobile');
    searchBoxes.forEach(box => {
        const input = box.querySelector('input');
        if (!input) return;

        // Ensure box has relative positioning so absolute dropdown works
        box.style.position = 'relative';

        const resultsDropdown = document.createElement('div');
        resultsDropdown.className = 'global-search-results';
        box.appendChild(resultsDropdown);

        function performSearch() {
            const query = input.value.toLowerCase().trim();
            resultsDropdown.innerHTML = '';

            let matches = [];
            if (query.length === 0) {
                matches = GLOBAL_SEARCH_INDEX;
            } else {
                matches = GLOBAL_SEARCH_INDEX.filter(item => 
                    item.name.toLowerCase().includes(query) || 
                    item.desc.toLowerCase().includes(query)
                );
            }

            if (matches.length === 0) {
                resultsDropdown.classList.add('active');
                resultsDropdown.innerHTML = `
                    <div style="padding:15px; text-align:center; font-size:0.8rem; color:var(--text-muted); font-weight:700;">
                        No results found for "${input.value}"
                    </div>
                `;
                return;
            }

            resultsDropdown.classList.add('active');
            matches.forEach(item => {
                const el = document.createElement('a');
                el.href = item.url;
                el.className = 'global-search-item';
                el.innerHTML = `
                    <span class="item-title">${item.name}</span>
                    <div class="item-meta">
                        <span>${item.desc}</span>
                        <span class="item-cat">${item.category}</span>
                    </div>
                `;
                resultsDropdown.appendChild(el);
            });
        }

        input.addEventListener('input', performSearch);
        input.addEventListener('focus', performSearch);
        input.addEventListener('click', performSearch);

        document.addEventListener('click', (e) => {
            if (!box.contains(e.target)) {
                resultsDropdown.classList.remove('active');
            }
        });
    });

});


