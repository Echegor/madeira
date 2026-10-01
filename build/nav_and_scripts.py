# Navigation Elements, Drawer Sheet, Footer & JavaScript Controller for Madeira Deck

def get_header_and_drawer():
    return """
    <!-- Top Navigation Header -->
    <header class="deck-header">
      <div class="brand-nav-container">
        <button class="header-brand" id="deckDrawerTrigger" type="button" aria-label="Open Slide Navigation Sheet" title="Open Slide Index (List all 30 pages)">
          <span class="brand-crest-box">
            <svg class="brand-compass-svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10" stroke="var(--gold-primary)" stroke-width="1.8"/>
              <polygon points="12 2 15 9 22 12 15 15 12 22 9 15 2 12 9 9 12 2" fill="var(--gold-primary)"/>
            </svg>
          </span>
          <span class="brand-title">Madeira Island Alpine & Coastal Expedition</span>
          <span class="brand-drawer-badge">
            <span class="badge-text-primary">INDEX</span>
            <span class="badge-dot">•</span>
            <span class="badge-text-sub">30 SLIDES</span>
            <span class="badge-chevron">▾</span>
          </span>
        </button>
        <!-- Built-in Native Mobile Dropdown Component (triggers native Android / iOS system bottom sheet) -->
        <select class="native-slide-select" id="nativeSlidePicker" onchange="window.goToSlide(parseInt(this.value, 10))" title="Quick Jump to Slide" aria-label="Quick Jump to Slide">
          <optgroup label="📍 ACT I: STRATEGIC ORIENTATION (SLIDES 1–7)">
            <option value="0">Slide 01 • Cover & Expedition Metrics</option>
            <option value="1">Slide 02 • Strategic Architecture & Microclimates</option>
            <option value="2">Slide 03 • Interactive Cartography & GPS Dispatch</option>
            <option value="3">Slide 04 • Meteorology & Cloud Inversions</option>
            <option value="4">Slide 05 • Island Driving & Rental Logistics</option>
            <option value="5">Slide 06 • Levada Safety & Trail Permits</option>
            <option value="6">Slide 07 • Technical Packing List & Gear</option>
          </optgroup>
          <optgroup label="🐉 ACT II: EAST COAST & DRAGON'S TAIL (SLIDES 8–13)">
            <option value="7">Slide 08 • Day 1: FNC Arrival & Historic Funchal</option>
            <option value="8">Slide 09 • Night 1: Funchal Boutique 3★/4★ Base</option>
            <option value="9">Slide 10 • Night 1: Authentic Espetada & Bolo do Caco</option>
            <option value="10">Slide 11 • Day 2: Ponta de São Lourenço (PR8)</option>
            <option value="11">Slide 12 • Day 2: Caniçal Harbor & Prainha Beach</option>
            <option value="12">Slide 13 • Night 2: East Coast Sanctuary (Machico)</option>
          </optgroup>
          <optgroup label="⛰️ ACT III: ALPINE PEAKS & LEVADAS (SLIDES 14–19)">
            <option value="13">Slide 14 • Day 3: PR1 Pico do Arieiro to Pico Ruivo</option>
            <option value="14">Slide 15 • Day 3: Alpine Sunrise & Shuttle Logistics</option>
            <option value="15">Slide 16 • Night 3: Quinta do Furão (Santana Cliffs)</option>
            <option value="16">Slide 17 • Day 4: PR9 Levada do Caldeirão Verde</option>
            <option value="17">Slide 18 • Day 4: Santana Thatched Houses & Lunch</option>
            <option value="18">Slide 19 • Night 4: North Coast Ocean View Inn</option>
          </optgroup>
          <optgroup label="🌊 ACT IV: MIST FORESTS & OCEAN POOLS (SLIDES 20–24)">
            <option value="19">Slide 20 • Day 5: Fanal Ancient Mist Forest (UNESCO)</option>
            <option value="20">Slide 21 • Day 5: Porto Moniz Lava Pools & Seixal</option>
            <option value="21">Slide 22 • Night 5: Northwest Ocean Sanctuary</option>
            <option value="22">Slide 23 • Day 6: PR6 25 Fontes & Risco Cascades</option>
            <option value="23">Slide 24 • Day 6: Achadas da Cruz & Cabo Girão</option>
          </optgroup>
          <optgroup label="🏛️ ACT V: FUNCHAL FINALE & SCORECARD (SLIDES 25–30)">
            <option value="24">Slide 25 • Night 6 & 7: Return to Funchal Seaside</option>
            <option value="25">Slide 26 • Day 7: Monte Palace Gardens & Wicker Sledge</option>
            <option value="26">Slide 27 • Day 7: Grand Farewell Seafood Feast</option>
            <option value="27">Slide 28 • Day 8: FNC Runway & Departure Flow</option>
            <option value="28">Slide 29 • Master Scorecard & Shared Financial Ledger</option>
            <option value="29">Slide 30 • Zero-Fail SOS Directory & Rescue Toolkit</option>
          </optgroup>
        </select>
      </div>
      <div class="header-controls">
        <button class="btn-fs" id="themeBtn" title="Click to Cycle Color Scheme" style="border-color: var(--gold-primary); color: var(--gold-primary); font-weight: 700;">🎨 PALETTE: Porcelain & Slate</button>
        <div class="slide-counter" id="slideCounter">SLIDE 01 / 30</div>
        <button class="btn-fs" id="fullscreenBtn" title="Toggle Fullscreen">⛶ EXPAND</button>
      </div>
    </header>

    <!-- Slide Navigation Drawer & Page Selection Sheet -->
    <div class="drawer-overlay" id="drawerOverlay" aria-hidden="true">
      <div class="drawer-backdrop" id="drawerBackdrop" title="Close Directory"></div>
      <aside class="drawer-sheet" id="drawerSheet" role="dialog" aria-modal="true" aria-labelledby="drawerTitle">
        <!-- Touch pull handle for mobile bottom-sheet -->
        <div class="drawer-drag-bar" id="drawerDragBar" title="Swipe down to close">
          <div class="drawer-drag-pill"></div>
        </div>

        <!-- Drawer Header -->
        <div class="drawer-header">
          <div class="drawer-header-text">
            <div class="drawer-eyebrow">MADEIRA EXPEDITION DOSSIER • 30 MILESTONES</div>
            <h3 class="drawer-title" id="drawerTitle">Slide Directory</h3>
          </div>
          <button class="drawer-close-btn" id="drawerCloseBtn" type="button" aria-label="Close Slide Directory" title="Close Directory">✕</button>
        </div>

        <!-- Search & Filter Controls -->
        <div class="drawer-search-row">
          <div class="drawer-search-wrapper">
            <span class="drawer-search-icon">🔍</span>
            <input type="text" class="drawer-search-input" id="drawerSearchInput" placeholder="Search slide number, PR trail, hotel, or village..." aria-label="Search slides" autocomplete="off" />
            <button class="drawer-search-clear" id="drawerSearchClear" type="button" aria-label="Clear search" style="display: none;">✕</button>
          </div>
          <div class="drawer-filter-pills" id="drawerFilterPills">
            <button class="drawer-filter-pill active" data-filter="all" type="button">All (30)</button>
            <button class="drawer-filter-pill" data-filter="trail" type="button">Trails & Peaks (10)</button>
            <button class="drawer-filter-pill" data-filter="retreat" type="button">Lodging (6)</button>
            <button class="drawer-filter-pill" data-filter="dining" type="button">Gastronomy (4)</button>
            <button class="drawer-filter-pill" data-filter="transit" type="button">Transit (5)</button>
            <button class="drawer-filter-pill" data-filter="overview" type="button">Strategy (8)</button>
          </div>
        </div>

        <!-- Scrollable Slide Items List -->
        <div class="drawer-list" id="drawerList">
          <!-- Dynamically populated by JS from the 30 slide sections -->
        </div>

        <!-- Drawer Footer Stats -->
        <div class="drawer-footer">
          <div class="drawer-stat">42.5 MILES PR TRAILS</div>
          <div class="drawer-stat">•</div>
          <div class="drawer-stat">+11,320 FT ASCENT</div>
          <div class="drawer-stat">•</div>
          <div class="drawer-stat">4 MICROCLIMATES</div>
        </div>
      </aside>
    </div>
"""

def get_footer():
    return """
    <!-- Bottom Controls & Progress Navigation -->
    <footer class="deck-footer">
      <div class="progress-dots" id="dotsContainer">
        <!-- 30 Dots dynamically generated -->
      </div>
      <div class="mobile-slide-indicator-container">
        <button class="mobile-slide-indicator" id="mobileSlideIndicator" type="button" title="Open Slide Directory">
          <span style="color: var(--gold-primary); font-weight: 800;">SLIDE 01</span>
          <span style="opacity: 0.4;">/</span>
          <span style="opacity: 0.75;">30</span>
          <span style="color: var(--gold-primary); margin-left: 2px;">▾</span>
        </button>
        <select class="native-slide-select" id="footerSlidePicker" onchange="window.goToSlide(parseInt(this.value, 10))" title="Quick Jump to Slide" aria-label="Quick Jump to Slide">
          <optgroup label="📍 ACT I: STRATEGIC ORIENTATION (SLIDES 1–7)">
            <option value="0">Slide 01 • Cover & Expedition Metrics</option>
            <option value="1">Slide 02 • Strategic Architecture & Microclimates</option>
            <option value="2">Slide 03 • Interactive Cartography & GPS Dispatch</option>
            <option value="3">Slide 04 • Meteorology & Cloud Inversions</option>
            <option value="4">Slide 05 • Island Driving & Rental Logistics</option>
            <option value="5">Slide 06 • Levada Safety & Trail Permits</option>
            <option value="6">Slide 07 • Technical Packing List & Gear</option>
          </optgroup>
          <optgroup label="🐉 ACT II: EAST COAST & DRAGON'S TAIL (SLIDES 8–13)">
            <option value="7">Slide 08 • Day 1: FNC Arrival & Historic Funchal</option>
            <option value="8">Slide 09 • Night 1: Funchal Boutique 3★/4★ Base</option>
            <option value="9">Slide 10 • Night 1: Authentic Espetada & Bolo do Caco</option>
            <option value="10">Slide 11 • Day 2: Ponta de São Lourenço (PR8)</option>
            <option value="11">Slide 12 • Day 2: Caniçal Harbor & Prainha Beach</option>
            <option value="12">Slide 13 • Night 2: East Coast Sanctuary (Machico)</option>
          </optgroup>
          <optgroup label="⛰️ ACT III: ALPINE PEAKS & LEVADAS (SLIDES 14–19)">
            <option value="13">Slide 14 • Day 3: PR1 Pico do Arieiro to Pico Ruivo</option>
            <option value="14">Slide 15 • Day 3: Alpine Sunrise & Shuttle Logistics</option>
            <option value="15">Slide 16 • Night 3: Quinta do Furão (Santana Cliffs)</option>
            <option value="16">Slide 17 • Day 4: PR9 Levada do Caldeirão Verde</option>
            <option value="17">Slide 18 • Day 4: Santana Thatched Houses & Lunch</option>
            <option value="18">Slide 19 • Night 4: North Coast Ocean View Inn</option>
          </optgroup>
          <optgroup label="🌊 ACT IV: MIST FORESTS & OCEAN POOLS (SLIDES 20–24)">
            <option value="19">Slide 20 • Day 5: Fanal Ancient Mist Forest (UNESCO)</option>
            <option value="20">Slide 21 • Day 5: Porto Moniz Lava Pools & Seixal</option>
            <option value="21">Slide 22 • Night 5: Northwest Ocean Sanctuary</option>
            <option value="22">Slide 23 • Day 6: PR6 25 Fontes & Risco Cascades</option>
            <option value="23">Slide 24 • Day 6: Achadas da Cruz & Cabo Girão</option>
          </optgroup>
          <optgroup label="🏛️ ACT V: FUNCHAL FINALE & SCORECARD (SLIDES 25–30)">
            <option value="24">Slide 25 • Night 6 & 7: Return to Funchal Seaside</option>
            <option value="25">Slide 26 • Day 7: Monte Palace Gardens & Wicker Sledge</option>
            <option value="26">Slide 27 • Day 7: Grand Farewell Seafood Feast</option>
            <option value="27">Slide 28 • Day 8: FNC Runway & Departure Flow</option>
            <option value="28">Slide 29 • Master Scorecard & Shared Financial Ledger</option>
            <option value="29">Slide 30 • Zero-Fail SOS Directory & Rescue Toolkit</option>
          </optgroup>
        </select>
      </div>
      
      <div class="nav-buttons">
        <button class="nav-btn" id="prevBtn" type="button" onclick="window.prevSlide && window.prevSlide()" title="Previous Slide (←)" aria-label="Previous Slide">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </button>
        <button class="nav-btn" id="nextBtn" type="button" onclick="window.nextSlide && window.nextSlide()" title="Next Slide (→ or Space)" aria-label="Next Slide">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>
      </div>
    </footer>
"""

def get_script():
    return """
  <!-- =======================================================================
       DECK JAVASCRIPT CONTROLLER & INTERACTIVE MAP
       ======================================================================= -->
  <script>
    (function() {
      const slides = Array.from(document.querySelectorAll('.slide'));
      const totalSlides = slides.length;
      let currentIndex = 0;

      const slideCounter = document.getElementById('slideCounter');
      const dotsContainer = document.getElementById('dotsContainer');
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const fullscreenBtn = document.getElementById('fullscreenBtn');
      const container = document.getElementById('presentationContainer');

      // High-performance, zero-delay touch & click tap binder for mobile and desktop
      function bindTap(el, handler) {
        if (!el) return;
        let lastActionTime = 0;
        let startX = 0;
        let startY = 0;
        let isPointerDown = false;

        function trigger(e) {
          const now = Date.now();
          if (now - lastActionTime < 320) return;
          lastActionTime = now;
          try {
            handler(e);
          } catch(err) {
            console.error('Error in tap handler:', err);
          }
        }

        el.addEventListener('pointerdown', function(e) {
          isPointerDown = true;
          startX = e.clientX;
          startY = e.clientY;
        }, { passive: true });

        el.addEventListener('pointerup', function(e) {
          if (!isPointerDown) return;
          isPointerDown = false;
          if (e.pointerType === 'touch' || e.pointerType === 'pen') {
            const diffX = Math.abs(e.clientX - startX);
            const diffY = Math.abs(e.clientY - startY);
            if (diffX < 24 && diffY < 24) {
              trigger(e);
            }
          }
        }, { passive: true });

        el.addEventListener('pointercancel', function() {
          isPointerDown = false;
        }, { passive: true });

        el.addEventListener('click', function(e) {
          trigger(e);
        });
      }

      // Build Progress Dots for all 30 slides
      if (dotsContainer) {
        for (let i = 0; i < totalSlides; i++) {
          const dot = document.createElement('div');
          dot.className = `dot ${i === 0 ? 'active' : ''}`;
          dot.title = `Slide ${i + 1}`;
          bindTap(dot, () => goToSlide(i));
          dotsContainer.appendChild(dot);
        }
      }
      const dots = dotsContainer ? Array.from(dotsContainer.children) : [];

      function updateSlide(index) {
        if (index < 0 || index >= totalSlides) return;
        
        slides[currentIndex].classList.remove('active');
        if (dots[currentIndex]) dots[currentIndex].classList.remove('active');
        
        currentIndex = index;
        
        slides[currentIndex].classList.add('active');
        if (dots[currentIndex]) dots[currentIndex].classList.add('active');
        
        // Update header counter format "SLIDE 01 / 30"
        const formattedCurrent = String(currentIndex + 1).padStart(2, '0');
        const formattedTotal = String(totalSlides).padStart(2, '0');
        if (slideCounter) {
          slideCounter.textContent = `SLIDE ${formattedCurrent} / ${formattedTotal}`;
        }

        const mobileSlideIndicator = document.getElementById('mobileSlideIndicator');
        if (mobileSlideIndicator) {
          mobileSlideIndicator.innerHTML = `
            <span style="color: var(--gold-primary); font-weight: 800;">SLIDE ${formattedCurrent}</span>
            <span style="opacity: 0.4;">/</span>
            <span style="opacity: 0.75;">${formattedTotal}</span>
            <span style="color: var(--gold-primary); margin-left: 2px;">▾</span>
          `;
        }

        // Synchronize built-in native mobile select components
        const topPicker = document.getElementById('nativeSlidePicker');
        if (topPicker) topPicker.value = String(currentIndex);
        const footerPicker = document.getElementById('footerSlidePicker');
        if (footerPicker) footerPicker.value = String(currentIndex);

        // Reset scroll position on current slide so user starts at the top
        slides[currentIndex].scrollTop = 0;
        
        try {
          history.replaceState(null, '', '#' + (currentIndex + 1));
        } catch(e) {}

        if (typeof syncDrawerActiveState === 'function') {
          syncDrawerActiveState();
        }
      }

      let lastSlideChangeTime = 0;
      function nextSlide() {
        const now = Date.now();
        if (now - lastSlideChangeTime < 260) return;
        lastSlideChangeTime = now;
        if (currentIndex < totalSlides - 1) {
          updateSlide(currentIndex + 1);
        } else {
          updateSlide(0); // Loop back
        }
      }

      function prevSlide() {
        const now = Date.now();
        if (now - lastSlideChangeTime < 260) return;
        lastSlideChangeTime = now;
        if (currentIndex > 0) {
          updateSlide(currentIndex - 1);
        } else {
          updateSlide(totalSlides - 1);
        }
      }

      function goToSlide(index) {
        updateSlide(index);
      }

      // Expose globally on window
      window.nextSlide = nextSlide;
      window.prevSlide = prevSlide;
      window.goToSlide = goToSlide;

      // Check URL hash on initial load
      const initialSlideFromHash = (function() {
        const hash = window.location.hash.replace('#', '');
        const num = parseInt(hash, 10);
        if (!isNaN(num) && num >= 1 && num <= totalSlides) {
          return num - 1;
        }
        return 0;
      })();
      if (initialSlideFromHash > 0) {
        updateSlide(initialSlideFromHash);
      }

      window.addEventListener('hashchange', () => {
        const hash = window.location.hash.replace('#', '');
        const num = parseInt(hash, 10);
        if (!isNaN(num) && num >= 1 && num <= totalSlides && num - 1 !== currentIndex) {
          updateSlide(num - 1);
        }
      });

      // Navigation button listeners
      if (nextBtn) {
        bindTap(nextBtn, nextSlide);
        nextBtn.addEventListener('click', (e) => { e.preventDefault(); nextSlide(); });
      }
      if (prevBtn) {
        bindTap(prevBtn, prevSlide);
        prevBtn.addEventListener('click', (e) => { e.preventDefault(); prevSlide(); });
      }
      const mobileSlideIndicatorBtn = document.getElementById('mobileSlideIndicator');
      if (mobileSlideIndicatorBtn) {
        bindTap(mobileSlideIndicatorBtn, () => {
          if (typeof window.openDrawer === 'function') window.openDrawer();
        });
      }

      // Keyboard navigation
      window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === ' ' || e.code === 'Space') {
          e.preventDefault();
          nextSlide();
        } else if (e.key === 'ArrowLeft') {
          e.preventDefault();
          prevSlide();
        } else if (e.key === 'Home') {
          e.preventDefault();
          goToSlide(0);
        } else if (e.key === 'End') {
          e.preventDefault();
          goToSlide(totalSlides - 1);
        } else if (e.key.toLowerCase() === 'f') {
          toggleFullscreen();
        }
      });

      // Touch / Swipe Navigation
      let touchStartX = 0;
      let touchEndX = 0;
      let touchStartY = 0;
      let touchEndY = 0;
      let isSwipeIgnored = false;

      function shouldIgnoreDeckSwipe(target) {
        if (!target || !(target instanceof Element)) return false;
        return !!target.closest(
          '#interactiveTrailSvg, .interactive-trail-box, .waypoint-selector, .stage-pill, .map-node, #inspectorContent, .transit-option-card, #transitDetailCard-5, button, a, input, select, textarea, [data-no-swipe], .no-swipe, #drawerOverlay, #drawerSheet, .drawer-list, .drawer-slide-item, #deckDrawerTrigger, .deck-header, .deck-footer, .nav-buttons'
        );
      }

      if (container) {
        container.addEventListener('touchstart', (e) => {
          if (shouldIgnoreDeckSwipe(e.target)) {
            isSwipeIgnored = true;
            return;
          }
          isSwipeIgnored = false;
          touchStartX = e.changedTouches[0].screenX;
          touchStartY = e.changedTouches[0].screenY;
        }, { passive: true });

        container.addEventListener('touchend', (e) => {
          if (isSwipeIgnored || shouldIgnoreDeckSwipe(e.target)) {
            isSwipeIgnored = false;
            return;
          }
          touchEndX = e.changedTouches[0].screenX;
          touchEndY = e.changedTouches[0].screenY;
          const diffX = touchEndX - touchStartX;
          const diffY = touchEndY - touchStartY;
          if (Math.abs(diffX) > 60 && Math.abs(diffX) > 1.8 * Math.abs(diffY)) {
            if (diffX < 0) nextSlide();
            else prevSlide();
          }
        }, { passive: true });
      }

      // Fullscreen Toggle
      function toggleFullscreen() {
        if (!document.fullscreenElement) {
          container.requestFullscreen().catch(err => console.warn(err));
          if (fullscreenBtn) fullscreenBtn.textContent = '✕ EXIT';
        } else {
          document.exitFullscreen();
          if (fullscreenBtn) fullscreenBtn.textContent = '⛶ EXPAND';
        }
      }
      if (fullscreenBtn) {
        bindTap(fullscreenBtn, toggleFullscreen);
        document.addEventListener('fullscreenchange', () => {
          if (!document.fullscreenElement) fullscreenBtn.textContent = '⛶ EXPAND';
          else fullscreenBtn.textContent = '✕ EXIT';
        });
      }

      // =====================================================================
      // INTERACTIVE ISLAND CARTOGRAPHY (SLIDE 3)
      // =====================================================================
      const stageData = [
        {
          id: 0,
          label: "Master Island Overview",
          title: "Madeira Alpine & Coastal Route (42.5 mi / 68.5 km)",
          desc: "High volcanic ridges above cloud seas, emerald levada gorges, ancient laurel mist forests, and volcanic lava basins across 4 distinct microclimates.",
          distance: "42.5 Miles (68.5 km) across 5 Premier PR Trails",
          elevation: "+11,320 ft (+3,450m) Cumulative Ascent",
          route: "Arieiro-Ruivo (PR1), Caldeirão Verde (PR9), 25 Fontes (PR6), São Lourenço (PR8)",
          lodging: "Clean, Quiet 3★/4★ Inns, Boutique Hotels & Historic Quintas",
          transfer: "Compact Turbo Rental Car • Full Island Expressway Network",
          alltrailsLink: "https://www.alltrails.com/portugal/madeira",
          gmapLink: "https://www.google.com/maps/dir/Funchal/Santana/Porto+Moniz/Funchal"
        },
        {
          id: 1,
          label: "PR8 • Eastern Peninsula",
          title: "Ponta de São Lourenço Dragon's Tail",
          desc: "4.5 miles (7.2 km) out-and-back trek across dramatic ochre sea cliffs plunging into crashing Atlantic surf. Zero trees, intense wind and sun exposure.",
          distance: "4.5 Miles (7.2 km) • 3.0 – 3.5 Hours Duration (08:30 Start)",
          elevation: "+1,050 ft (+320m) Ascent / -1,050 ft (-320m)",
          route: "Volcanic Basalt Ridges & Stairway to Ponta do Furado",
          lodging: "White Waters Hotel (Machico Bay)",
          transfer: "Lunch: Caniçal Harbor Lapas & Prainha Volcanic Beach",
          alltrailsLink: "https://www.alltrails.com/trail/portugal/madeira/pr8-vereda-da-ponta-de-sao-lourenco",
          gmapLink: "https://www.google.com/maps/dir/Machico/Ponta+de+São+Lourenço"
        },
        {
          id: 2,
          label: "PR1 • High Central Massif",
          title: "Pico do Arieiro to Pico Ruivo One-Way Ridge Traverse",
          desc: "The Atlantic's master alpine trek (strictly one-way by IFCN rule). Carved cliff tunnels, razor ridges, and dizzying vertical staircases above a sea of clouds.",
          distance: "6.2 Miles (10.0 km) One-Way to Achada do Teixeira • 4.5 – 5.5 Hours",
          elevation: "+2,450 ft (+750m) Ascent / -3,100 ft (-950m) Descent",
          route: "Ninho da Manta, Pedra Rija, Basalt Tunnels, Ruivo Summit (6,109 ft), PR1.2 Descent",
          lodging: "Quinta do Furão (Santana Cliff Vineyard Estate)",
          transfer: "Reverse-Parking Hack: Leave car at Teixeira, shuttle to Arieiro for sunrise",
          alltrailsLink: "https://www.alltrails.com/trail/portugal/madeira/pr1-vereda-do-areeiro-pico-ruivo",
          gmapLink: "https://www.google.com/maps/dir/Pico+do+Arieiro/Pico+Ruivo"
        },
        {
          id: 3,
          label: "PR9 • Laurissilva Rainforest",
          title: "Levada do Caldeirão Verde (Green Cauldron)",
          desc: "7.5 miles (12.0 km) round-trip flat levada hike deep into the UNESCO Laurissilva rainforest, passing 4 unlit rock tunnels to a roaring 330-ft waterfall amphitheater.",
          distance: "7.5 Miles (12.0 km) Round Trip • 3.5 – 4.0 Hours",
          elevation: "+330 ft (+100m) Gradual Aqueduct Grade",
          route: "Queimadas Forest House, 4 Basalt Tunnels, Emerald Cauldron",
          lodging: "Quinta do Furão or Hotel Santana",
          transfer: "Lunch: Santana Thatched Palheiros & Mountain Soup",
          alltrailsLink: "https://www.alltrails.com/trail/portugal/madeira/pr9-levada-do-caldeirao-verde",
          gmapLink: "https://www.google.com/maps/dir/Santana/Parque+Florestal+das+Queimadas"
        },
        {
          id: 4,
          label: "UNESCO Laurissilva • Fanal",
          title: "Fanal 500-Year-Old Ancient Mist Forest",
          desc: "Grotesque, twisted 500-year-old Til trees draped in thick moss and mountain mist on the high volcanic plateau. Eerie, silent, and magical at 3,770 ft elevation.",
          distance: "2.5 – 5.0 Miles (4–8 km) Exploration Stroll",
          elevation: "+820 ft (+250m) • 3,770 ft (1,150m) Plateau Elevation",
          route: "Ancient Til Grove, Volcanic Crater & Levada dos Cedros",
          lodging: "Aqua Natura Bay (Porto Moniz Waterfront)",
          transfer: "Live Netcam Check: Only head up when plateau has active cloud mist!",
          alltrailsLink: "https://www.alltrails.com/trail/portugal/madeira/fanal-vereda-do-fanal",
          gmapLink: "https://www.google.com/maps/dir/São+Vicente/Fanal"
        },
        {
          id: 5,
          label: "Northwest Coast Havens",
          title: "Porto Moniz Volcanic Pools & Seixal Black Sand",
          desc: "Natural Atlantic seawater pools formed in jagged basalt lava fields, paired with Seixal's emerald cliffside black sand beach, waterfalls, and Poça das Lesmas lava arch.",
          distance: "Coastal Swimming & Village Stroll",
          elevation: "Sea Level Atlantic Basins",
          route: "Porto Moniz Pools (€3), Poça das Lesmas Lava Arch & Seixal Beach",
          lodging: "Aqua Natura Bay / Hotel Euro Moniz",
          transfer: "Seaside Dinner: Fresh Grilled Amberjack & Passion Fruit",
          alltrailsLink: "https://www.alltrails.com/portugal/madeira/porto-moniz",
          gmapLink: "https://www.google.com/maps/dir/Porto+Moniz/Seixal"
        },
        {
          id: 6,
          label: "PR6 • Rabaçal Valley",
          title: "25 Fontes Waterfall & Risco Cascades",
          desc: "6.2 miles (10.0 km) circuit descending into the deep Rabaçal valley, tracing ancient stone levadas to the weeping spring basin and a 330-ft two-tiered waterfall.",
          distance: "6.2 Miles (10.0 km) Loop • 3.5 – 4.0 Hours (08:00 AM Start)",
          elevation: "+1,150 ft (+350m) Valley Descent & Climb",
          route: "Casa do Rabaçal, Levada do Risco, 25 Weeping Springs",
          lodging: "Return to Funchal (Hotel Porto Santa Maria)",
          transfer: "Paúl da Serra Plateau Scenic Highway ER110",
          alltrailsLink: "https://www.alltrails.com/trail/portugal/madeira/pr6-levada-das-25-fontes-e-levada-do-risco",
          gmapLink: "https://www.google.com/maps/dir/Rabaçal/Funchal"
        },
        {
          id: 7,
          label: "South Coast Transit & Viewpoints",
          title: "Achadas da Cruz Cable Car & Cabo Girão Skywalk",
          desc: "Riding an 84-degree vertical cliffside cable car down 1,480 ft to an isolated coastal shelf, then walking 1,932 ft over the sea on a glass skywalk.",
          distance: "Coastal Transit & Viewpoint Strolls",
          elevation: "1,480 ft (451m) Cable Drop / 1,932 ft (589m) Skywalk",
          route: "Teleférico das Achadas da Cruz & Cabo Girão Skywalk",
          lodging: "Hotel Porto Santa Maria (Central Funchal Base)",
          transfer: "VR1 South Coast Expressway • Sunset in Funchal Harbor",
          alltrailsLink: "https://www.alltrails.com/trail/portugal/madeira/teleferico-das-achadas-da-cruz",
          gmapLink: "https://www.google.com/maps/dir/Achadas+da+Cruz/Cabo+Girão/Funchal"
        }
      ];

      window.selectMapStage = function(idx) {
        const data = stageData[idx] || stageData[0];
        
        // Update pills
        const pills = document.querySelectorAll('.stage-pill');
        pills.forEach((p, i) => {
          if (i === idx) {
            p.classList.add('active');
            try { p.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' }); } catch (err) {}
          } else {
            p.classList.remove('active');
          }
        });

        // Highlight corresponding map node in SVG
        const nodes = document.querySelectorAll('.map-node');
        nodes.forEach((node) => {
          const stageAttr = parseInt(node.getAttribute('data-stage'), 10);
          if (stageAttr === idx) {
            node.classList.add('active');
          } else {
            node.classList.remove('active');
          }
        });

        const container = document.getElementById('inspectorContent');
        if (!container) return;

        container.innerHTML = `
          <div class="card-label">${data.label}</div>
          <h3 class="card-heading" style="margin-bottom:0.4rem;">${data.title}</h3>
          <p class="card-body" style="font-size: 1.02rem; margin-bottom: 0.8rem;">
            ${data.desc}
          </p>

          <div style="margin-top: 0.8rem; display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.88rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 5px;">
              <span style="color: var(--gold-glow);">Distance & Pace:</span>
              <strong>${data.distance}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.88rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 5px;">
              <span style="color: var(--teal-ocean);">Elevation Profile:</span>
              <strong>${data.elevation}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.88rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 5px;">
              <span style="color: var(--terracotta);">Terrain / Route:</span>
              <strong>${data.route}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.88rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 5px;">
              <span style="color: var(--sand-muted);">Overnight Retreat:</span>
              <strong>${data.lodging}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.88rem;">
              <span style="color: var(--sand-muted);">Gastronomy / Evening:</span>
              <strong style="color: var(--gold-primary);">${data.transfer}</strong>
            </div>
          </div>

          <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
            <a href="${data.alltrailsLink}" target="_blank" rel="noopener noreferrer" class="alltrails-stage-link" style="padding: 6px 10px; font-size: 0.76rem; justify-content: center;">
              <span>🌲 AllTrails Topo & GPS</span> ↗
            </a>
            <a href="${data.gmapLink}" target="_blank" rel="noopener noreferrer" class="gmaps-stage-link" style="padding: 6px 10px; font-size: 0.76rem; justify-content: center; margin-top: 0;">
              <span>📍 Route / Map Directions</span> ↗
            </a>
          </div>
        `;
      };

      // Initialize map inspector on page load
      window.selectMapStage(0);

      // =====================================================================
      // TRANSIT ROUTE OPTIONS SWITCHER (SLIDE 5: ISLAND DRIVING)
      // =====================================================================
      const transitData = {
        5: [
          {
            label: "Primary Ground Selection",
            title: "Compact Turbo Petrol Hatchback",
            tagText: "RECOMMENDED",
            tagClass: "tag-gold",
            boxes: [
              { name: "Weekly Rental + Full CDW", price: "€210 – €260", sub: "Total 7 days for 2 travelers", color: "var(--gold-glow)" },
              { name: "Mountain Fuel & Parking", price: "~€60 – €75", sub: "Full week unleaded petrol", color: "var(--teal-ocean)" }
            ],
            highlights: [
              "<strong>Low-End Climbing Torque:</strong> Modern 1.0L or 1.2L turbocharged engines deliver peak torque at 1,500 RPM, effortlessly ascending Madeira's 20%–25% village switchbacks without stalling.",
              "<strong>Compact Footprint:</strong> Ideal dimensions for navigating narrow historic streets in Funchal Old Town, tight mountain tunnels, and compact trailhead parking spaces.",
              "<strong>Comprehensive Zero-Excess CDW:</strong> Essential on Madeira to protect against minor gravel chips on mountain roads and tight parking scuffs.",
              "<strong>Full Flexibility:</strong> Allows spontaneous sunrise departures at 06:15 AM to Pico do Arieiro and late-night returns from coastal restaurants."
            ],
            duration: "TOTAL INDEPENDENCE",
            effort: "LOW (EASY DRIVE)",
            effortColor: "var(--gold-primary)"
          },
          {
            label: "Comfort Selection",
            title: "Compact Automatic Crossover",
            tagText: "MAX COMFORT",
            tagClass: "tag-teal",
            boxes: [
              { name: "Weekly Rental + Full CDW", price: "€280 – €340", sub: "Automatic transmission", color: "var(--teal-ocean)" },
              { name: "Mountain Fuel", price: "~€75 – €90", sub: "Higher clearance vehicle", color: "var(--gold-glow)" }
            ],
            highlights: [
              "<strong>Hill-Start Assist:</strong> Automatic transmission completely eliminates clutch slip and rollback anxiety on 25% steep village inclines and stoplights.",
              "<strong>Higher Ride Height:</strong> Improved visibility and ground clearance when pulling over on unpaved trailhead verges and rural mountain lookouts.",
              "<strong>Generous Trunk Space:</strong> Accommodates 2 large suitcases and technical hiking packs out of sight in the trunk.",
              "<strong>Relaxed Navigation:</strong> Less driving fatigue after 6 hours on mountain trails."
            ],
            duration: "TOTAL INDEPENDENCE",
            effort: "VERY LOW (ZERO ROLLBACK)",
            effortColor: "var(--teal-ocean)"
          },
          {
            label: "Budget Warning",
            title: "Naturally Aspirated 1.0L Non-Turbo",
            tagText: "FATAL FLAW",
            tagClass: "tag-terracotta",
            boxes: [
              { name: "Apparent Base Rental", price: "€140 – €180", sub: "Cheap advertised rate", color: "var(--terracotta)" },
              { name: "Clutch Wear Risk", price: "HIGH", sub: "Engine screams on 20% grades", color: "var(--terracotta)" }
            ],
            highlights: [
              "<strong>Severe Torque Deficit:</strong> Non-turbo engines produce under 95 Nm of torque at high RPMs. With two adults, luggage, and air conditioning, the car struggles to climb 20%+ switchbacks.",
              "<strong>Forced 1st-Gear Driving:</strong> Drivers are forced to drop into 1st gear on standard village ascents, leading to engine overheating and clutch burnout.",
              "<strong>Stressful Mountain Transit:</strong> Nerve-wracking hill starts on blind corners and steep descents.",
              "<strong>Verdict:</strong> Avoid at all costs. Pay the modest €30–€50 upgrade for a turbo or automatic."
            ],
            duration: "HIGH STRESS",
            effort: "UNRECOMMENDED",
            effortColor: "var(--terracotta)"
          },
          {
            label: "Public Transport Alternative",
            title: "Public Coaches & Minivan Shuttles",
            tagText: "BUDGET / RIGID",
            tagClass: "tag-gold",
            boxes: [
              { name: "Bus / Shuttle Passes", price: "€70 – €110", sub: "Combined for 2 passengers", color: "var(--gold-glow)" },
              { name: "Taxi Add-ons", price: "€80 – €120", sub: "Required for sunrise trips", color: "var(--sand-light)" }
            ],
            highlights: [
              "<strong>Rigid Timetables:</strong> Regional buses (SAM, Rodoeste, Horários do Funchal) connect coastal towns reliably, but mountain routes are sparse (often 1–2 per day).",
              "<strong>Zero Sunrise Access:</strong> No public buses reach Pico do Arieiro for 07:15 AM sunrise. Requires booking third-party van transfers (e.g., Pico Transfers, ~€35/person).",
              "<strong>Luggage Constraints:</strong> Hauling bags between hotels on public transit limits multi-destination lodging agility.",
              "<strong>Verdict:</strong> Viable only for travelers unwilling to drive mountain roads."
            ],
            duration: "RESTRICTED HOURS",
            effort: "MEDIUM (SCHEDULE CONSTRAINTS)",
            effortColor: "var(--sand-muted)"
          }
        ]
      };

      window.switchTransitOption = function(slideNum, optIdx) {
        const cards = document.querySelectorAll(`[data-slide="${slideNum}"] .transit-option-card`);
        cards.forEach(c => {
          if (parseInt(c.getAttribute('data-opt'), 10) === optIdx) {
            c.classList.add('active');
          } else {
            c.classList.remove('active');
          }
        });

        const data = transitData[slideNum] && transitData[slideNum][optIdx];
        const container = document.getElementById(`transitDetailCard-${slideNum}`);
        if (!data || !container) return;

        container.style.opacity = '0.35';
        setTimeout(() => {
          container.innerHTML = `
            <div>
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.8rem;">
                <div>
                  <div class="card-label">${data.label}</div>
                  <h3 class="card-heading" style="margin-bottom: 0.2rem;">${data.title}</h3>
                </div>
                <div class="tag ${data.tagClass}" style="font-size: 0.75rem;">${data.tagText}</div>
              </div>

              <!-- Pricing Callout Boxes -->
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 1rem;">
                <div class="stat-box" style="padding: 10px 14px; text-align: left;">
                  <div style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--sand-muted); text-transform: uppercase;">${data.boxes[0].name}</div>
                  <div style="font-size: 1.45rem; font-weight: 700; color: ${data.boxes[0].color}; font-family: var(--font-serif); margin-top: 2px;">${data.boxes[0].price}</div>
                  <div style="font-size: 0.75rem; color: var(--sand-muted);">${data.boxes[0].sub}</div>
                </div>
                <div class="stat-box" style="padding: 10px 14px; text-align: left;">
                  <div style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--sand-muted); text-transform: uppercase;">${data.boxes[1].name}</div>
                  <div style="font-size: 1.45rem; font-weight: 700; color: ${data.boxes[1].color}; font-family: var(--font-serif); margin-top: 2px;">${data.boxes[1].price}</div>
                  <div style="font-size: 0.75rem; color: var(--sand-muted);">${data.boxes[1].sub}</div>
                </div>
              </div>

              <ul class="highlight-list" style="margin-top: 0.4rem;">
                ${data.highlights.map(h => `<li>${h}</li>`).join('')}
              </ul>
            </div>

            <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid var(--border-subtle); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--sand-muted);">DURATION: ${data.duration}</span>
              <span style="font-family: var(--font-mono); font-size: 0.8rem; color: ${data.effortColor}; font-weight: 700;">EFFORT: ${data.effort}</span>
            </div>
          `;
          container.style.opacity = '1';
        }, 120);
      };

      // Initialize Slide 5 transit option on page load
      window.switchTransitOption(5, 0);

      // =====================================================================
      // THEME PALETTE CONTROLLER
      // =====================================================================
      const themes = [
        { id: "linen", name: "Porcelain & Slate" },
        { id: "coastal", name: "Atlantic Navy" },
        { id: "obsidian", name: "Obsidian & Gold" }
      ];
      let currentThemeIdx = 0;
      const themeBtn = document.getElementById('themeBtn');

      function applyTheme(idx) {
        currentThemeIdx = idx % themes.length;
        const selected = themes[currentThemeIdx];
        document.documentElement.setAttribute('data-theme', selected.id);
        if (themeBtn) {
          themeBtn.textContent = `🎨 PALETTE: ${selected.name}`;
        }
        try { localStorage.setItem('deck-theme', selected.id); } catch(e) {}
      }

      const savedTheme = (function() {
        try { return localStorage.getItem('deck-theme') || 'linen'; } catch(e) { return 'linen'; }
      })();
      const initialIdx = themes.findIndex(t => t.id === savedTheme);
      applyTheme(initialIdx >= 0 ? initialIdx : 0);

      if (themeBtn) {
        bindTap(themeBtn, () => {
          applyTheme(currentThemeIdx + 1);
        });
      }

      // =====================================================================
      // SLIDE NAVIGATION DRAWER & PAGE SELECTION SHEET
      // =====================================================================
      const deckDrawerTrigger = document.getElementById('deckDrawerTrigger');
      const drawerOverlay = document.getElementById('drawerOverlay');
      const drawerBackdrop = document.getElementById('drawerBackdrop');
      const drawerSheet = document.getElementById('drawerSheet');
      const drawerCloseBtn = document.getElementById('drawerCloseBtn');
      const drawerSearchInput = document.getElementById('drawerSearchInput');
      const drawerSearchClear = document.getElementById('drawerSearchClear');
      const drawerFilterPills = document.getElementById('drawerFilterPills');
      const drawerList = document.getElementById('drawerList');

      // Classification taxonomy for all 30 slides
      const slideMetaMap = {
        1: { cat: ['all', 'overview'], primaryCat: 'overview', tag: 'COVER' },
        2: { cat: ['all', 'overview'], primaryCat: 'overview', tag: 'TOPOGRAPHY' },
        3: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'CARTOGRAPHY' },
        4: { cat: ['all', 'overview'], primaryCat: 'overview', tag: 'METEOROLOGY' },
        5: { cat: ['all', 'transit'], primaryCat: 'transit', tag: 'DRIVING' },
        6: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'LEVADA SAFETY' },
        7: { cat: ['all', 'overview'], primaryCat: 'overview', tag: 'GEAR KIT' },
        8: { cat: ['all', 'transit'], primaryCat: 'transit', tag: 'ARRIVAL FNC' },
        9: { cat: ['all', 'retreat'], primaryCat: 'retreat', tag: 'LODGING' },
        10: { cat: ['all', 'dining'], primaryCat: 'dining', tag: 'ESPETADA' },
        11: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'PR8 CLIFTS' },
        12: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'CANIÇAL' },
        13: { cat: ['all', 'retreat', 'dining'], primaryCat: 'retreat', tag: 'EAST RETREAT' },
        14: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'PR1 RIDGE' },
        15: { cat: ['all', 'transit'], primaryCat: 'transit', tag: 'SUNRISE LOGISTICS' },
        16: { cat: ['all', 'retreat'], primaryCat: 'retreat', tag: 'QUINTA' },
        17: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'PR9 CANYON' },
        18: { cat: ['all', 'overview', 'dining'], primaryCat: 'dining', tag: 'SANTANA' },
        19: { cat: ['all', 'retreat'], primaryCat: 'retreat', tag: 'NORTH COAST' },
        20: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'FANAL FOREST' },
        21: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'LAVA POOLS' },
        22: { cat: ['all', 'retreat'], primaryCat: 'retreat', tag: 'PORTO MONIZ' },
        23: { cat: ['all', 'trail'], primaryCat: 'trail', tag: 'PR6 LEVADA' },
        24: { cat: ['all', 'transit', 'trail'], primaryCat: 'transit', tag: 'CABLE CAR' },
        25: { cat: ['all', 'retreat'], primaryCat: 'retreat', tag: 'FUNCHAL BASE' },
        26: { cat: ['all', 'overview'], primaryCat: 'overview', tag: 'MONTE PALACE' },
        27: { cat: ['all', 'dining'], primaryCat: 'dining', tag: 'FAREWELL DINE' },
        28: { cat: ['all', 'transit'], primaryCat: 'transit', tag: 'FNC RUNWAY' },
        29: { cat: ['all', 'overview'], primaryCat: 'overview', tag: 'MASTER LEDGER' },
        30: { cat: ['all', 'overview'], primaryCat: 'overview', tag: 'SOS DIRECTORY' }
      };

      const slideDirectoryData = slides.map((slideEl, index) => {
        const slideNum = index + 1;
        const eyebrowEl = slideEl.querySelector('.slide-eyebrow');
        const titleEl = slideEl.querySelector('.slide-title');
        const subtitleEl = slideEl.querySelector('.slide-subtitle');

        const eyebrow = eyebrowEl ? eyebrowEl.textContent.trim().replace(/\\s+/g, ' ') : `Milestone ${slideNum}`;
        const title = titleEl ? titleEl.textContent.trim().replace(/\\s+/g, ' ') : `Slide ${slideNum}`;
        const subtitle = subtitleEl ? subtitleEl.textContent.trim().replace(/\\s+/g, ' ') : '';

        const meta = slideMetaMap[slideNum] || { cat: ['all'], primaryCat: 'overview', tag: `SLIDE ${slideNum}` };

        return {
          index,
          num: slideNum,
          formattedNum: String(slideNum).padStart(2, '0'),
          eyebrow,
          title,
          subtitle,
          categories: meta.cat,
          primaryCat: meta.primaryCat,
          tag: meta.tag
        };
      });

      let currentDrawerFilter = 'all';
      let currentDrawerSearch = '';
      let isDrawerOpen = false;

      function renderDrawerItems() {
        if (!drawerList) return;

        const term = currentDrawerSearch.toLowerCase().trim();
        const filtered = slideDirectoryData.filter(item => {
          if (currentDrawerFilter !== 'all' && !item.categories.includes(currentDrawerFilter)) {
            return false;
          }
          if (term) {
            const numStr = String(item.num);
            const formattedStr = item.formattedNum;
            const titleMatch = item.title.toLowerCase().includes(term);
            const eyebrowMatch = item.eyebrow.toLowerCase().includes(term);
            const subtitleMatch = item.subtitle.toLowerCase().includes(term);
            const tagMatch = item.tag.toLowerCase().includes(term);
            const numMatch = numStr === term || formattedStr === term || `slide ${numStr}`.includes(term) || `page ${numStr}`.includes(term);
            if (!titleMatch && !eyebrowMatch && !subtitleMatch && !tagMatch && !numMatch) {
              return false;
            }
          }
          return true;
        });

        if (filtered.length === 0) {
          drawerList.innerHTML = `
            <div style="padding: 2.5rem 1rem; text-align: center; color: var(--sand-muted);">
              <div style="font-size: 2rem; margin-bottom: 0.5rem; opacity: 0.7;">🔍</div>
              <div style="font-family: var(--font-serif); font-size: 1.15rem; color: var(--text-title); margin-bottom: 0.35rem;">No Milestones Found</div>
              <div style="font-size: 0.82rem; font-family: var(--font-sans);">No slides match "${currentDrawerSearch}". Try searching by page number, trail, or village.</div>
            </div>
          `;
          return;
        }

        drawerList.innerHTML = filtered.map(item => {
          const isActive = item.index === currentIndex;
          return `
            <div class="drawer-slide-item ${isActive ? 'active' : ''}" data-index="${item.index}" role="button" tabindex="0" aria-label="Jump to Slide ${item.num}: ${item.title}">
              <div class="drawer-slide-num">${item.formattedNum}</div>
              <div class="drawer-slide-content">
                <div class="drawer-slide-meta">
                  <span class="drawer-slide-tag" data-cat="${item.primaryCat}">${item.tag}</span>
                  ${isActive ? '<span class="drawer-slide-current-badge">● CURRENT</span>' : ''}
                </div>
                <div class="drawer-slide-title">${item.title}</div>
                ${item.subtitle ? `<div class="drawer-slide-desc">${item.subtitle}</div>` : ''}
              </div>
              <div class="drawer-slide-arrow" aria-hidden="true">→</div>
            </div>
          `;
        }).join('');
      }

      function syncDrawerActiveState(shouldScroll = false) {
        if (!drawerList) return;
        const items = drawerList.querySelectorAll('.drawer-slide-item');
        items.forEach(el => {
          const idx = parseInt(el.getAttribute('data-index'), 10);
          const isActive = idx === currentIndex;
          el.classList.toggle('active', isActive);
          const metaEl = el.querySelector('.drawer-slide-meta');
          let currentBadge = el.querySelector('.drawer-slide-current-badge');
          if (isActive) {
            if (!currentBadge && metaEl) {
              const badge = document.createElement('span');
              badge.className = 'drawer-slide-current-badge';
              badge.textContent = '● CURRENT';
              metaEl.appendChild(badge);
            }
          } else if (currentBadge) {
            currentBadge.remove();
          }
        });

        if (shouldScroll && isDrawerOpen) {
          const activeEl = drawerList.querySelector('.drawer-slide-item.active');
          if (activeEl) {
            activeEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
          }
        }
      }

      let drawerOpenedAt = 0;
      function openDrawer() {
        if (!drawerOverlay) return;
        isDrawerOpen = true;
        drawerOpenedAt = Date.now();
        drawerOverlay.classList.add('active');
        drawerOverlay.setAttribute('aria-hidden', 'false');
        renderDrawerItems();
        setTimeout(() => { syncDrawerActiveState(true); }, 100);
      }

      function closeDrawer(force = false) {
        if (!drawerOverlay || !isDrawerOpen) return;
        if (!force && (Date.now() - drawerOpenedAt < 400)) return;
        isDrawerOpen = false;
        drawerOverlay.classList.remove('active');
        drawerOverlay.setAttribute('aria-hidden', 'true');
        if (drawerSearchInput) drawerSearchInput.blur();
      }

      function toggleDrawer() {
        if (isDrawerOpen) closeDrawer(true);
        else openDrawer();
      }

      window.openDrawer = openDrawer;
      window.closeDrawer = closeDrawer;
      window.toggleDrawer = toggleDrawer;

      if (deckDrawerTrigger) bindTap(deckDrawerTrigger, openDrawer);
      if (drawerCloseBtn) bindTap(drawerCloseBtn, () => closeDrawer(true));
      if (drawerBackdrop) bindTap(drawerBackdrop, () => closeDrawer(false));

      if (drawerList) {
        let listTouchStartY = 0;
        let listTouchMoved = false;

        drawerList.addEventListener('touchstart', (e) => {
          listTouchMoved = false;
          listTouchStartY = e.touches[0].clientY;
        }, { passive: true });

        drawerList.addEventListener('touchmove', (e) => {
          if (Math.abs(e.touches[0].clientY - listTouchStartY) > 8) {
            listTouchMoved = true;
          }
        }, { passive: true });

        drawerList.addEventListener('touchend', (e) => {
          if (!listTouchMoved) {
            const item = e.target.closest('.drawer-slide-item');
            if (item) {
              const idx = parseInt(item.getAttribute('data-index'), 10);
              if (!isNaN(idx)) {
                e.preventDefault();
                goToSlide(idx);
                closeDrawer(true);
              }
            }
          }
        }, { passive: false });

        drawerList.addEventListener('click', (e) => {
          const item = e.target.closest('.drawer-slide-item');
          if (item) {
            const idx = parseInt(item.getAttribute('data-index'), 10);
            if (!isNaN(idx)) {
              goToSlide(idx);
              closeDrawer(true);
            }
          }
        });
      }

      if (drawerSearchInput) {
        drawerSearchInput.addEventListener('input', (e) => {
          currentDrawerSearch = e.target.value;
          if (drawerSearchClear) {
            drawerSearchClear.style.display = currentDrawerSearch ? 'block' : 'none';
          }
          renderDrawerItems();
        });
      }

      if (drawerSearchClear) {
        bindTap(drawerSearchClear, () => {
          currentDrawerSearch = '';
          if (drawerSearchInput) {
            drawerSearchInput.value = '';
            drawerSearchInput.focus();
          }
          drawerSearchClear.style.display = 'none';
          renderDrawerItems();
        });
      }

      if (drawerFilterPills) {
        bindTap(drawerFilterPills, (e) => {
          const pill = e.target.closest('.drawer-filter-pill');
          if (!pill) return;
          const filter = pill.getAttribute('data-filter') || 'all';
          currentDrawerFilter = filter;
          drawerFilterPills.querySelectorAll('.drawer-filter-pill').forEach(btn => {
            btn.classList.toggle('active', btn === pill);
          });
          renderDrawerItems();
        });
      }

      window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && isDrawerOpen) {
          closeDrawer(true);
        }
      });

      renderDrawerItems();

    })();
  </script>
</body>
</html>
"""

if __name__ == '__main__':
    hdr = get_header_and_drawer()
    ftr = get_footer()
    sc = get_script()
    print("Nav and scripts updated with American units.")
