$files = Get-ChildItem -Path . -Filter *.html

$HEADER_TEMPLATE = @"
    <div class="portal-header-container">
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
    </div>
"@

$FOOTER_TEMPLATE = @"
    <footer class="site-footer reveal-element">
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
    </footer>
"@

$MOBILE_MENU_TEMPLATE = @"
    <!-- Professional Sliding Mobile Menu -->
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
    </nav>
"@

$active_news = @("news.html", "transfers.html", "interviews.html", "features.html", "reports.html", "videos.html")
$active_matches = @("fixtures.html", "results.html", "standings.html", "livescores.html", "match-details.html")
$active_hub = @("teams.html", "players.html", "transfers.html", "statistics.html", "coach-details.html", "player-details.html", "team-details.html")
$active_ligikuu = @("nbcpremierleague.html", "championship.html", "firstleague.html", "womensleague.html")
$active_board = @("about.html")
$active_contact = @("contact.html")
$active_home = @("index.html")

function Get-ActiveHeader($filename) {
    $hdr = $HEADER_TEMPLATE
    
    $isHome = ""
    if ($active_home -contains $filename) { $isHome = ' class="active"' }
    
    $isNews = ""
    if ($active_news -contains $filename) { $isNews = ' active' }
    
    $isNewsL = ""
    if ($filename -eq "news.html") { $isNewsL = ' class="active"' }
    
    $isTrans = ""
    if ($filename -eq "transfers.html") { $isTrans = ' class="active"' }
    
    $isInt = ""
    if ($filename -eq "interviews.html") { $isInt = ' class="active"' }
    
    $isFeat = ""
    if ($filename -eq "features.html") { $isFeat = ' class="active"' }
    
    $isRep = ""
    if ($filename -eq "reports.html") { $isRep = ' class="active"' }
    
    $isVid = ""
    if ($filename -eq "videos.html") { $isVid = ' class="active"' }
    
    $isMatches = ""
    if ($active_matches -contains $filename) { $isMatches = ' active' }
    
    $isFix = ""
    if ($filename -eq "fixtures.html") { $isFix = ' class="active"' }
    
    $isCal = ""
    if ($filename -eq "calendar.html") { $isCal = ' class="active"' }
    
    $isRes = ""
    if ($filename -eq "results.html") { $isRes = ' class="active"' }
    
    $isStd = ""
    if ($filename -eq "standings.html") { $isStd = ' class="active"' }
    
    $isLive = ""
    if ($filename -eq "livescores.html") { $isLive = ' class="active"' }
    
    $isHub = ""
    if ($active_hub -contains $filename) { $isHub = ' active' }
    
    $isTeams = ""
    if (@("teams.html", "team-details.html", "coach-details.html") -contains $filename) { $isTeams = ' class="active"' }
    
    $isPlr = ""
    if (@("players.html", "player-details.html") -contains $filename) { $isPlr = ' class="active"' }
    
    $isStat = ""
    if ($filename -eq "statistics.html") { $isStat = ' class="active"' }
    
    $isLigi = ""
    if ($active_ligikuu -contains $filename) { $isLigi = ' active' }
    
    $isNbc = ""
    if ($filename -eq "nbcpremierleague.html") { $isNbc = ' class="active"' }
    
    $isChmp = ""
    if ($filename -eq "championship.html") { $isChmp = ' class="active"' }
    
    $isFst = ""
    if ($filename -eq "firstleague.html") { $isFst = ' class="active"' }
    
    $isWmn = ""
    if ($filename -eq "womensleague.html") { $isWmn = ' class="active"' }
    
    $isBrd = ""
    if ($active_board -contains $filename) { $isBrd = ' active' }
    
    $isAbout = ""
    if ($filename -eq "about.html") { $isAbout = ' class="active"' }
    
    $isContact = ""
    if ($active_contact -contains $filename) { $isContact = ' class="active"' }
    
    $hdr = $hdr.Replace("__ACTIVE_HOME__", $isHome)
    $hdr = $hdr.Replace("__ACTIVE_NEWS_PARENT__", $isNews)
    $hdr = $hdr.Replace("__ACTIVE_NEWS_LATEST__", $isNewsL)
    $hdr = $hdr.Replace("__ACTIVE_TRANSFERS_NEWS__", $isTrans)
    $hdr = $hdr.Replace("__ACTIVE_INTERVIEWS__", $isInt)
    $hdr = $hdr.Replace("__ACTIVE_FEATURES__", $isFeat)
    $hdr = $hdr.Replace("__ACTIVE_REPORTS__", $isRep)
    $hdr = $hdr.Replace("__ACTIVE_VIDEOS__", $isVid)
    
    $hdr = $hdr.Replace("__ACTIVE_MATCHES_PARENT__", $isMatches)
    $hdr = $hdr.Replace("__ACTIVE_FIXTURES__", $isFix)
    $hdr = $hdr.Replace("__ACTIVE_CALENDAR__", $isCal)
    $hdr = $hdr.Replace("__ACTIVE_RESULTS__", $isRes)
    $hdr = $hdr.Replace("__ACTIVE_STANDINGS__", $isStd)
    $hdr = $hdr.Replace("__ACTIVE_LIVESCORES__", $isLive)
    
    $hdr = $hdr.Replace("__ACTIVE_HUB_PARENT__", $isHub)
    $hdr = $hdr.Replace("__ACTIVE_TEAMS__", $isTeams)
    $hdr = $hdr.Replace("__ACTIVE_PLAYERS__", $isPlr)
    $hdr = $hdr.Replace("__ACTIVE_TRANSFERS_HUB__", $isTrans)
    $hdr = $hdr.Replace("__ACTIVE_STATISTICS__", $isStat)
    
    $hdr = $hdr.Replace("__ACTIVE_LIGIKUU_PARENT__", $isLigi)
    $hdr = $hdr.Replace("__ACTIVE_NBC__", $isNbc)
    $hdr = $hdr.Replace("__ACTIVE_CHAMPIONSHIP__", $isChmp)
    $hdr = $hdr.Replace("__ACTIVE_FIRSTLEAGUE__", $isFst)
    $hdr = $hdr.Replace("__ACTIVE_WOMENSLEAGUE__", $isWmn)
    
    $hdr = $hdr.Replace("__ACTIVE_BOARD_PARENT__", $isBrd)
    $hdr = $hdr.Replace("__ACTIVE_ABOUTBOARD__", $isAbout)
    $hdr = $hdr.Replace("__ACTIVE_HISTORY__", "")
    $hdr = $hdr.Replace("__ACTIVE_MEMBERS__", "")
    $hdr = $hdr.Replace("__ACTIVE_SECRETARIAT__", "")
    
    $hdr = $hdr.Replace("__ACTIVE_CONTACT__", $isContact)
    
    return $hdr
}

function Get-ActiveMobile($filename) {
    $mob = $MOBILE_MENU_TEMPLATE
    
    $isHome = ""; if ($active_home -contains $filename) { $isHome = ' class="active"' }
    $isNews = ""; if ($active_news -contains $filename) { $isNews = ' class="active"' }
    $isFix = ""; if ($filename -eq "fixtures.html") { $isFix = ' class="active"' }
    $isCal = ""; if ($filename -eq "calendar.html") { $isCal = ' class="active"' }
    $isRes = ""; if ($filename -eq "results.html") { $isRes = ' class="active"' }
    $isStd = ""; if ($filename -eq "standings.html") { $isStd = ' class="active"' }
    $isTeams = ""; if (@("teams.html", "team-details.html", "coach-details.html") -contains $filename) { $isTeams = ' class="active"' }
    $isPlr = ""; if (@("players.html", "player-details.html") -contains $filename) { $isPlr = ' class="active"' }
    $isTrans = ""; if ($filename -eq "transfers.html") { $isTrans = ' class="active"' }
    $isStat = ""; if ($filename -eq "statistics.html") { $isStat = ' class="active"' }
    $isLive = ""; if ($filename -eq "livescores.html") { $isLive = ' class="active"' }
    $isVid = ""; if ($filename -eq "videos.html") { $isVid = ' class="active"' }
    $isGal = ""; if ($filename -eq "gallery.html") { $isGal = ' class="active"' }
    $isBrd = ""; if ($active_board -contains $filename) { $isBrd = ' class="active"' }
    $isContact = ""; if ($active_contact -contains $filename) { $isContact = ' class="active"' }
    
    $mob = $mob.Replace("__MOBILE_ACTIVE_HOME__", $isHome)
    $mob = $mob.Replace("__MOBILE_ACTIVE_NEWS__", $isNews)
    $mob = $mob.Replace("__MOBILE_ACTIVE_FIXTURES__", $isFix)
    $mob = $mob.Replace("__MOBILE_ACTIVE_CALENDAR__", $isCal)
    $mob = $mob.Replace("__MOBILE_ACTIVE_RESULTS__", $isRes)
    $mob = $mob.Replace("__MOBILE_ACTIVE_STANDINGS__", $isStd)
    $mob = $mob.Replace("__MOBILE_ACTIVE_TEAMS__", $isTeams)
    $mob = $mob.Replace("__MOBILE_ACTIVE_PLAYERS__", $isPlr)
    $mob = $mob.Replace("__MOBILE_ACTIVE_TRANSFERS__", $isTrans)
    $mob = $mob.Replace("__MOBILE_ACTIVE_STATISTICS__", $isStat)
    $mob = $mob.Replace("__MOBILE_ACTIVE_LIVESCORES__", $isLive)
    $mob = $mob.Replace("__MOBILE_ACTIVE_VIDEOS__", $isVid)
    $mob = $mob.Replace("__MOBILE_ACTIVE_GALLERY__", $isGal)
    $mob = $mob.Replace("__MOBILE_ACTIVE_ABOUT__", $isBrd)
    $mob = $mob.Replace("__MOBILE_ACTIVE_CONTACT__", $isContact)
    
    return $mob
}

function Find-NestedDiv($content, $startTag) {
    $startIdx = $content.IndexOf($startTag)
    if ($startIdx -eq -1) { return -1, -1 }
    
    $nestingLevel = 0
    $idx = $startIdx
    while ($idx -lt $content.Length) {
        if ($content.Substring($idx).StartsWith("<div", [System.StringComparison]::OrdinalIgnoreCase)) {
            $nestingLevel++
            $idx += 4
            continue
        } elseif ($content.Substring($idx).StartsWith("</div>", [System.StringComparison]::OrdinalIgnoreCase)) {
            $nestingLevel--
            if ($nestingLevel -eq 0) {
                return $startIdx, ($idx + 6)
            }
            $idx += 6
            continue
        }
        $idx++
    }
    return -1, -1
}

function Remove-OldHeader($content) {
    $start, $end = Find-NestedDiv $content '<div class="portal-header-container">'
    if ($start -ne -1) {
        return $content.Substring(0, $start) + "`n" + (Get-ActiveHeader $filename) + "`n" + $content.Substring($end)
    }
    return $content
}

function Remove-OldFooter($content) {
    # Match footer opening tag and closing </footer>
    $footerStart = $content.IndexOf("<footer")
    if ($footerStart -eq -1) { return $content }
    $footerEnd = $content.IndexOf("</footer>", $footerStart)
    if ($footerEnd -eq -1) { return $content }
    
    return $content.Substring(0, $footerStart) + "`n" + $FOOTER_TEMPLATE + "`n" + $content.Substring($footerEnd + 9)
}

function Remove-OldMobileMenu($content) {
    $mStart = $content.IndexOf('<nav class="full-screen-menu"')
    if ($mStart -eq -1) {
        $mStart = $content.IndexOf('<nav class="full-screen-menu')
    }
    if ($mStart -eq -1) { return $content }
    
    $nesting = 0
    $idx = $mStart
    $mEnd = -1
    while ($idx -lt $content.Length) {
        if ($content.Substring($idx).StartsWith("<nav", [System.StringComparison]::OrdinalIgnoreCase)) {
            $nesting++
            $idx += 4
            continue
        } elseif ($content.Substring($idx).StartsWith("</nav>", [System.StringComparison]::OrdinalIgnoreCase)) {
            $nesting--
            if ($nesting -eq 0) {
                $mEnd = $idx + 6
                break
            }
            $idx += 6
            continue
        }
        $idx++
    }
    
    if ($mEnd -ne -1) {
        return $content.Substring(0, $mStart) + "`n" + (Get-ActiveMobile $filename) + "`n" + $content.Substring($mEnd)
    }
    return $content
}

foreach ($file in $files) {
    $filename = $file.Name
    Write-Host "Standardizing $filename..."
    
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    
    $content = Remove-OldHeader $content
    $content = Remove-OldFooter $content
    $content = Remove-OldMobileMenu $content
    
    # Remove existing script.js imports
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '<script src=["'']script\.js["'']></script>', "")
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '<script src=["'']script\.js["'']>\s*</script>', "")
    
    # Insert script.js before </body>
    $bodyClose = $content.IndexOf("</body>")
    if ($bodyClose -ne -1) {
        $content = $content.Substring(0, $bodyClose) + "`n<script src=`"script.js`"></script>`n" + $content.Substring($bodyClose)
    }
    
    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}

Write-Host "All files standardized successfully!"
