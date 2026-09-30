# ACT I: STRATEGIC ORIENTATION & PREPARATION (Slides 1–7)

def get_slides_act1():
    return """
      <!-- ===================================================================
           SLIDE 1: COVER & EXPEDITION METRICS
           =================================================================== -->
      <section class="slide active" data-slide="1">
        <div class="content-area" style="justify-content: center;">
          <div class="slide-eyebrow">Autumn & Spring Private Island Expedition • Master Field Guide</div>
          <h1 class="slide-title" style="font-size: 3.6rem; max-width: 1100px; margin-bottom: 1.2rem;">
            Madeira: Island of Clouds, Canyons & Atlantic Cliffs
          </h1>
          <p class="slide-subtitle" style="font-size: 1.35rem; max-width: 980px; color: var(--sand-light); line-height: 1.6;">
            An 8-day / 7-night alpine and subtropical coastal expedition across the "Hawaii of Europe"—soaring volcanic ridges above cloud seas, emerald levada gorges, ancient laurel forests, and dramatic ocean cliffscapes.
          </p>

          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin-top: 2.2rem;">
            <div class="stat-box">
              <div class="card-label">Dates & Window</div>
              <div class="stat-number" style="font-size: 1.65rem;">8 Days / 7 Nights</div>
              <div class="stat-caption">Ideal Oct–Nov or Apr–Jun • Spring & Fall Seasons</div>
            </div>
            <div class="stat-box">
              <div class="card-label">Trek Distance</div>
              <div class="stat-number">42.5 <span style="font-size: 1.2rem; color: var(--sand-muted);">MILES</span></div>
              <div class="stat-caption">68.5 KM • 5 Premier PR Routes</div>
            </div>
            <div class="stat-box">
              <div class="card-label">Vertical Gain</div>
              <div class="stat-number">+11,320 <span style="font-size: 1.2rem; color: var(--sand-muted);">FT</span></div>
              <div class="stat-caption">+3,450 M • Volcanic Ascents & Stairs</div>
            </div>
            <div class="stat-box">
              <div class="card-label">Lodging Standard</div>
              <div class="stat-number" style="font-size: 1.65rem; color: var(--teal-ocean);">100% Private</div>
              <div class="stat-caption">Quiet 3★/4★ Inns & Historic Quintas w/ Breakfast</div>
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 1.2rem;">
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--sand-muted);">
            EXPEDITION SCOPE: 42.5 MILES (68.5 KM) • +11,320 FT (+3,450M) VERTICAL • 4 MICROCLIMATES
          </div>
          <div class="tag tag-gold">MASTER FIELD DOSSIER • 2026 EDITION</div>
        </div>
      </section>

      <!-- ===================================================================
           SLIDE 2: STRATEGIC ARCHITECTURE & MICROCLIMATES
           =================================================================== -->
      <section class="slide" data-slide="2">
        <div class="slide-eyebrow">Island Topography & Route Philosophy</div>
        <h2 class="slide-title">Three Vertical Worlds & Microclimatic Strategy</h2>
        <p class="slide-subtitle">
          Rising 6,109 feet (1,862 meters) straight out of the Atlantic abyss within 3.7 miles (6 km) of the coast, Madeira creates three dramatic vertical ecosystems across a single compact island.
        </p>

        <div class="content-area">
          <div class="grid-2col">
            <div class="glass-card gold-trim">
              <div class="card-label">Topographical Architecture</div>
              <h3 class="card-heading">The Three Vertical Ecosystems</h3>
              <ul class="highlight-list">
                <li><strong>Subtropical Coastal Fringe (0–1,000 ft / 0–300m):</strong> Sunny, sheltered microclimate (68°F–75°F / 20°C–24°C). Terraced banana plantations, red volcanic cliffs, and calm ocean swimming bays along the south coast.</li>
                <li><strong>UNESCO Laurissilva Rainforest (1,000–4,250 ft / 300–1,300m):</strong> Permanent moisture belt fed by Northeast Trade Winds (<em>Alísios</em>). Dense primordial laurel forests, moss-draped gorges, and dripping hand-hewn levada aqueducts.</li>
                <li><strong>High Central Volcanic Massif (4,250–6,109 ft / 1,300–1,862m):</strong> Barren, razor-thin basalt ridges soaring above the sea of clouds. Crisp alpine air (43°F–54°F / 6°C–12°C), dramatic weather inversions, and knife-edge paths.</li>
                <li><strong>The Strategic Philosophy:</strong> Conquer high alpine peaks and narrow levadas early in the morning before afternoon trade clouds build; descend to coastal fishing villages and natural lava pools for restorative afternoons.</li>
              </ul>
            </div>

            <div class="editorial-media">
              <img src="https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?auto=format&fit=crop&w=1200&q=80" alt="Madeira Mountain Ridge Above Clouds" loading="lazy">
              <div class="media-overlay">
                <div class="media-badge">EXPEDITION PHILOSOPHY</div>
                <div class="media-title">Alpine Mornings, Ocean Evenings</div>
                <div class="media-caption">Synchronizing trail logistics with Madeira's distinct vertical weather layers guarantees maximum sunshine and optimal trail safety.</div>
              </div>
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 1.2rem;">
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--sand-muted);">
            TACTICAL PRINCIPLE: VERTICAL MOBILITY & REAL-TIME WEBCAM ROUTING
          </div>
          <div class="tag tag-teal">ISLAND TOPOGRAPHY</div>
        </div>
      </section>

      <!-- ===================================================================
           SLIDE 3: INTERACTIVE ISLAND CARTOGRAPHY & GPS DISPATCH
           =================================================================== -->
      <section class="slide" data-slide="3">
        <div class="slide-eyebrow">Island Cartography & Waypoint Command</div>
        <h2 class="slide-title">Interactive Madeira Cartography & Trail Dispatch</h2>
        <p class="slide-subtitle">
          Click or tap any waypoint below or scrub the island map to inspect premier PR trailheads, distances in miles and km, vertical gain in feet, and verified GPS links.
        </p>

        <div class="content-area">
          <div class="waypoint-selector" style="margin-bottom: 1rem;">
            <button class="stage-pill active" onclick="window.selectMapStage(0)">00 • Master Overview</button>
            <button class="stage-pill" onclick="window.selectMapStage(1)">PR8 • São Lourenço</button>
            <button class="stage-pill" onclick="window.selectMapStage(2)">PR1 • Arieiro → Ruivo</button>
            <button class="stage-pill" onclick="window.selectMapStage(3)">PR9 • Caldeirão Verde</button>
            <button class="stage-pill" onclick="window.selectMapStage(4)">Fanal • Ancient Mist Forest</button>
            <button class="stage-pill" onclick="window.selectMapStage(5)">Porto Moniz & Seixal</button>
            <button class="stage-pill" onclick="window.selectMapStage(6)">PR6 • 25 Fontes & Risco</button>
            <button class="stage-pill" onclick="window.selectMapStage(7)">Achadas da Cruz & Cabo Girão</button>
          </div>

          <div class="grid-2col">
            <div class="glass-card gold-trim interactive-trail-box" style="padding: 1.4rem;">
              <div class="card-label">Interactive Island Radar</div>
              
              <svg id="interactiveTrailSvg" viewBox="0 0 700 320" style="width: 100%; height: auto; max-height: 290px; filter: drop-shadow(0 8px 24px rgba(0,0,0,0.12));" xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <linearGradient id="madeiraCoastGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="var(--gold-primary)" stop-opacity="0.22"/>
                    <stop offset="50%" stop-color="var(--teal-ocean)" stop-opacity="0.28"/>
                    <stop offset="100%" stop-color="var(--terracotta)" stop-opacity="0.18"/>
                  </linearGradient>
                </defs>

                <!-- Island Landmass Contour -->
                <path d="M 85,150 C 75,135 90,110 115,100 C 140,90 170,95 210,85 C 250,75 285,90 330,80 C 375,70 420,85 450,95 C 480,105 510,120 540,135 C 560,140 590,145 625,148 C 650,150 675,152 680,156 C 675,162 650,160 625,158 C 595,156 570,165 550,175 C 530,185 500,210 470,225 C 440,238 395,245 350,242 C 305,240 260,235 220,225 C 180,215 145,200 120,185 C 95,170 80,160 85,150 Z" 
                      fill="url(#madeiraCoastGrad)" 
                      stroke="var(--border-gold)" 
                      stroke-width="2" 
                      stroke-linejoin="round" />

                <!-- Mountain Spine Ridge (Dashed Topographic Crest) -->
                <path d="M 120,135 C 180,125 250,140 330,135 C 380,130 430,115 480,130 C 520,140 560,155 640,152" 
                      fill="none" 
                      stroke="var(--gold-glow)" 
                      stroke-width="1.8" 
                      stroke-dasharray="4,4" 
                      opacity="0.6" />

                <!-- Node 0: Master Overview / Funchal Hub -->
                <g class="map-node active" data-stage="0" onclick="window.selectMapStage(0)" style="cursor: pointer;">
                  <circle cx="430" cy="235" r="7" fill="var(--gold-primary)" stroke="#fff" stroke-width="2"/>
                  <text x="430" y="258" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="var(--text-title)" font-weight="700">Funchal Base</text>
                </g>

                <!-- Node 1: PR8 Ponta de São Lourenço -->
                <g class="map-node" data-stage="1" onclick="window.selectMapStage(1)" style="cursor: pointer;">
                  <circle cx="650" cy="154" r="7" fill="var(--terracotta)" stroke="#fff" stroke-width="2"/>
                  <text x="650" y="142" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="var(--terracotta)" font-weight="700">PR8 São Lourenço</text>
                </g>

                <!-- Node 2: PR1 Pico do Arieiro to Ruivo -->
                <g class="map-node" data-stage="2" onclick="window.selectMapStage(2)" style="cursor: pointer;">
                  <circle cx="395" cy="140" r="7" fill="var(--gold-primary)" stroke="#fff" stroke-width="2"/>
                  <text x="395" y="126" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="var(--gold-primary)" font-weight="700">PR1 Arieiro-Ruivo</text>
                </g>

                <!-- Node 3: PR9 Levada do Caldeirão Verde -->
                <g class="map-node" data-stage="3" onclick="window.selectMapStage(3)" style="cursor: pointer;">
                  <circle cx="440" cy="115" r="7" fill="var(--teal-ocean)" stroke="#fff" stroke-width="2"/>
                  <text x="440" y="103" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="var(--teal-ocean)" font-weight="700">PR9 Caldeirão Verde</text>
                </g>

                <!-- Node 4: Fanal Ancient Mist Forest -->
                <g class="map-node" data-stage="4" onclick="window.selectMapStage(4)" style="cursor: pointer;">
                  <circle cx="180" cy="125" r="7" fill="var(--teal-ocean)" stroke="#fff" stroke-width="2"/>
                  <text x="180" y="113" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="var(--teal-ocean)" font-weight="700">Fanal Forest</text>
                </g>

                <!-- Node 5: Porto Moniz Lava Pools & Seixal -->
                <g class="map-node" data-stage="5" onclick="window.selectMapStage(5)" style="cursor: pointer;">
                  <circle cx="120" cy="98" r="7" fill="var(--gold-primary)" stroke="#fff" stroke-width="2"/>
                  <text x="120" y="86" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="var(--gold-primary)" font-weight="700">Porto Moniz Pools</text>
                </g>

                <!-- Node 6: PR6 25 Fontes & Risco -->
                <g class="map-node" data-stage="6" onclick="window.selectMapStage(6)" style="cursor: pointer;">
                  <circle cx="215" cy="165" r="7" fill="var(--teal-ocean)" stroke="#fff" stroke-width="2"/>
                  <text x="215" y="185" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="var(--teal-ocean)" font-weight="700">PR6 25 Fontes</text>
                </g>

                <!-- Node 7: Achadas da Cruz & Cabo Girão -->
                <g class="map-node" data-stage="7" onclick="window.selectMapStage(7)" style="cursor: pointer;">
                  <circle cx="370" cy="242" r="7" fill="var(--terracotta)" stroke="#fff" stroke-width="2"/>
                  <text x="370" y="265" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="var(--terracotta)" font-weight="700">Cabo Girão Skywalk</text>
                </g>
              </svg>

              <div style="font-family: var(--font-mono); font-size: 0.76rem; color: var(--sand-muted); margin-top: 8px; text-align: center;">
                TAP ANY WAYPOINT OR USE PILLS ABOVE TO INSPECT TRAIL SPECS (MILES & FEET)
              </div>
            </div>

            <div class="glass-card teal-trim" id="inspectorContent">
              <!-- Dynamically populated by window.selectMapStage -->
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 1.2rem;">
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--sand-muted);">
            TOTAL EXPEDITION ROUTE: 42.5 MILES (68.5 KM) • +11,320 FT VERTICAL GAIN • 5 PREMIER PR TRAILS
          </div>
          <div class="tag tag-gold">GPS ROUTE HUB</div>
        </div>
      </section>

      <!-- ===================================================================
           SLIDE 4: MADEIRA METEOROLOGY & MICROCLIMATES
           =================================================================== -->
      <section class="slide" data-slide="4">
        <div class="slide-eyebrow">Alpine Meteorology & Microclimates</div>
        <h2 class="slide-title">Madeira Meteorology & Cloud Inversion Survival</h2>
        <p class="slide-subtitle">
          Understanding trade winds, the Foehn effect, and why live webcams are your ultimate weapon for scoring blue skies on mountain summits.
        </p>

        <div class="content-area">
          <div class="grid-2col">
            <div class="glass-card teal-trim">
              <div class="card-label">Trade Winds & The Inversion Engine</div>
              <h3 class="card-heading">The "Sea of Clouds" Dynamic</h3>
              <ul class="highlight-list">
                <li><strong>The Alísios Mechanism:</strong> Prevailing northeast trade winds push warm Atlantic moisture against Madeira’s sheer 5,900-foot northern barrier, forcing it upward into a persistent cloud layer between 2,600 and 4,600 feet (800m to 1,400m).</li>
                <li><strong>The Temperature Inversion:</strong> Around 4,600 feet (1,400m), the cloud ceiling abruptly caps. Pico do Arieiro and Pico Ruivo emerge into brilliant sunshine above an unbroken carpet of white cotton clouds.</li>
                <li><strong>Rapid Thermal Swings:</strong> Expect a 25°F drop within a 35-minute drive from sunny Funchal (72°F / 22°C) to the windswept summit of Arieiro (46°F / 8°C). Summit wind chill can feel near freezing (32°F / 0°C) at sunrise.</li>
                <li><strong>Foehn Rain Shadow:</strong> The southern coast (Funchal, Ponta do Sol) stays warm and dry because clouds shed their moisture over the north mountains before warming as they descend the southern slopes.</li>
              </ul>
            </div>

            <div class="glass-card gold-trim">
              <div class="card-label">Field Execution Protocol</div>
              <h3 class="card-heading">The Netmadeira Live Webcam Strategy</h3>
              <div class="stat-box" style="margin-bottom: 0.9rem; padding: 10px 14px;">
                <div style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--gold-glow); text-transform: uppercase;">Essential Field URL</div>
                <div style="font-size: 1.15rem; font-weight: 700; color: var(--text-title); font-family: var(--font-mono); margin-top: 2px;">netmadeira.com/webcams</div>
                <div style="font-size: 0.75rem; color: var(--sand-muted);">Verify Pico do Arieiro, Bica da Cana, & Encumeada 30 mins before leaving hotel</div>
              </div>
              <ul class="highlight-list">
                <li><strong>Step 1 (06:00 AM Webcam Check):</strong> Open live summit cameras. If Arieiro shows clear starry skies or brilliant dawn light while Encumeada is foggy, the cloud inversion is locked in!</li>
                <li><strong>Step 2 (Adaptive Decision):</strong> If summit webcams reveal total gray soup with high winds (>30 mph / >50 km/h), swap the day: do a sheltered low-elevation levada or sunny coastal walk instead.</li>
                <li><strong>Rain Radar Vigilance:</strong> Check IPMA (Portuguese Met Institute) Madeira Doppler radar for convective cells before entering narrow canyons like Caldeirão Verde.</li>
              </ul>
              <div class="field-alert" style="margin-top: 0.8rem; padding: 0.9rem 1.1rem;">
                <div class="field-alert-icon">⚠️</div>
                <div class="field-alert-text" style="font-size: 0.92rem; line-height: 1.45;">
                  Never hike exposed razor crests or steep levadas during official orange wind/rain alerts from Proteção Civil. Rockfalls and flash flooding can occur rapidly.
                </div>
              </div>
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 1.2rem;">
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--sand-muted);">
            METEOROLOGY RULE: NEVER DRIVE TO HIGH PEAKS BLIND—ALWAYS VERIFY NETMADEIRA WEBCAMS FIRST
          </div>
          <div class="tag tag-terracotta">WEATHER PROTOCOL</div>
        </div>
      </section>

      <!-- ===================================================================
           SLIDE 5: ISLAND DRIVING & RENTAL LOGISTICS
           =================================================================== -->
      <section class="slide" data-slide="5">
        <div class="slide-eyebrow">Ground Logistics & Mountain Roads</div>
        <h2 class="slide-title">Island Driving, Rental Architecture & Tunnels</h2>
        <p class="slide-subtitle">
          Navigating 150+ highway tunnels, the 65 mph (100 km/h) VR1 coastal expressway, and 25% cobblestone mountain switchbacks—vehicle selection and driving etiquette.
        </p>

        <div class="content-area">
          <div class="grid-2col-wide-left">
            <div class="glass-card gold-trim" id="transitDetailCard-5">
              <!-- Dynamically populated by window.switchTransitOption(5, optIdx) -->
            </div>

            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div class="transit-option-card active" data-opt="0" onclick="window.switchTransitOption(5, 0)">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="font-size: 0.95rem; color: var(--text-title);">Compact Turbo Petrol (1.0L / 1.2L Turbo)</strong>
                  <span class="tag tag-gold" style="font-size: 0.65rem;">RECOMMENDED</span>
                </div>
                <p style="font-size: 0.82rem; color: var(--sand-muted); margin-top: 4px;">Essential low-end climbing torque for steep 20–25% village switchbacks.</p>
              </div>

              <div class="transit-option-card" data-opt="1" onclick="window.switchTransitOption(5, 1)">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="font-size: 0.95rem; color: var(--text-title);">Compact Automatic Crossover (e.g. Captur / T-Roc)</strong>
                  <span class="tag tag-teal" style="font-size: 0.65rem;">MAX COMFORT</span>
                </div>
                <p style="font-size: 0.82rem; color: var(--sand-muted); margin-top: 4px;">Automatic hill-start assist prevents rolling backwards on extreme inclines.</p>
              </div>

              <div class="transit-option-card" data-opt="2" onclick="window.switchTransitOption(5, 2)">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="font-size: 0.95rem; color: var(--terracotta);">Naturally Aspirated 1.0L Non-Turbo</strong>
                  <span class="tag tag-terracotta" style="font-size: 0.65rem;">FATAL FLAW</span>
                </div>
                <p style="font-size: 0.82rem; color: var(--sand-muted); margin-top: 4px;">Severely lacks torque; burns clutches on 25% grades with 2 pax & luggage.</p>
              </div>

              <div class="transit-option-card" data-opt="3" onclick="window.switchTransitOption(5, 3)">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="font-size: 0.95rem; color: var(--text-title);">Public Coaches & Mountain Trail Shuttles</strong>
                  <span class="tag tag-gold" style="font-size: 0.65rem;">BUDGET / RIGID</span>
                </div>
                <p style="font-size: 0.82rem; color: var(--sand-muted); margin-top: 4px;">Cheap, but rigid timetables make 07:00 AM alpine sunrises impossible.</p>
              </div>
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 1.2rem;">
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--sand-muted);">
            CIVIL ENGINEERING: 150+ MODERN TUNNELS MAKE CROSS-ISLAND DRIVING FAST & SAFE
          </div>
          <div class="tag tag-gold">DRIVING ARCHITECTURE</div>
        </div>
      </section>

      <!-- ===================================================================
           SLIDE 6: LEVADA TRAIL SAFETY & ETIQUETTE
           =================================================================== -->
      <section class="slide" data-slide="6">
        <div class="slide-eyebrow">Trail Safety & Cultural Etiquette</div>
        <h2 class="slide-title">Levada Safety, Tunnel Protocols & ICNF Permits</h2>
        <p class="slide-subtitle">
          Historic 15th-century stone aqueducts clinging to vertical cliff walls require disciplined field protocols, headlamps, and newly introduced trail permits.
        </p>

        <div class="content-area">
          <div class="grid-2col">
            <div class="glass-card terracotta-trim">
              <div class="card-label">Levada Cliff & Tunnel Protocols</div>
              <h3 class="card-heading">Narrow Wall Passing & Tunnel Etiquette</h3>
              <ul class="highlight-list">
                <li><strong>Anatomy of a Levada:</strong> Maintenance walkways are frequently only 16 to 32 inches (40–80 cm) wide, with a rushing water channel on one side and a sheer cliff drop-off (often 300+ ft / 100m+) on the other.</li>
                <li><strong>Two-Way Passing Etiquette:</strong> When meeting oncoming hikers on narrow ledges, the hiker on the outer wall steps toward the mountain or hugs the rock face. Always halt completely before passing.</li>
                <li><strong>Water Tunnels (Túneis):</strong> Premier levadas (PR9 Caldeirão Verde, PR6 25 Fontes) pass through long, unlit tunnels (up to 3,300 ft / 1,000m long). A 300+ lumen waterproof headlamp is mandatory. Smartphone torches are inadequate and easily dropped in water.</li>
                <li><strong>Basalt Ceiling Collisions:</strong> Tunnels are hand-carved with low, jagged basalt rock roofs. Keep your head down and wear a hooded jacket or baseball cap to absorb glancing bumps.</li>
                <li><strong>Vertigo Cable Railings:</strong> Steel safety cables line exposed cliff drop-offs. Never lean your full body weight against them or hang heavy backpacks from them.</li>
              </ul>
            </div>

            <div class="glass-card gold-trim">
              <div class="card-label">Official ICNF Conservation Permits</div>
              <h3 class="card-heading">The €3/Trail Simplifica Permit System</h3>
              <ul class="highlight-list">
                <li><strong>Mandatory PR Trail Permits:</strong> The Regional Government (ICNF) mandates a €3 permit fee per non-resident hiker across classified trails (PR1, PR1.2, PR6, PR8, PR9, PR11).</li>
                <li><strong>Advance Online Purchase:</strong> Buy permits via <em>simplifica.madeira.gov.pt</em>. Save digital PDF QR codes to your phone's offline wallet (cellular data is zero inside deep canyons!).</li>
                <li><strong>Field Ranger Inspections:</strong> Uniformed Forestry Police (<em>Polícia Florestal</em>) patrol trailheads and levada entries. Hiking without an official permit carries fines of €50 to €500.</li>
                <li><strong>Real-Time Trail Status:</strong> Levadas occasionally close due to rockfalls or heavy rains. Always verify active trail status at <em>ifcn.madeira.gov.pt</em> before driving out.</li>
              </ul>
              <div class="property-pill" style="margin-top: 1rem;">
                <div style="font-family: var(--font-mono); font-size: 0.74rem; color: var(--gold-glow); text-transform: uppercase;">Permit Allocation for 2 Hikers</div>
                <div style="font-size: 1.15rem; font-weight: 700; color: var(--text-title); margin-top: 2px;">5 PR Trails × €3 = €30 Total Shared Permit Cost</div>
                <div style="font-size: 0.78rem; color: var(--sand-muted);">Includes PR1 Arieiro-Ruivo, PR8 São Lourenço, PR9 Caldeirão Verde, PR6 25 Fontes, and PR1.2 Teixeira</div>
              </div>
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 1.2rem;">
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--sand-muted);">
            SAFETY MANDATE: ALWAYS CARRY A 300+ LUMEN HEADLAMP ON ALL LEVADA TREKS
          </div>
          <div class="tag tag-teal">TRAIL PROTOCOL</div>
        </div>
      </section>

      <!-- ===================================================================
           SLIDE 7: TECHNICAL PACKING LIST & GEAR DIRECTORY
           =================================================================== -->
      <section class="slide" data-slide="7">
        <div class="slide-eyebrow">Equipment Architecture & Field Gear</div>
        <h2 class="slide-title">Technical Packing Directory: Peaks to Ocean Pools</h2>
        <p class="slide-subtitle">
          Essential alpine, levada, and subtropical coastal kit engineered for cold volcanic ridges, wet unlit tunnels, and Atlantic tidal pools.
        </p>

        <div class="content-area">
          <div class="grid-2col">
            <div class="glass-card teal-trim">
              <div class="card-label">Trail & Alpine Performance Kit</div>
              <h3 class="card-heading">Footwear, Lighting & Hard Shells</h3>
              <ul class="highlight-list">
                <li><strong>Trail Runners with Sticky Outsoles:</strong> Vibram Megagrip or Contagrip lugs (e.g. Hoka Speedgoat, Brooks Cascadia). Smooth road running shoes are treacherous on wet basalt stone and levada algae.</li>
                <li><strong>High-Lumen Waterproof Headlamp:</strong> Minimum 300–450 lumens with wide flood beam (Black Diamond Storm / Petzl Actik). Crucial for PR9's 4 dark tunnels and PR1 sunrise starts.</li>
                <li><strong>Packable Waterproof Hard Shell:</strong> 2.5L or 3L lightweight breathable jacket (Gore-Tex / Pertex). Essential for sudden cloudbursts, dripping levada tunnels, and summit wind chill.</li>
                <li><strong>Layered Fleece / Down Sweater:</strong> High peaks drop to 43°F–46°F (6°C–8°C) at sunrise. A packable micro-puff down jacket is ideal for waiting at Miradouro do Juncal.</li>
                <li><strong>Telescopic Trekking Poles:</strong> Must have rubber tip caps (metal carbide tips can damage stone stairways and are prohibited on some wooden walkways).</li>
              </ul>
            </div>

            <div class="glass-card gold-trim">
              <div class="card-label">Electronics, Hydration & Ocean Kit</div>
              <h3 class="card-heading">Navigation, Power & Subtropical Essentials</h3>
              <ul class="highlight-list">
                <li><strong>Offline GPS Nav & Power Bank:</strong> 10,000 mAh battery bank. Download Madeira offline maps on AllTrails Pro, Wikiloc, and Maps.me (canyons have zero cell reception).</li>
                <li><strong>10L–15L Waterproof Dry Bag:</strong> Protects phones, car keys, and spare dry socks from tunnel drippings and waterfall spray at Caldeirão Verde.</li>
                <li><strong>Hydration & Trail Snacks:</strong> Minimum 50 oz (1.5 Liters) capacity per person. Electrolytes and energy bars (plus sweet local Madeira bananas and Queijadas).</li>
                <li><strong>Ocean Swim & Pool Gear:</strong> Quick-dry microfiber towel and swimwear packed in the car trunk for post-hike plunges at Porto Moniz and Seixal.</li>
                <li><strong>Sun & Wind Defense:</strong> Polarized sunglasses and SPF 50 sunscreen—UV index is intense on high peaks and unshaded Ponta de São Lourenço.</li>
              </ul>
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 1.2rem;">
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--sand-muted);">
            GEAR STRATEGY: LIGHTWEIGHT LAYERS COVERING 43°F (6°C) SUMMITS TO 75°F (24°C) OCEAN POOLS
          </div>
          <div class="tag tag-gold">MASTER GEAR KIT</div>
        </div>
      </section>
"""

if __name__ == '__main__':
    slides = get_slides_act1()
    print("Act 1 updated with American units.")
