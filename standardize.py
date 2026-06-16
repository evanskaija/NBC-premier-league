import os
import re

# Dynamically resolve directory path relative to the script location
workspace_dir = os.path.dirname(os.path.abspath(__file__))

HEADER_TEMPLATE = """    <div class="portal-header-container">
        <!-- TOP TIER: PREMIUM LIGHT BRANDING -->
        <div class="header-top-tier">
            <a href="index.html" class="brand-section">
                <img src="images/Premier league.png" alt="Logo" class="logo-desktop">
                <img src="images/NBC.png" alt="NBC Logo" class="logo-mobile">
                <span class="site-title">Tanzania Football Hub</span>
            </a>

            <div class="header-search-box desktop-only">
                <i class="fa-solid fa-magnifying-glass" style="color:#aaa; margin-right:12px;"></i>
                <input type="text" placeholder="Search for players, matches, or news...">
            </div>

            <div class="utility-section">
                <!-- Language Selector -->
                <div class="lang-selector-mini">
                    <i class="fa-solid fa-globe lang-icon" style="color: var(--primary); margin-right: 5px;"></i>
                    <select style="background: transparent; border: none; color: var(--text-main); font-family: 'Outfit'; font-weight: 800; font-size: 0.8rem; cursor: pointer; outline: none; padding-right: 5px;">
                        <option value="en">EN</option>
                        <option value="sw">SW</option>
                    </select>
                </div>
                
                <!-- Dark Mode Toggle -->
                <div class="nav-utility-btn" id="theme-toggle">
                    <i class="fa-solid fa-moon"></i>
                </div>
                
                <a href="https://fcms.ma.services/tan/login" target="_blank" class="header-login-btn">Member Login</a>
                <div class="mobile-toggle-btn" id="mobile-toggle-btn"><i class="fa-solid fa-bars"></i></div>
            </div>
        </div>

        <!-- BOTTOM TIER: ELITE NAVIGATION -->
        <nav class="header-nav-tier desktop-only">
            <ul class="nav-strip">
                <li><a href="index.html"__ACTIVE_HOME__><i class="fa-solid fa-house"></i> Home</a></li>
                <li class="nav-item-dropdown__ACTIVE_NEWS_PARENT__">
                    <a href="news.html"><i class="fa-solid fa-newspaper"></i> News <i class="fa-solid fa-chevron-down" style="font-size:0.6rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="news.html"__ACTIVE_NEWS_LATEST__>Latest News</a>
                        <a href="transfers.html"__ACTIVE_TRANSFERS_NEWS__>Transfers</a>
                        <a href="interviews.html"__ACTIVE_INTERVIEWS__>Interviews</a>
                        <a href="features.html"__ACTIVE_FEATURES__>Features</a>
                        <a href="reports.html"__ACTIVE_REPORTS__>Reports</a>
                        <a href="videos.html"__ACTIVE_VIDEOS__>Videos</a>
                    </div>
                </li>
                <li class="nav-item-dropdown__ACTIVE_MATCHES_PARENT__">
                    <a href="#"><i class="fa-solid fa-calendar-check"></i> Matches <i class="fa-solid fa-chevron-down" style="font-size:0.6rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="fixtures.html"__ACTIVE_FIXTURES__>Fixtures</a>
                        <a href="results.html"__ACTIVE_RESULTS__>Results</a>
                        <a href="standings.html"__ACTIVE_STANDINGS__>Standings</a>
                        <a href="livescores.html"__ACTIVE_LIVESCORES__>Live Scores</a>
                    </div>
                </li>
                <li><a href="calendar.html"__ACTIVE_CALENDAR__><i class="fa-solid fa-calendar-days"></i> Calendar</a></li>
                <li class="nav-item-dropdown__ACTIVE_HUB_PARENT__">
                    <a href="#"><i class="fa-solid fa-users-viewfinder"></i> Hub <i class="fa-solid fa-chevron-down" style="font-size:0.6rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="teams.html"__ACTIVE_TEAMS__>Teams</a>
                        <a href="players.html"__ACTIVE_PLAYERS__>Players</a>
                        <a href="transfers.html"__ACTIVE_TRANSFERS_HUB__>Transfers</a>
                        <a href="statistics.html"__ACTIVE_STATISTICS__>Statistics</a>
                    </div>
                </li>
                <li class="nav-item-dropdown__ACTIVE_LIGIKUU_PARENT__ mega-parent">
                    <a href="#"><i class="fa-solid fa-trophy"></i> Ligi Kuu <i class="fa-solid fa-chevron-down" style="font-size:0.6rem;"></i></a>
                    <div class="mega-dropdown-menu">
                        <div class="mega-grid">
                            <div class="mega-col">
                                <h5 data-translate-key="competitions">Competitions</h5>
                                <a href="nbcpremierleague.html"__ACTIVE_NBC__>
                                    <img src="images/NBC.png" alt="NBC" class="mega-icon">
                                    <div class="mega-text">
                                        <strong>NBC Premier League</strong>
                                        <span data-translate-key="nbc-desc">Tanzania's top-tier league division</span>
                                    </div>
                                </a>
                                <a href="championship.html"__ACTIVE_CHAMPIONSHIP__>
                                    <img src="images/championship.png" alt="Championship" class="mega-icon">
                                    <div class="mega-text">
                                        <strong>Championship</strong>
                                        <span data-translate-key="champ-desc">Second-tier division promotion battle</span>
                                    </div>
                                </a>
                                <a href="firstleague.html"__ACTIVE_FIRSTLEAGUE__>
                                    <img src="images/Premier league.png" alt="First League" class="mega-icon">
                                    <div class="mega-text">
                                        <strong>First League</strong>
                                        <span data-translate-key="first-desc">Third-tier regional division</span>
                                    </div>
                                </a>
                                <a href="womensleague.html"__ACTIVE_WOMENSLEAGUE__>
                                    <img src="images/NBC.png" alt="Women's League" class="mega-icon">
                                    <div class="mega-text">
                                        <strong>Women's League</strong>
                                        <span data-translate-key="womens-desc">Top female football competition</span>
                                    </div>
                                </a>
                            </div>
                            <div class="mega-col">
                                <h5 data-translate-key="cups-rules">Cup & Regulations</h5>
                                <a href="facup.html">
                                    <img src="images/crdb cup.jpg" alt="FA Cup" class="mega-icon">
                                    <div class="mega-text">
                                        <strong>CRDB FA Cup</strong>
                                        <span data-translate-key="fa-desc">Knockout tournament for all clubs</span>
                                    </div>
                                </a>
                                <a href="kanuni.html">
                                    <i class="fa-solid fa-scale-balanced mega-font-icon"></i>
                                    <div class="mega-text">
                                        <strong>League Rules & Kanuni</strong>
                                        <span data-translate-key="rules-desc">Official rules, laws, and regulations</span>
                                    </div>
                                </a>
                            </div>
                            <div class="mega-col mega-featured">
                                <div class="mega-featured-card">
                                    <img src="images/tuzo1.JPG" alt="Featured">
                                    <div class="featured-overlay"></div>
                                    <div class="featured-info">
                                        <span class="feat-badge" data-translate-key="featured">Featured</span>
                                        <h6 data-translate-key="spotlight-title">NBC Premier League Derby</h6>
                                        <p data-translate-key="spotlight-desc">Relive the excitement of the Dar es Salaam Derby.</p>
                                        <a href="nbcpremierleague.html" class="btn btn-primary btn-xs" data-translate-key="view-table">View Standings</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="nav-item-dropdown__ACTIVE_BOARD_PARENT__ mega-parent">
                    <a href="#"><i class="fa-solid fa-landmark"></i> Board <i class="fa-solid fa-chevron-down" style="font-size:0.6rem;"></i></a>
                    <div class="mega-dropdown-menu">
                        <div class="mega-grid">
                            <div class="mega-col">
                                <h5 data-translate-key="about-board">About Board</h5>
                                <a href="about.html"__ACTIVE_ABOUTBOARD__>
                                    <i class="fa-solid fa-circle-info mega-font-icon"></i>
                                    <div class="mega-text">
                                        <strong>About TPLB</strong>
                                        <span data-translate-key="tplb-desc">Overview of the Premier League Board</span>
                                    </div>
                                </a>
                                <a href="about.html#history"__ACTIVE_HISTORY__>
                                    <i class="fa-solid fa-clock-rotate-left mega-font-icon"></i>
                                    <div class="mega-text">
                                        <strong>TPLB History</strong>
                                        <span data-translate-key="history-desc">Key historical timelines and milestones</span>
                                    </div>
                                </a>
                            </div>
                            <div class="mega-col">
                                <h5 data-translate-key="organization">Organization</h5>
                                <a href="about.html#board"__ACTIVE_MEMBERS__>
                                    <i class="fa-solid fa-users mega-font-icon"></i>
                                    <div class="mega-text">
                                        <strong>Board Members</strong>
                                        <span data-translate-key="members-desc">Meet the executive leadership team</span>
                                    </div>
                                </a>
                                <a href="about.html#secretariat"__ACTIVE_SECRETARIAT__>
                                    <i class="fa-solid fa-sitemap mega-font-icon"></i>
                                    <div class="mega-text">
                                        <strong>Secretariat Hub</strong>
                                        <span data-translate-key="secretariat-desc">Operational departments and staff</span>
                                    </div>
                                </a>
                            </div>
                            <div class="mega-col mega-featured">
                                <div class="mega-featured-card">
                                    <img src="images/mkapa.jpg" alt="Featured">
                                    <div class="featured-overlay"></div>
                                    <div class="featured-info">
                                        <span class="feat-badge" data-translate-key="contact">Contact</span>
                                        <h6 data-translate-key="have-questions">Have questions?</h6>
                                        <p data-translate-key="contact-desc">Reach out to the TPLB secretariat office.</p>
                                        <a href="contact.html" class="btn btn-primary btn-xs" data-translate-key="get-in-touch">Get in Touch</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>
                <li><a href="contact.html"__ACTIVE_CONTACT__><i class="fa-solid fa-headset"></i> Contact</a></li>
            </ul>
        </nav>
    </div>"""

FOOTER_TEMPLATE = """    <footer class="site-footer reveal-element">
        <div class="footer-bg-overlay"></div>

        <div class="container">
            <div class="footer-main-grid">
                <!-- Column 1: Brand -->
                <div class="f-col branding">
                    <div class="f-logo">
                        <img src="images/Premier league.png" alt="Logo">
                        <span>Tanzania Football Hub</span>
                    </div>
                    <p class="f-desc" data-translate-key="footer-desc">The official digital portal for the NBC Premier League and Tanzanian football.</p>
                    <div class="f-contact-details" style="margin-top: 15px; font-size: 0.8rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 8px;">
                        <span><i class="fa-solid fa-envelope" style="color: var(--primary); margin-right: 8px;"></i> info@tanzaniafootballhub.com</span>
                        <span><i class="fa-solid fa-phone" style="color: var(--primary); margin-right: 8px;"></i> +255 22 212 3456</span>
                    </div>
                    <div class="f-social-v2" style="margin-top: 15px;">
                        <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                        <a href="#"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#"><i class="fa-brands fa-youtube"></i></a>
                        <a href="#"><i class="fa-brands fa-tiktok"></i></a>
                    </div>
                </div>

                <!-- Column 2: Competitions -->
                <div class="f-col">
                    <h4 data-translate-key="competitions">Competitions</h4>
                    <ul class="f-nav-links">
                        <li><a href="nbcpremierleague.html">NBC Premier League</a></li>
                        <li><a href="championship.html">Championship</a></li>
                        <li><a href="firstleague.html">First League</a></li>
                        <li><a href="womensleague.html">Women's League</a></li>
                        <li><a href="facup.html">FA Cup</a></li>
                    </ul>
                </div>

                <!-- Column 3: The Hub -->
                <div class="f-col">
                    <h4 data-translate-key="quick-links">Quick Links</h4>
                    <ul class="f-nav-links">
                        <li><a href="news.html" data-translate-key="news">News</a></li>
                        <li><a href="fixtures.html" data-translate-key="fixtures">Fixtures</a></li>
                        <li><a href="standings.html" data-translate-key="standings">Standings</a></li>
                        <li><a href="statistics.html" data-translate-key="statistics">Statistics</a></li>
                        <li><a href="transfers.html" data-translate-key="transfers">Transfers</a></li>
                    </ul>
                </div>

                <!-- Column 4: Newsletter Signup -->
                <div class="f-col">
                    <h4 data-translate-key="newsletter-title">Stay Updated</h4>
                    <p style="font-size:0.8rem; color: var(--text-muted); margin-bottom: 15px; line-height: 1.5;" data-translate-key="newsletter-desc">Subscribe to get latest scores, fixtures, and news alerts.</p>
                    <div class="input-group-premium">
                        <input type="email" placeholder="Enter your email..." style="padding: 8px 12px; font-size: 0.8rem;">
                        <button class="btn btn-primary btn-sm" style="border-radius: 8px;" data-translate-key="subscribe">Subscribe</button>
                    </div>
                </div>
            </div>

            <!-- Bottom Legal Bar -->
            <div class="footer-bottom">
                <div class="copy" data-translate-key="copyright">
                    &copy; 2026 Tanzania Football Federation (TFF). All rights reserved.
                </div>
                <div class="legal-links">
                    <a href="#" data-translate-key="privacy">Privacy Policy</a>
                    <a href="#" data-translate-key="terms">Terms of Use</a>
                    <a href="#" data-translate-key="accessibility">Accessibility</a>
                </div>
            </div>
        </div>
    </footer>"""

MOBILE_MENU_TEMPLATE = """    <!-- Professional Sliding Mobile Menu -->
    <nav class="full-screen-menu" id="full-menu">
        <div class="menu-drawer">
            <div class="menu-close-area" id="close-menu-btn"><i class="fa-solid fa-xmark"></i></div>

            <div class="menu-header">
                <img src="images/Premier league.png" alt="Hub Logo">
                <h2>MENU</h2>
            </div>

            <!-- Vertical Navigation list -->
            <div class="mobile-menu-grid">
                <a href="index.html"__MOBILE_ACTIVE_HOME__><i class="fa-solid fa-house"></i><span>Home</span></a>
                <a href="news.html"__MOBILE_ACTIVE_NEWS__><i class="fa-solid fa-newspaper"></i><span>News</span></a>
                <a href="fixtures.html"__MOBILE_ACTIVE_MATCHES__><i class="fa-solid fa-calendar-check"></i><span>Matches</span></a>
                
                <a href="calendar.html"__MOBILE_ACTIVE_CALENDAR__><i class="fa-solid fa-calendar-days"></i><span>Calendar</span></a>
                <a href="teams.html"__MOBILE_ACTIVE_HUB__><i class="fa-solid fa-users-viewfinder"></i><span>Hub</span></a>
                
                <a href="#" class="menu-grid-item mobile-dropdown-btn" data-target="mobile-ligikuu-dropdown"><i class="fa-solid fa-trophy"></i><span>Ligi Kuu <i class="fa-solid fa-chevron-down" style="font-size:0.6rem; margin-left: 2px;"></i></span></a>
                
                <!-- Collapsible Dropdown for Ligi Kuu -->
                <div class="mobile-dropdown-content" id="mobile-ligikuu-dropdown" style="display: none;">
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px;">
                        <li><a href="nbcpremierleague.html" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><img src="images/NBC.png" alt="NBC" style="height: 18px; width: auto;"> NBC Premier League</a></li>
                        <li><a href="championship.html" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><img src="images/championship.png" alt="Championship" style="height: 18px; width: auto;"> Championship</a></li>
                        <li><a href="firstleague.html" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><img src="images/Premier league.png" alt="First League" style="height: 18px; width: auto;"> First League</a></li>
                        <li><a href="womensleague.html" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><img src="images/NBC.png" alt="Women" style="height: 18px; width: auto;"> Women's League</a></li>
                        <li><a href="kanuni.html" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-scale-balanced" style="color: var(--primary); font-size: 0.95rem; width: 18px; text-align: center;"></i> League Rules & Kanuni</a></li>
                    </ul>
                </div>

                <a href="#" class="menu-grid-item mobile-dropdown-btn" data-target="mobile-board-dropdown"><i class="fa-solid fa-circle-info"></i><span>Board <i class="fa-solid fa-chevron-down" style="font-size:0.6rem; margin-left: 2px;"></i></span></a>
                
                <!-- Collapsible Dropdown for Board -->
                <div class="mobile-dropdown-content" id="mobile-board-dropdown" style="display: none;">
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px;">
                        <li><a href="about.html" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-circle-info" style="color: var(--primary); font-size: 0.95rem; width: 18px; text-align: center;"></i> About TPLB</a></li>
                        <li><a href="about.html#history" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-clock-rotate-left" style="color: var(--primary); font-size: 0.95rem; width: 18px; text-align: center;"></i> History</a></li>
                        <li><a href="about.html#members" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-users" style="color: var(--primary); font-size: 0.95rem; width: 18px; text-align: center;"></i> Members</a></li>
                        <li><a href="about.html#secretariat" style="text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-user-tie" style="color: var(--primary); font-size: 0.95rem; width: 18px; text-align: center;"></i> Secretariat</a></li>
                    </ul>
                </div>

                <a href="contact.html"__MOBILE_ACTIVE_CONTACT__><i class="fa-solid fa-envelope"></i><span>Contact</span></a>
            </div>

            <!-- Theme Toggle and Language Selector (Inside drawer for clean header) -->
            <div class="menu-utilities" style="margin-top: 15px; display: flex; flex-direction: column; gap: 12px; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 15px;">
                <!-- Theme Mode Selector (Dark/Light) -->
                <div class="menu-grid-item" id="theme-toggle-mobile" style="cursor: pointer; background: transparent; border: none; padding-left: 12px; display: flex; align-items: center; gap: 12px;">
                    <i class="fa-solid fa-moon" style="color: var(--primary); font-size: 1.15rem; width: 20px; text-align: center;"></i>
                    <span style="font-size: 1.05rem; font-weight: 800; text-transform: uppercase;">Dark Mode</span>
                </div>

                <!-- Language Selector Dropdown -->
                <div class="menu-grid-item lang-selector-mini" style="background: transparent; border: none; padding-left: 12px; display: flex; align-items: center; gap: 12px;">
                    <i class="fa-solid fa-globe lang-icon" style="color: var(--primary); font-size: 1.15rem; width: 20px; text-align: center;"></i>
                    <select style="background: transparent; border: none; color: #ffffff; font-family: 'Outfit'; font-weight: 800; font-size: 1.05rem; cursor: pointer; outline: none; text-transform: uppercase; padding: 0;">
                        <option value="en" style="background: #000814; color: #ffffff;">English</option>
                        <option value="sw" style="background: #000814; color: #ffffff;">Swahili</option>
                    </select>
                </div>
            </div>

            <!-- Login Primary Action Button (Matches booking button layout in image) -->
            <div class="menu-action-box" style="margin-top: auto; padding-top: 20px;">
                <a href="https://fcms.ma.services/tan/login" target="_blank" class="menu-action-btn">Member Login</a>
            </div>
        </div>
    </nav>"""

BOTTOM_NAV_TEMPLATE = """    <!-- Mobile Only: Bottom Navigation Bar -->
    <div class="mobile-bottom-nav">
        <a href="index.html"__BOTTOM_ACTIVE_HOME__><i class="fa-solid fa-house"></i><span>Home</span></a>
        <a href="fixtures.html"__BOTTOM_ACTIVE_MATCHES__><i class="fa-solid fa-calendar-check"></i><span>Matches</span></a>
        <a href="standings.html"__BOTTOM_ACTIVE_TABLE__><i class="fa-solid fa-table-list"></i><span>Table</span></a>
        <a href="news.html"__BOTTOM_ACTIVE_NEWS__><i class="fa-solid fa-newspaper"></i><span>News</span></a>
        <a href="https://fcms.ma.services/tan/login" target="_blank"__BOTTOM_ACTIVE_PROFILE__><i class="fa-solid fa-user"></i><span>Profile</span></a>
    </div>"""


active_news = ["news.html", "transfers.html", "interviews.html", "features.html", "reports.html", "videos.html"]
active_matches = ["fixtures.html", "results.html", "standings.html", "livescores.html", "match-details.html"]
active_hub = ["teams.html", "players.html", "transfers.html", "statistics.html", "coach-details.html", "player-details.html", "team-details.html"]
active_ligikuu = ["nbcpremierleague.html", "championship.html", "firstleague.html", "womensleague.html"]
active_board = ["about.html"]
active_contact = ["contact.html"]
active_home = ["index.html"]

def get_active_header(filename):
    hdr = HEADER_TEMPLATE
    
    # helper to replace active states
    def rep(placeholder, value):
        nonlocal hdr
        hdr = hdr.replace(placeholder, value)
        
    rep("__ACTIVE_HOME__", ' class="active"' if filename in active_home else '')
    rep("__ACTIVE_NEWS_PARENT__", ' active' if filename in active_news else '')
    rep("__ACTIVE_NEWS_LATEST__", ' class="active"' if filename == "news.html" else '')
    rep("__ACTIVE_TRANSFERS_NEWS__", ' class="active"' if filename == "transfers.html" else '')
    rep("__ACTIVE_INTERVIEWS__", ' class="active"' if filename == "interviews.html" else '')
    rep("__ACTIVE_FEATURES__", ' class="active"' if filename == "features.html" else '')
    rep("__ACTIVE_REPORTS__", ' class="active"' if filename == "reports.html" else '')
    rep("__ACTIVE_VIDEOS__", ' class="active"' if filename == "videos.html" else '')
    
    rep("__ACTIVE_MATCHES_PARENT__", ' active' if filename in active_matches else '')
    rep("__ACTIVE_FIXTURES__", ' class="active"' if filename == "fixtures.html" else '')
    rep("__ACTIVE_CALENDAR__", ' class="active"' if filename == "calendar.html" else '')
    rep("__ACTIVE_RESULTS__", ' class="active"' if filename == "results.html" else '')
    rep("__ACTIVE_STANDINGS__", ' class="active"' if filename == "standings.html" else '')
    rep("__ACTIVE_LIVESCORES__", ' class="active"' if filename == "livescores.html" else '')
    
    rep("__ACTIVE_HUB_PARENT__", ' active' if filename in active_hub else '')
    rep("__ACTIVE_TEAMS__", ' class="active"' if filename in ["teams.html", "team-details.html", "coach-details.html"] else '')
    rep("__ACTIVE_PLAYERS__", ' class="active"' if filename in ["players.html", "player-details.html"] else '')
    rep("__ACTIVE_TRANSFERS_HUB__", ' class="active"' if filename == "transfers.html" else '')
    rep("__ACTIVE_STATISTICS__", ' class="active"' if filename == "statistics.html" else '')
    
    rep("__ACTIVE_LIGIKUU_PARENT__", ' active' if filename in active_ligikuu else '')
    rep("__ACTIVE_NBC__", ' class="active"' if filename == "nbcpremierleague.html" else '')
    rep("__ACTIVE_CHAMPIONSHIP__", ' class="active"' if filename == "championship.html" else '')
    rep("__ACTIVE_FIRSTLEAGUE__", ' class="active"' if filename == "firstleague.html" else '')
    rep("__ACTIVE_WOMENSLEAGUE__", ' class="active"' if filename == "womensleague.html" else '')
    
    rep("__ACTIVE_BOARD_PARENT__", ' active' if filename in active_board else '')
    rep("__ACTIVE_ABOUTBOARD__", ' class="active"' if filename == "about.html" else '')
    rep("__ACTIVE_HISTORY__", '')
    rep("__ACTIVE_MEMBERS__", '')
    rep("__ACTIVE_SECRETARIAT__", '')
    rep("__ACTIVE_CONTACT__", ' class="active"' if filename in active_contact else '')
    
    return hdr

def get_active_mobile(filename):
    mob = MOBILE_MENU_TEMPLATE
    
    def rep(placeholder, value):
        nonlocal mob
        mob = mob.replace(placeholder, value)
        
    rep("__MOBILE_ACTIVE_HOME__", ' class="menu-grid-item active"' if filename in active_home else ' class="menu-grid-item"')
    rep("__MOBILE_ACTIVE_NEWS__", ' class="menu-grid-item active"' if filename in active_news else ' class="menu-grid-item"')
    rep("__MOBILE_ACTIVE_MATCHES__", ' class="menu-grid-item active"' if filename in active_matches else ' class="menu-grid-item"')
    rep("__MOBILE_ACTIVE_CALENDAR__", ' class="menu-grid-item active"' if filename == "calendar.html" else ' class="menu-grid-item"')
    rep("__MOBILE_ACTIVE_HUB__", ' class="menu-grid-item active"' if filename in active_hub else ' class="menu-grid-item"')
    rep("__MOBILE_ACTIVE_LIGIKUU__", ' class="menu-grid-item active"' if filename in active_ligikuu else ' class="menu-grid-item"')
    rep("__MOBILE_ACTIVE_BOARD__", ' class="menu-grid-item active"' if filename in active_board else ' class="menu-grid-item"')
    rep("__MOBILE_ACTIVE_CONTACT__", ' class="menu-grid-item active"' if filename in active_contact else ' class="menu-grid-item"')
    rep("__MOBILE_ACTIVE_LOGIN__", ' class="menu-grid-item"')
    
    return mob

def get_bottom_nav(filename):
    nav = BOTTOM_NAV_TEMPLATE
    nav = nav.replace("__BOTTOM_ACTIVE_HOME__", ' class="bottom-nav-item active"' if filename in active_home else ' class="bottom-nav-item"')
    nav = nav.replace("__BOTTOM_ACTIVE_MATCHES__", ' class="bottom-nav-item active"' if filename in active_matches or filename == "calendar.html" else ' class="bottom-nav-item"')
    nav = nav.replace("__BOTTOM_ACTIVE_TABLE__", ' class="bottom-nav-item active"' if filename == "standings.html" else ' class="bottom-nav-item"')
    nav = nav.replace("__BOTTOM_ACTIVE_NEWS__", ' class="bottom-nav-item active"' if filename in active_news else ' class="bottom-nav-item"')
    nav = nav.replace("__BOTTOM_ACTIVE_PROFILE__", ' class="bottom-nav-item"')
    return nav

def remove_old_bottom_nav(content):
    p_start, p_end = find_nested_div(content, '<div class="mobile-bottom-nav">')
    if p_start != -1:
        return content[:p_start], content[p_end:]
    return None, None

def find_nested_div(content, start_tag):
    start_idx = content.find(start_tag)
    if start_idx == -1:
        return -1, -1
    
    nesting_level = 0
    idx = start_idx
    while idx < len(content):
        if content[idx:].lower().startswith("<div"):
            # check if it is followed by a space or ">"
            if idx + 4 < len(content) and content[idx+4] in (" ", ">"):
                nesting_level += 1
                idx += 4
                continue
        elif content[idx:].lower().startswith("</div>"):
            nesting_level -= 1
            if nesting_level == 0:
                return start_idx, idx + 6
            idx += 6
            continue
        idx += 1
    return -1, -1

def remove_old_header(content):
    # Try finding portal-header-container
    p_start, p_end = find_nested_div(content, '<div class="portal-header-container">')
    if p_start != -1:
        return content[:p_start], content[p_end:]
    
    # Try finding top-header-wrapper + main-nav
    # We find top-header-wrapper
    t_start, t_end = find_nested_div(content, '<div class="top-header-wrapper">')
    if t_start != -1:
        # Check if there's main-nav next or within 1000 characters
        # And look for the end of main-nav
        nav_match = re.search(r'<nav class="main-nav[^"]*">', content[t_end:t_end+2000])
        if nav_match:
            nav_start = t_end + nav_match.start()
            # find closing </nav> for this main-nav
            nav_end = content.find("</nav>", nav_start)
            if nav_end != -1:
                return content[:t_start], content[nav_end+6:]
        # If no main-nav found, just remove top-header-wrapper
        return content[:t_start], content[t_end:]
    
    # If neither found, see if we can find top-header-wrapper manually
    return None, None

def remove_old_footer(content):
    # Find footer
    # Footer could open with <footer ...> and end with </footer>
    footer_match = re.search(r'<footer[^>]*>', content, re.IGNORECASE)
    if footer_match:
        f_start = footer_match.start()
        # Find closing </footer>
        f_end = content.lower().find("</footer>", f_start)
        if f_end != -1:
            return content[:f_start], content[f_end+9:]
    return None, None

def remove_old_mobile_menu(content):
    # Find full-screen-menu
    m_start = content.find('<nav class="full-screen-menu"')
    if m_start == -1:
        m_start = content.find('<nav class="full-screen-menu')
        
    if m_start != -1:
        # find closing </nav>
        # since mobile menu is nested nav or div, let's track nesting
        nesting = 0
        idx = m_start
        while idx < len(content):
            if content[idx:].lower().startswith("<nav"):
                if idx + 4 < len(content) and content[idx+4] in (" ", ">"):
                    nesting += 1
                    idx += 4
                    continue
            elif content[idx:].lower().startswith("</nav>"):
                nesting -= 1
                if nesting == 0:
                    return content[:m_start], content[idx+6:]
                idx += 6
                continue
            idx += 1
    return None, None

files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

# Include index.html in standardisation loop to apply responsive menu
for filename in files:
    
    filepath = os.path.join(workspace_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    print(f"Standardizing {filename}...")
    
    # 1. Remove old header
    clean_prefix, clean_suffix = remove_old_header(content)
    if clean_prefix is not None:
        content = clean_prefix + "\n" + get_active_header(filename) + "\n" + clean_suffix
    else:
        # No header found! Insert it right after <body> tag
        body_idx = content.lower().find("<body>")
        if body_idx != -1:
            content = content[:body_idx+6] + "\n" + get_active_header(filename) + "\n" + content[body_idx+6:]
            
    # 2. Remove old footer (if any) and insert standard footer
    clean_prefix, clean_suffix = remove_old_footer(content)
    if clean_prefix is not None:
        content = clean_prefix + "\n" + FOOTER_TEMPLATE + "\n" + clean_suffix
    else:
        # No footer found, let's insert it before script.js or before mobile menu or before </body>
        # In this case we'll handle it during mobile menu insert
        pass
        
    # 3. Remove old mobile menu (if any)
    clean_prefix, clean_suffix = remove_old_mobile_menu(content)
    if clean_prefix is not None:
        content = clean_prefix + "\n" + get_active_mobile(filename) + "\n" + clean_suffix
        
    # 4. Remove old bottom nav (if any)
    clean_prefix, clean_suffix = remove_old_bottom_nav(content)
    if clean_prefix is not None:
        content = clean_prefix + "\n" + clean_suffix
        
    # Ensure standard mobile menu is placed correctly before script.js, and that script.js is imported
    # Let's remove script.js import if we find it, and place it at the very bottom
    script_pattern = r'<script src=["\']script\.js["\']></script>'
    content = re.sub(script_pattern, "", content)
    
    # Remove any duplicate script.js imports
    content = re.sub(r'<script src=["\']script\.js["\']>\s*</script>', "", content)
    
    # Determine what to insert before </body>
    body_close = content.lower().find("</body>")
    if body_close != -1:
        menu_insert = ""
        if "full-screen-menu" not in content:
            menu_insert = get_active_mobile(filename) + "\n"
            
        ftr_insert = ""
        if "site-footer" not in content:
            ftr_insert = FOOTER_TEMPLATE + "\n"
            
        # Append footer, mobile menu, bottom nav, and script.js
        content = content[:body_close] + "\n" + ftr_insert + menu_insert + get_bottom_nav(filename) + "\n<script src=\"script.js\"></script>\n" + content[body_close:]

    # Write the modified content back
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("All files standardized!")
