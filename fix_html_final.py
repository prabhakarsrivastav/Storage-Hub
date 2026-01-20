
import os
import html

file_path = "index.html"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Check against common anchor
anchor = 'class="products-section all-segments-section"'
if anchor in content:
    # Find the end of this section
    # This is rough, counting section tags might be better, or just finding the next major tag.
    # But since I know the structure, let's look for "Trending Pendrive"
    
    idx = content.find(anchor)
    # Find the closing </section> of all-segments
    # Since there are nested divs, we search for </section> after the anchor.
    # The all-segments section is simple.
    end_section_idx = content.find('</section>', idx)
    
    if end_section_idx != -1:
        # We keep everything up to and including </section> of all-segments
        # BUT wait, the combined wrapper might be involved.
        # "combined-smoke-section" wraps trending-ram and all-segments.
        # So it should be all-segments </section> -> wrapper </div>.
        
        # Let's verify if combined-wrapper exists
        has_wrapper = 'class="combined-smoke-section"' in content
        
        cut_point = end_section_idx + 10 # len(</section>)
        
        # If wrapper, we look for </div> after </section>
        if has_wrapper:
             wrapper_close = content.find('</div>', cut_point)
             if wrapper_close != -1:
                 cut_point = wrapper_close + 6
        
        # Now we construct the new end of file
        # We will hardcode the Pendrive Section HTML we want
        pendrive_html = """
    <!-- Trending Pendrive Section -->
    <section class="products-section trending-pendrive-section">
        <div class="container">
            <div class="section-header">
                <div class="section-title">
                    <span class="title-dot red-dot"></span>
                    <h2>Trending Pendrive</h2>
                </div>
                <div class="section-filters" style="margin-left: auto; gap: 40px;">
                    <button class="filter-btn active">Show All</button>
                    <button class="filter-btn">All Brands</button>
                    <button class="filter-btn">All Offers</button>
                </div>
            </div>

            <div class="pendrive-carousel-container">
                <button class="carousel-nav prev-nav">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M15 18L9 12L15 6" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>

                <div class="pendrive-grid-wrapper">
                    <!-- Card 1 -->
                    <div class="pendrive-card">
                        <div class="pd-top">
                            <span class="shop-badge">SHOP</span>
                            <div class="pd-image">
                                <img src="assets/images/pendrive-kingston.png" alt="Kingston Pendrive">
                            </div>
                        </div>
                        <div class="pd-bottom">
                            <h3 class="pd-title">Lorem Ipsum Dolor Sit Amet, Consectetur</h3>
                            <div class="pd-actions">
                                <div class="pd-price">₹ 3,850</div>
                                <div class="pd-icons">
                                    <button class="pd-icon-btn">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                                        </svg>
                                    </button>
                                    <button class="pd-icon-btn">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <polyline points="1 4 1 10 7 10"></polyline>
                                            <polyline points="23 20 23 14 17 14"></polyline>
                                            <path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="active-bar"></div>
                    </div>

                    <!-- Card 2 -->
                    <div class="pendrive-card">
                        <div class="pd-top">
                            <span class="shop-badge">SHOP</span>
                            <div class="pd-image">
                                <img src="assets/images/pendrive-kingston.png" alt="Kingston Pendrive" style="filter: hue-rotate(180deg);">
                            </div>
                        </div>
                        <div class="pd-bottom">
                            <h3 class="pd-title">Lorem Ipsum Dolor Sit Amet, Consectetur</h3>
                            <div class="pd-actions">
                                <div class="pd-price">₹ 3,850</div>
                                <div class="pd-icons">
                                    <button class="pd-icon-btn">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                                        </svg>
                                    </button>
                                    <button class="pd-icon-btn">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <polyline points="1 4 1 10 7 10"></polyline>
                                            <polyline points="23 20 23 14 17 14"></polyline>
                                            <path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="active-bar"></div>
                    </div>

                    <!-- Card 3 -->
                    <div class="pendrive-card">
                        <div class="pd-top">
                            <span class="shop-badge">SHOP</span>
                            <div class="pd-image">
                                <img src="assets/images/pendrive-sandisk.png" alt="Sandisk Pendrive">
                            </div>
                        </div>
                        <div class="pd-bottom">
                            <h3 class="pd-title">Lorem Ipsum Dolor Sit Amet, Consectetur</h3>
                            <div class="pd-actions">
                                <div class="pd-price">₹ 3,850</div>
                                <div class="pd-icons">
                                    <button class="pd-icon-btn">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                                        </svg>
                                    </button>
                                    <button class="pd-icon-btn">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <polyline points="1 4 1 10 7 10"></polyline>
                                            <polyline points="23 20 23 14 17 14"></polyline>
                                            <path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="active-bar"></div>
                    </div>
                     <!-- Card 4 -->
                    <div class="pendrive-card">
                        <div class="pd-top">
                            <span class="shop-badge">SHOP</span>
                            <div class="pd-image">
                                <img src="assets/images/pendrive-kingston.png" alt="Kingston Pendrive" style="filter: hue-rotate(90deg);">
                            </div>
                        </div>
                        <div class="pd-bottom">
                            <h3 class="pd-title">Lorem Ipsum Dolor Sit Amet, Consectetur</h3>
                            <div class="pd-actions">
                                <div class="pd-price">₹ 3,850</div>
                                <div class="pd-icons">
                                    <button class="pd-icon-btn">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                                        </svg>
                                    </button>
                                    <button class="pd-icon-btn">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <polyline points="1 4 1 10 7 10"></polyline>
                                            <polyline points="23 20 23 14 17 14"></polyline>
                                            <path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="active-bar"></div>
                    </div>
                </div>

                <button class="carousel-nav next-nav">
                     <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 18L15 12L9 6" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </div>
            
            <div class="section-footer">
                <a href="#" class="more-link">More</a>
            </div>
        </div>
    </section>

    <script src="script.js"></script>
</body>
</html>
"""
        new_content = content[:cut_point] + "\n" + pendrive_html
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print("Replaced content successfully.")
    else:
        print("Could not find end of all segments section")
else:
    print("Could not find all segments section")
