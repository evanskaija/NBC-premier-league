import os
import re

workspace_dir = r"c:\Users\EVANS\OneDrive\Desktop\my projects\Nbc pl"

HEADER_TEMPLATE = """    <div class="portal-header-container">
        <!-- TOP TIER: PREMIUM LIGHT BRANDING -->
        <div class="header-top-tier">
            <a href="index.html" class="brand-section">
                <img src="images/Premier league.png" alt="Logo">
                <span class="site-title">Tanzania Football Hub</span>
            </a>

            <div class="header-search-box desktop-only">
                <i class="fa-solid fa-magnifying-glass" style="color:#aaa; margin-right:12px;"></i>
                <input type="text" placeholder="Search for players, matches, or news...">
            </div>

            <div class="utility-section">
                <!-- Language Selector -->
                <div class="lang-selector-mini">
                    <select>
                        <option value="en">English</option>
                        <option value="sw">Kiswahili</option>
                    </select>
                </div>
                
                <!-- Dark Mode Toggle -->
                <div class="nav-utility-btn" id="theme-toggle">
                    <i class="fa-solid fa-moon"></i>
                </div>
                
                <a href="https://fcms.ma.services/tan/login" target="_blank" class="header-login-btn">Member Login</a>
                <div class="mobile-toggle-btn" id="mobile-toggle-btn">☰</div>
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
                <li class="nav-item-dropdown__ACTIVE_HUB_PARENT__">
                    <a href="#"><i class="fa-solid fa-users-viewfinder"></i> Hub <i class="fa-solid fa-chevron-down" style="font-size:0.6rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="teams.html"__ACTIVE_TEAMS__>Teams</a>
                        <a href="players.html"__ACTIVE_PLAYERS__>Players</a>
                        <a href="transfers.html"__ACTIVE_TRANSFERS_HUB__>Transfers</a>
                        <a href="statistics.html"__ACTIVE_STATISTICS__>Statistics</a>
                    </div>
                </li>
                <li class="nav-item-dropdown__ACTIVE_LIGIKUU_PARENT__">
                    <a href="#"><i class="fa-solid fa-trophy"></i> Ligi Kuu <i class="fa-solid fa-chevron-down" style="font-size:0.6rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="https://www.ligikuu.co.tz/wp-content/uploads/2025/09/KANUNI-TPL-2025.pdf?_gl=1*l9q035*_ga*MTQ4NDgwMDc0Ny4xNzc5Njk0NDgw*_ga_LERPJ5HFT3*czE3ODA3NTQzMDMkbzIzJGcxJHQxNzgwNzU0MzEwJGo1MyRsMCRoMA.." target="_blank"__ACTIVE_NBC__>NBC Premier League</a>
                        <a href="https://www.ligikuu.co.tz/wp-content/uploads/2026/01/KANUNI-CHAMPIONSHIP-20252026.pdf?_gl=1*ifs1gm*_ga*MTQ4NDgwMDc0Ny4xNzc5Njk0NDgw*_ga_LERPJ5HFT3*czE3ODA3NTQzMDMkbzIzJGcxJHQxNzgwNzU0NTE3JGo2MCRsMCRoMA.." target="_blank"__ACTIVE_CHAMPIONSHIP__>Championship</a>
                        <a href="https://www.ligikuu.co.tz/wp-content/uploads/2026/01/KANUNI-FIRST-LEAGUE-20252026-1.pdf?_gl=1*4d6yjz*_ga*MTQ4NDgwMDc0Ny4xNzc5Njk0NDgw*_ga_LERPJ5HFT3*czE3ODA3NTQzMDMkbzIzJGcxJHQxNzgwNzU0NTkxJGo2MCRsMCRoMA.." target="_blank"__ACTIVE_FIRSTLEAGUE__>First League</a>
                        <a href="womensleague.html"__ACTIVE_WOMENSLEAGUE__>Women's League</a>
                    </div>
                </li>
                <li class="nav-item-dropdown__ACTIVE_BOARD_PARENT__">
                    <a href="#"><i class="fa-solid fa-landmark"></i> Board <i class="fa-solid fa-chevron-down" style="font-size:0.6rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="about.html"__ACTIVE_ABOUTBOARD__>About Board</a>
                        <a href="about.html#history"__ACTIVE_HISTORY__>History</a>
                        <a href="about.html#board"__ACTIVE_MEMBERS__>Members</a>
                        <a href="about.html#secretariat"__ACTIVE_SECRETARIAT__>Secretariat</a>
                    </div>
                </li>
                <li><a href="contact.html"__ACTIVE_CONTACT__><i class="fa-solid fa-headset"></i> Contact</a></li>
            </ul>
        </nav>
    </div>"""

FOOTER_TEMPLATE = """    <footer class="site-footer reveal-element">
        <!-- Partner / Sponsor Bar -->
        <div class="footer-partners">
            <div class="container">
                <div class="partners-grid-v2">
                    <div class="partner-logo"><img src="images/nbc.png" alt="NBC"></div>
                    <div class="partner-logo"><img src="images/Premier league.png" alt="TFF"></div>
                    <div class="partner-logo"><img src="images/crdb cup.jpg" alt="CRDB"></div>
                    <div class="partner-logo"><img src="images/championship.png" alt="Puma"></div>
                    <div class="partner-logo"><img src="images/confidaration.png" alt="CAF"></div>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="footer-main-grid">
                <!-- Column 1: Brand -->
                <div class="f-col branding">
                    <div class="f-logo">
                        <img src="images/Premier league.png" alt="Logo">
                        <span>Tanzania Football Hub</span>
                    </div>
                    <p class="f-desc">The official digital portal for the NBC Premier League and Tanzanian football.
                        Stay connected with every goal, every moment, and every hero.</p>
                    <div class="f-social-v2">
                        <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                        <a href="#"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#"><i class="fa-brands fa-youtube"></i></a>
                        <a href="#"><i class="fa-brands fa-tiktok"></i></a>
                    </div>
                </div>

                <!-- Column 2: Competitions -->
                <div class="f-col">
                    <h4>Competitions</h4>
                    <ul class="f-nav-links">
                        <li><a href="https://www.ligikuu.co.tz/wp-content/uploads/2025/09/KANUNI-TPL-2025.pdf?_gl=1*l9q035*_ga*MTQ4NDgwMDc0Ny4xNzc5Njk0NDgw*_ga_LERPJ5HFT3*czE3ODA3NTQzMDMkbzIzJGcxJHQxNzgwNzU0MzEwJGo1MyRsMCRoMA.." target="_blank">NBC Premier League</a></li>
                        <li><a href="https://www.ligikuu.co.tz/wp-content/uploads/2026/01/KANUNI-CHAMPIONSHIP-20252026.pdf?_gl=1*ifs1gm*_ga*MTQ4NDgwMDc0Ny4xNzc5Njk0NDgw*_ga_LERPJ5HFT3*czE3ODA3NTQzMDMkbzIzJGcxJHQxNzgwNzU0NTE3JGo2MCRsMCRoMA.." target="_blank">Championship</a></li>
                        <li><a href="https://www.ligikuu.co.tz/wp-content/uploads/2026/01/KANUNI-FIRST-LEAGUE-20252026-1.pdf?_gl=1*4d6yjz*_ga*MTQ4NDgwMDc0Ny4xNzc5Njk0NDgw*_ga_LERPJ5HFT3*czE3ODA3NTQzMDMkbzIzJGcxJHQxNzgwNzU0NTkxJGo2MCRsMCRoMA.." target="_blank">First League</a></li>
                        <li><a href="womensleague.html">Women's League</a></li>
                        <li><a href="facup.html">FA Cup</a></li>
                        <li><a href="cafmatches.html">CAF Matches</a></li>
                    </ul>
                </div>

                <!-- Column 3: Resources -->
                <div class="f-col">
                    <h4>Resources</h4>
                    <ul class="f-nav-links">
                        <li><a href="fixtures.html">Official Fixtures</a></li>
                        <li><a href="results.html">Live Results</a></li>
                        <li><a href="standings.html">League Standings</a></li>
                        <li><a href="livescores.html">Live Scores</a></li>
                        <li><a href="statistics.html">Player Statistics</a></li>
                        <li><a href="transfers.html">Transfers Tracker</a></li>
                    </ul>
                </div>

                <!-- Column 4: The Hub -->
                <div class="f-col">
                    <h4>The Hub</h4>
                    <ul class="f-nav-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="news.html">Latest News</a></li>
                        <li><a href="interviews.html">Interviews</a></li>
                        <li><a href="features.html">Features</a></li>
                        <li><a href="reports.html">Reports</a></li>
                        <li><a href="videos.html">Videos</a></li>
                        <li><a href="about.html">About TPLB</a></li>
                        <li><a href="about.html#history">History of TPLB</a></li>
                        <li><a href="about.html#board">Board Members</a></li>
                        <li><a href="about.html#secretariat">Secretariat</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
            </div>

            <!-- Bottom Legal Bar -->
            <div class="footer-bottom">
                <div class="copy">
                    &copy; 2026 Tanzania Football Federation (TFF). All rights reserved.
                </div>
                <div class="legal-links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Use</a>
                    <a href="#">Accessibility</a>
                </div>
            </div>
        </div>
    </footer>"""

MOBILE_MENU_TEMPLATE = """    <!-- Professional Sliding Mobile Menu -->
    <nav class="full-screen-menu" id="full-menu">
        <div class="menu-drawer">
            <div class="menu-close-area" id="close-menu-btn">✕</div>

            <div class="menu-header">
                <img src="images/Premier league.png" alt="Hub Logo">
                <h2>MENU</h2>
            </div>

            <ul class="main-nav-links" id="mobile-nav-links">
                <li><a href="index.html"__MOBILE_ACTIVE_HOME__><i class="fa-solid fa-house"></i> Home</a></li>
                <li><a href="news.html"__MOBILE_ACTIVE_NEWS__><i class="fa-solid fa-newspaper"></i> News</a></li>
                <li><a href="fixtures.html"__MOBILE_ACTIVE_FIXTURES__><i class="fa-solid fa-calendar-days"></i> Fixtures</a></li>
                <li><a href="results.html"__MOBILE_ACTIVE_RESULTS__><i class="fa-solid fa-square-poll-vertical"></i> Results</a></li>
                <li><a href="standings.html"__MOBILE_ACTIVE_STANDINGS__><i class="fa-solid fa-table-list"></i> Standings</a></li>
                <li><a href="teams.html"__MOBILE_ACTIVE_TEAMS__><i class="fa-solid fa-shield-halved"></i> Teams</a></li>
                <li><a href="players.html"__MOBILE_ACTIVE_PLAYERS__><i class="fa-solid fa-user-group"></i> Players</a></li>
                <li><a href="transfers.html"__MOBILE_ACTIVE_TRANSFERS__><i class="fa-solid fa-right-left"></i> Transfers</a></li>
                <li><a href="statistics.html"__MOBILE_ACTIVE_STATISTICS__><i class="fa-solid fa-chart-line"></i> Statistics</a></li>
                <li><a href="livescores.html"__MOBILE_ACTIVE_LIVESCORES__><i class="fa-solid fa-satellite-dish"></i> Live Scores</a></li>
                <li><a href="videos.html"__MOBILE_ACTIVE_VIDEOS__><i class="fa-solid fa-video"></i> Videos</a></li>
                <li><a href="gallery.html"__MOBILE_ACTIVE_GALLERY__><i class="fa-solid fa-images"></i> Gallery</a></li>
                <li><a href="about.html"__MOBILE_ACTIVE_ABOUT__><i class="fa-solid fa-circle-info"></i> About TFF</a></li>
                <li><a href="contact.html"__MOBILE_ACTIVE_CONTACT__><i class="fa-solid fa-envelope"></i> Contact</a></li>
                <li><a href="#"><i class="fa-solid fa-user"></i> Login</a></li>
                <li><a href="#"><i class="fa-solid fa-user-plus"></i> Register</a></li>
            </ul>
        </div>
    </nav>"""


active_news = ["news.html", "transfers.html", "interviews.html", "features.html", "reports.html", "videos.html"]
active_matches = ["fixtures.html", "results.html", "standings.html", "livescores.html", "match-details.html"]
active_hub = ["teams.html", "players.html", "transfers.html", "statistics.html", "coach-details.html", "player-details.html", "team-details.html"]
active_ligikuu = ["nbcpremierleague.html", "championship.html", "firstleague.html", "womensleague.html"]
active_board = ["about.html"]
active_contact = ["contact.html"]
active_home = ["index.html"]

def get_active_header(filename):
    hdr = HEADER_TEMPLATE
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
    rep("__MOBILE_ACTIVE_HOME__", ' class="active"' if filename in active_home else '')
    rep("__MOBILE_ACTIVE_NEWS__", ' class="active"' if filename in active_news else '')
    rep("__MOBILE_ACTIVE_FIXTURES__", ' class="active"' if filename == "fixtures.html" else '')
    rep("__MOBILE_ACTIVE_RESULTS__", ' class="active"' if filename == "results.html" else '')
    rep("__MOBILE_ACTIVE_STANDINGS__", ' class="active"' if filename == "standings.html" else '')
    rep("__MOBILE_ACTIVE_TEAMS__", ' class="active"' if filename in ["teams.html", "team-details.html", "coach-details.html"] else '')
    rep("__MOBILE_ACTIVE_PLAYERS__", ' class="active"' if filename in ["players.html", "player-details.html"] else '')
    rep("__MOBILE_ACTIVE_TRANSFERS__", ' class="active"' if filename == "transfers.html" else '')
    rep("__MOBILE_ACTIVE_STATISTICS__", ' class="active"' if filename == "statistics.html" else '')
    rep("__MOBILE_ACTIVE_LIVESCORES__", ' class="active"' if filename == "livescores.html" else '')
    rep("__MOBILE_ACTIVE_VIDEOS__", ' class="active"' if filename == "videos.html" else '')
    rep("__MOBILE_ACTIVE_GALLERY__", ' class="active"' if filename == "gallery.html" else '')
    rep("__MOBILE_ACTIVE_ABOUT__", ' class="active"' if filename in active_board else '')
    rep("__MOBILE_ACTIVE_CONTACT__", ' class="active"' if filename in active_contact else '')
    return mob

def find_nested_div(content, start_tag):
    start_idx = content.find(start_tag)
    if start_idx == -1:
        return -1, -1
    
    nesting_level = 0
    idx = start_idx
    while idx < len(content):
        if content[idx:].lower().startswith("<div"):
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
    p_start, p_end = find_nested_div(content, '<div class="portal-header-container">')
    if p_start != -1:
        return content[:p_start], content[p_end:]
    
    t_start, t_end = find_nested_div(content, '<div class="top-header-wrapper">')
    if t_start != -1:
        nav_match = re.search(r'<nav class="main-nav[^"]*">', content[t_end:t_end+2000])
        if nav_match:
            nav_start = t_end + nav_match.start()
            nav_end = content.find("</nav>", nav_start)
            if nav_end != -1:
                return content[:t_start], content[nav_end+6:]
        return content[:t_start], content[t_end:]
    
    return None, None

def remove_old_footer(content):
    footer_match = re.search(r'<footer[^>]*>', content, re.IGNORECASE)
    if footer_match:
        f_start = footer_match.start()
        f_end = content.lower().find("</footer>", f_start)
        if f_end != -1:
            return content[:f_start], content[f_end+9:]
    return None, None

def remove_old_mobile_menu(content):
    m_start = content.find('<nav class="full-screen-menu"')
    if m_start == -1:
        m_start = content.find('<nav class="full-screen-menu')
        
    if m_start != -1:
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

def process_file(filename):
    filepath = os.path.join(workspace_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Header
    clean_prefix, clean_suffix = remove_old_header(content)
    if clean_prefix is not None:
        content = clean_prefix + "\n" + get_active_header(filename) + "\n" + clean_suffix
    else:
        body_idx = content.lower().find("<body>")
        if body_idx != -1:
            content = content[:body_idx+6] + "\n" + get_active_header(filename) + "\n" + content[body_idx+6:]
            
    # 2. Footer
    clean_prefix, clean_suffix = remove_old_footer(content)
    if clean_prefix is not None:
        content = clean_prefix + "\n" + FOOTER_TEMPLATE + "\n" + clean_suffix
        
    # 3. Mobile menu
    clean_prefix, clean_suffix = remove_old_mobile_menu(content)
    if clean_prefix is not None:
        content = clean_prefix + "\n" + get_active_mobile(filename) + "\n" + clean_suffix
        
    # Script tag placement
    script_pattern = r'<script src=["\']script\.js["\']></script>'
    content = re.sub(script_pattern, "", content)
    content = re.sub(r'<script src=["\']script\.js["\']>\s*</script>', "", content)
    
    if "full-screen-menu" not in content:
        body_close = content.lower().find("</body>")
        if body_close != -1:
            ftr_insert = ""
            if "site-footer" not in content:
                ftr_insert = FOOTER_TEMPLATE + "\n"
            content = content[:body_close] + "\n" + ftr_insert + get_active_mobile(filename) + "\n<script src=\"script.js\"></script>\n" + content[body_close:]
    else:
        body_close = content.lower().find("</body>")
        if body_close != -1:
            # check if script tag is there, if not, place it
            content = content[:body_close] + "\n<script src=\"script.js\"></script>\n" + content[body_close:]

    return content

# Test on coach-details.html and print top/bottom diff
result = process_file("coach-details.html")
print("PROCESSED COACH-DETAILS:")
print("TOP LINES:")
print("\n".join(result.splitlines()[:75]))
print("BOTTOM LINES:")
print("\n".join(result.splitlines()[-45:]))
