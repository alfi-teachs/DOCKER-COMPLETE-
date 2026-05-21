# style.css

```bash

body {
  font-family: 'Poppins', sans-serif;
  color: #000000;
  background-color: #ffffff;
}

.layout_padding {
  padding-top: 120px;
  padding-bottom: 120px;
}

.layout_padding2 {
  padding-top: 45px;
  padding-bottom: 45px;
}

.layout_padding2-top {
  padding-top: 45px;
}

.layout_padding2-bottom {
  padding-bottom: 45px;
}

.layout_padding-top {
  padding-top: 120px;
}

.layout_padding-bottom {
  padding-bottom: 120px;
}

.heading_container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  text-align: center;
}

.heading_container h2 {
  font-weight: bold;
  position: relative;
  padding-bottom: 5px;
  text-transform: uppercase;
}

.heading_container h2::before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 55px;
  height: 5px;
  background-color: #ff2953;
  -webkit-transform: translateX(-50%);
          transform: translateX(-50%);
}

/*header section*/
.hero_area {
  height: 100vh;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  background-image: url(../images/hero-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
}

.sub_page .hero_area {
  height: auto;
}

.sub_page .who_section.layout_padding {
  padding-top: 0;
}

.hero_area.sub_pages {
  height: auto;
}

.header_section .container-fluid {
  padding-right: 25px;
  padding-left: 25px;
}

.header_section .nav_container {
  margin: 0 auto;
}

.custom_nav-container.navbar-expand-lg .navbar-nav .nav-item .nav-link {
  margin: 10px 30px;
  padding: 0;
  padding-bottom: 3px;
  color: #ffffff;
  text-align: center;
  position: relative;
  text-transform: uppercase;
  font-size: 15px;
}

.custom_nav-container.navbar-expand-lg .navbar-nav .nav-item .nav-link::after {
  display: none;
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 3px;
  border-radius: 5px;
  background-color: #ffffff;
}

.custom_nav-container.navbar-expand-lg .navbar-nav .nav-item.active a::after, .custom_nav-container.navbar-expand-lg .navbar-nav .nav-item:hover a::after {
  display: block;
  background-color: #ff2953;
}

a,
a:hover,
a:focus {
  text-decoration: none;
}

a:hover,
a:focus {
  color: initial;
}

.btn,
.btn:focus {
  outline: none !important;
  -webkit-box-shadow: none;
          box-shadow: none;
}

.user_option {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.user_option a {
  color: #ffffff;
  margin: 10px 30px;
}

.custom_nav-container .nav_search-btn {
  background-image: url(../images/search-icon.png);
  background-size: 22px;
  background-repeat: no-repeat;
  background-position-y: 7px;
  width: 35px;
  height: 35px;
  padding: 0;
  border: none;
}

.navbar-brand {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  position: relative;
}

.navbar-brand span {
  font-size: 22px;
  text-transform: uppercase;
  font-weight: bold;
  color: #ffffff;
  position: relative;
  z-index: 3;
}

.custom_nav-container {
  z-index: 99999;
  padding: 15px 0;
}

.custom_nav-container .navbar-toggler {
  outline: none;
}

.custom_nav-container .navbar-toggler .navbar-toggler-icon {
  background-image: url(../images/menu.png);
  background-size: 55px;
}

/*end header section*/
.slider_section {
  -webkit-box-flex: 1;
      -ms-flex: 1;
          flex: 1;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  color: #ffffff;
}

.slider_section #carouselExampleIndicators {
  width: 100%;
}

.slider_section .row {
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.slider_section .box {
  margin: 125px 0;
}

.slider_section .detail-box {
  text-align: center;
}

.slider_section .detail-box h1,
.slider_section .detail-box h2,
.slider_section .detail-box h3 {
  text-transform: uppercase;
  font-weight: bold;
}

.slider_section .detail-box h2 {
  font-size: 2.5rem;
}

.slider_section .detail-box h1 {
  font-size: 3.5rem;
  font-weight: bold;
  letter-spacing: .5rem;
}

.slider_section .detail-box p {
  margin-top: 25px;
}

.slider_section .detail-box a {
  display: inline-block;
  padding: 8px 35px;
  background-color: transparent;
  border: 1.5px solid #ffffff;
  color: #ffffff;
  border-radius: 0px;
  -webkit-transition: -webkit-transform 0.3s;
  transition: -webkit-transform 0.3s;
  transition: transform 0.3s;
  transition: transform 0.3s, -webkit-transform 0.3s;
  text-transform: uppercase;
  margin-top: 35px;
}

.slider_section .detail-box a:hover {
  background-color: #ffffff;
  color: #000000;
}

.slider_section #carouselExampleIndicators .carousel-indicators {
  position: unset;
  margin: 0;
  margin-top: 45px;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.slider_section #carouselExampleIndicators .carousel-indicators li {
  width: 14px;
  height: 14px;
  background-color: transparent;
  border: 2px solid #ffffff;
  border-radius: 100%;
  opacity: 1;
}

.slider_section #carouselExampleIndicators .carousel-indicators li.active {
  border: 4px solid #ffffff;
}

.us_section {
  background-image: url(../images/us-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: #ffffff;
}

.us_section .us_container {
  padding-top: 25px;
}

.us_section .us_container .box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  text-align: center;
  margin: 25px 10px 0 10px;
}

.us_section .us_container .box .img-box {
  height: 100px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
}

.us_section .us_container .box .img-box img {
  max-width: 100%;
}

.us_section .us_container .box .detail-box h5 {
  font-weight: bold;
}

.heathy_section {
  background-image: url(../images/healthy-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: #ffffff;
  text-align: center;
}

.heathy_section h2 {
  font-weight: bold;
}

.heathy_section p {
  margin-top: 35px;
}

.heathy_section .btn-box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  margin-top: 45px;
}

.heathy_section .btn-box a {
  display: inline-block;
  padding: 8px 35px;
  background-color: transparent;
  border: 1.5px solid #ffffff;
  color: #ffffff;
  border-radius: 0;
  -webkit-transition: -webkit-transform 0.3s;
  transition: -webkit-transform 0.3s;
  transition: transform 0.3s;
  transition: transform 0.3s, -webkit-transform 0.3s;
  text-transform: uppercase;
}

.heathy_section .btn-box a:hover {
  background-color: #ffffff;
  color: #000000;
}

.trainer_section {
  background-image: url(../images/trainer-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: #ffffff;
}

.trainer_section .box {
  margin-top: 55px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  text-align: center;
}

.trainer_section .box .name h5 {
  font-weight: bold;
  margin-bottom: 15px;
}

.trainer_section .box .img-box {
  border-radius: 15px;
  overflow: hidden;
}

.trainer_section .box .img-box img {
  width: 100%;
}

.trainer_section .box .social_box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
  width: 225px;
  padding: 12px 45px;
  background-color: #ffffff;
  border-radius: 50px;
  margin-top: -25px;
}

.contact_section {
  position: relative;
  background-color: #27223f;
  color: #ffffff;
}

.contact_section .heading_container {
  -webkit-box-pack: start;
      -ms-flex-pack: start;
          justify-content: start;
}

.contact_section .heading_container h2::before {
  text-align: left;
  left: 0;
  -webkit-transform: none;
          transform: none;
}

.contact_section .row {
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.contact_section .img-box img {
  width: 100%;
}

.contact_section .form_container {
  padding: 45px 0 45px 15px;
}

.contact_section input {
  width: 100%;
  border: none;
  background-color: #ffffff;
  outline: none;
  color: #000000;
  margin-top: 25px;
  padding: 12px;
}

.contact_section input::-webkit-input-placeholder {
  color: #2a2a2c;
}

.contact_section input:-ms-input-placeholder {
  color: #2a2a2c;
}

.contact_section input::-ms-input-placeholder {
  color: #2a2a2c;
}

.contact_section input::placeholder {
  color: #2a2a2c;
}

.contact_section input.message-box {
  padding: 45px 12px;
}

.contact_section button {
  padding: 10px 65px;
  outline: none;
  border: none;
  color: #ffffff;
  background: #ff2953;
  margin: 45px 0 0 auto;
  text-transform: uppercase;
}

.info_section {
  background-color: #252233;
}

.info_items {
  width: 70%;
  margin: 0 auto;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
}

.info_items .item {
  width: 200px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  text-align: center;
}

.info_items .item .img-box {
  width: 80px;
  height: 80px;
  border-radius: 100%;
  background-repeat: no-repeat;
  background-position: center;
}

.info_items .item .detail-box {
  margin-top: 5px;
  color: #fff;
}

.info_items {
  position: relative;
}

.info_items a {
  position: relative;
}

.info_items .item .img-box.box-1 {
  background-image: url(../images/location-white.png);
}

.info_items .item .img-box.box-2 {
  background-image: url(../images/telephone-white.png);
}

.info_items .item .img-box.box-3 {
  background-image: url(../images/envelope-white.png);
}

/* footer section*/
.footer_section {
  background-color: #fbfdfd;
  padding: 20px;
  font-weight: 500;
}

.footer_section p {
  color: #292929;
  margin: 0;
  text-align: center;
}

.footer_section a {
  color: #292929;
}

/* end footer section*/
/*# sourceMappingURL=style.css.map */
body {
  font-family: 'Poppins', sans-serif;
  color: #000000;
  background-color: #ffffff;
}

.layout_padding {
  padding-top: 120px;
  padding-bottom: 120px;
}

.layout_padding2 {
  padding-top: 45px;
  padding-bottom: 45px;
}

.layout_padding2-top {
  padding-top: 45px;
}

.layout_padding2-bottom {
  padding-bottom: 45px;
}

.layout_padding-top {
  padding-top: 120px;
}

.layout_padding-bottom {
  padding-bottom: 120px;
}

.heading_container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  text-align: center;
}

.heading_container h2 {
  font-weight: bold;
  position: relative;
  padding-bottom: 5px;
  text-transform: uppercase;
}

.heading_container h2::before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 55px;
  height: 5px;
  background-color: #ff2953;
  -webkit-transform: translateX(-50%);
          transform: translateX(-50%);
}

/*header section*/
.hero_area {
  height: 100vh;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  background-image: url(../images/hero-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
}

.sub_page .hero_area {
  height: auto;
}

.sub_page .who_section.layout_padding {
  padding-top: 0;
}

.hero_area.sub_pages {
  height: auto;
}

.header_section .container-fluid {
  padding-right: 25px;
  padding-left: 25px;
}

.header_section .nav_container {
  margin: 0 auto;
}

.custom_nav-container.navbar-expand-lg .navbar-nav .nav-item .nav-link {
  margin: 10px 30px;
  padding: 0;
  padding-bottom: 3px;
  color: #ffffff;
  text-align: center;
  position: relative;
  text-transform: uppercase;
  font-size: 15px;
}

.custom_nav-container.navbar-expand-lg .navbar-nav .nav-item .nav-link::after {
  display: none;
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 3px;
  border-radius: 5px;
  background-color: #ffffff;
}

.custom_nav-container.navbar-expand-lg .navbar-nav .nav-item.active a::after, .custom_nav-container.navbar-expand-lg .navbar-nav .nav-item:hover a::after {
  display: block;
  background-color: #ff2953;
}

a,
a:hover,
a:focus {
  text-decoration: none;
}

a:hover,
a:focus {
  color: initial;
}

.btn,
.btn:focus {
  outline: none !important;
  -webkit-box-shadow: none;
          box-shadow: none;
}

.user_option {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.user_option a {
  color: #ffffff;
  margin: 10px 30px;
}

.custom_nav-container .nav_search-btn {
  background-image: url(../images/search-icon.png);
  background-size: 22px;
  background-repeat: no-repeat;
  background-position-y: 7px;
  width: 35px;
  height: 35px;
  padding: 0;
  border: none;
}

.navbar-brand {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  position: relative;
}

.navbar-brand span {
  font-size: 22px;
  text-transform: uppercase;
  font-weight: bold;
  color: #ffffff;
  position: relative;
  z-index: 3;
}

.custom_nav-container {
  z-index: 99999;
  padding: 15px 0;
}

.custom_nav-container .navbar-toggler {
  outline: none;
}

.custom_nav-container .navbar-toggler .navbar-toggler-icon {
  background-image: url(../images/menu.png);
  background-size: 55px;
}

/*end header section*/
.slider_section {
  -webkit-box-flex: 1;
      -ms-flex: 1;
          flex: 1;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  color: #ffffff;
}

.slider_section #carouselExampleIndicators {
  width: 100%;
}

.slider_section .row {
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.slider_section .box {
  margin: 125px 0;
}

.slider_section .detail-box {
  text-align: center;
}

.slider_section .detail-box h1,
.slider_section .detail-box h2,
.slider_section .detail-box h3 {
  text-transform: uppercase;
  font-weight: bold;
}

.slider_section .detail-box h2 {
  font-size: 2.5rem;
}

.slider_section .detail-box h1 {
  font-size: 3.5rem;
  font-weight: bold;
  letter-spacing: .5rem;
}

.slider_section .detail-box p {
  margin-top: 25px;
}

.slider_section .detail-box a {
  display: inline-block;
  padding: 8px 35px;
  background-color: transparent;
  border: 1.5px solid #ffffff;
  color: #ffffff;
  border-radius: 0px;
  -webkit-transition: -webkit-transform 0.3s;
  transition: -webkit-transform 0.3s;
  transition: transform 0.3s;
  transition: transform 0.3s, -webkit-transform 0.3s;
  text-transform: uppercase;
  margin-top: 35px;
}

.slider_section .detail-box a:hover {
  background-color: #ffffff;
  color: #000000;
}

.slider_section #carouselExampleIndicators .carousel-indicators {
  position: unset;
  margin: 0;
  margin-top: 45px;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.slider_section #carouselExampleIndicators .carousel-indicators li {
  width: 14px;
  height: 14px;
  background-color: transparent;
  border: 2px solid #ffffff;
  border-radius: 100%;
  opacity: 1;
}

.slider_section #carouselExampleIndicators .carousel-indicators li.active {
  border: 4px solid #ffffff;
}

.us_section {
  background-image: url(../images/us-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: #ffffff;
}

.us_section .us_container {
  padding-top: 25px;
}

.us_section .us_container .box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  text-align: center;
  margin: 25px 10px 0 10px;
}

.us_section .us_container .box .img-box {
  height: 100px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
}

.us_section .us_container .box .img-box img {
  max-width: 100%;
}

.us_section .us_container .box .detail-box h5 {
  font-weight: bold;
}

.heathy_section {
  background-image: url(../images/healthy-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: #ffffff;
  text-align: center;
}

.heathy_section h2 {
  font-weight: bold;
}

.heathy_section p {
  margin-top: 35px;
}

.heathy_section .btn-box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  margin-top: 45px;
}

.heathy_section .btn-box a {
  display: inline-block;
  padding: 8px 35px;
  background-color: transparent;
  border: 1.5px solid #ffffff;
  color: #ffffff;
  border-radius: 0;
  -webkit-transition: -webkit-transform 0.3s;
  transition: -webkit-transform 0.3s;
  transition: transform 0.3s;
  transition: transform 0.3s, -webkit-transform 0.3s;
  text-transform: uppercase;
}

.heathy_section .btn-box a:hover {
  background-color: #ffffff;
  color: #000000;
}

.trainer_section {
  background-image: url(../images/trainer-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: #ffffff;
}

.trainer_section .box {
  margin-top: 55px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  text-align: center;
}

.trainer_section .box .name h5 {
  font-weight: bold;
  margin-bottom: 15px;
}

.trainer_section .box .img-box {
  border-radius: 15px;
  overflow: hidden;
}

.trainer_section .box .img-box img {
  width: 100%;
}

.trainer_section .box .social_box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
  width: 225px;
  padding: 12px 45px;
  background-color: #ffffff;
  border-radius: 50px;
  margin-top: -25px;
}

.contact_section {
  position: relative;
  background-color: #27223f;
  color: #ffffff;
}

.contact_section .heading_container {
  -webkit-box-pack: start;
      -ms-flex-pack: start;
          justify-content: start;
}

.contact_section .heading_container h2::before {
  text-align: left;
  left: 0;
  -webkit-transform: none;
          transform: none;
}

.contact_section .row {
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.contact_section .img-box img {
  width: 100%;
}

.contact_section .form_container {
  padding: 45px 0 45px 15px;
}

.contact_section input {
  width: 100%;
  border: none;
  background-color: #ffffff;
  outline: none;
  color: #000000;
  margin-top: 25px;
  padding: 12px;
}

.contact_section input::-webkit-input-placeholder {
  color: #2a2a2c;
}

.contact_section input:-ms-input-placeholder {
  color: #2a2a2c;
}

.contact_section input::-ms-input-placeholder {
  color: #2a2a2c;
}

.contact_section input::placeholder {
  color: #2a2a2c;
}

.contact_section input.message-box {
  padding: 45px 12px;
}

.contact_section button {
  padding: 10px 65px;
  outline: none;
  border: none;
  color: #ffffff;
  background: #ff2953;
  margin: 45px 0 0 auto;
  text-transform: uppercase;
}

.info_section {
  background-color: #252233;
}

.info_items {
  width: 70%;
  margin: 0 auto;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
}

.info_items .item {
  width: 200px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  text-align: center;
}

.info_items .item .img-box {
  width: 80px;
  height: 80px;
  border-radius: 100%;
  background-repeat: no-repeat;
  background-position: center;
}

.info_items .item .detail-box {
  margin-top: 5px;
  color: #fff;
}

.info_items {
  position: relative;
}

.info_items a {
  position: relative;
}

.info_items .item .img-box.box-1 {
  background-image: url(../images/location-white.png);
}

.info_items .item .img-box.box-2 {
  background-image: url(../images/telephone-white.png);
}

.info_items .item .img-box.box-3 {
  background-image: url(../images/envelope-white.png);
}

/* footer section*/
.footer_section {
  background-color: #fbfdfd;
  padding: 20px;
  font-weight: 500;
}

.footer_section p {
  color: #292929;
  margin: 0;
  text-align: center;
}

.footer_section a {
  color: #292929;
}

/* end footer section*/
/*# sourceMappingURL=style.css.map */

```
# style.scss


```bash
$black: #000000;
$white: #ffffff;
$primary1: #ff2953;

@mixin main-font {
  font-family: 'Poppins', sans-serif;
}

@mixin hero_btn($col1, $col2, $pad1, $pad2, $bRadius) {
  display: inline-block;
  padding: $pad1 $pad2;
  background-color: transparent;
  border: 1.5px solid $col1;
  color: $col1;
  border-radius: $bRadius;
  transition: transform 0.3s;

  &:hover {
    background-color: $col1;
    color: $col2;
  }
}

@mixin upperBold {
  text-transform: uppercase;
  font-weight: bold;
}

body {
  @include main-font;
  color: #000000;
  background-color: #ffffff;
}

.layout_padding {
  padding-top: 120px;
  padding-bottom: 120px;
}

.layout_padding2 {
  padding-top: 45px;
  padding-bottom: 45px;
}

.layout_padding2-top {
  padding-top: 45px;
}

.layout_padding2-bottom {
  padding-bottom: 45px;
}

.layout_padding-top {
  padding-top: 120px;
}

.layout_padding-bottom {
  padding-bottom: 120px;
}

.heading_container {
  display: flex;
  justify-content: center;
  text-align: center;

  h2 {
    font-weight: bold;
    position: relative;
    padding-bottom: 5px;
    text-transform: uppercase;

    &::before {
      content: "";
      position: absolute;
      bottom: 0;
      left: 50%;
      width: 55px;
      height: 5px;
      background-color: $primary1;
      transform: translateX(-50%);
    }
  }
}

/*header section*/
.hero_area {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-image: url(../images/hero-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
}

.sub_page {
  .hero_area {
    height: auto;
  }

  .who_section.layout_padding {
    padding-top: 0;
  }
}

.hero_area.sub_pages {
  height: auto;
}

.header_section {}

.header_section .container-fluid {
  padding-right: 25px;
  padding-left: 25px;
}

.header_section .nav_container {
  margin: 0 auto;
}

.custom_nav-container.navbar-expand-lg .navbar-nav .nav-item {
  .nav-link {
    margin: 10px 30px;
    padding: 0;
    padding-bottom: 3px;
    color: #ffffff;
    text-align: center;
    position: relative;
    text-transform: uppercase;
    font-size: 15px;

    &::after {
      display: none;
      content: "";
      position: absolute;
      left: 0;
      bottom: 0;
      width: 100%;
      height: 3px;
      border-radius: 5px;
      background-color: $white;
    }
  }

  &.active,
  &:hover {
    a {
      &::after {
        display: block;
        background-color: $primary1;
      }
    }
  }
}

a,
a:hover,
a:focus {
  text-decoration: none;
}

a:hover,
a:focus {
  color: initial;
}

.btn,
.btn:focus {
  outline: none !important;
  box-shadow: none;
}

.user_option {
  display: flex;
  align-items: center;

  a {
    color: $white;
    margin: 10px 30px;
  }
}

.custom_nav-container .nav_search-btn {
  background-image: url(../images/search-icon.png);
  background-size: 22px;
  background-repeat: no-repeat;
  background-position-y: 7px;
  width: 35px;
  height: 35px;
  padding: 0;
  border: none;
}

.navbar-brand {
  display: flex;
  align-items: center;
  position: relative;

  span {
    font-size: 22px;
    text-transform: uppercase;
    font-weight: bold;
    color: $white;
    position: relative;
    z-index: 3;
  }

}

.custom_nav-container {
  z-index: 99999;
  padding: 15px 0;
}

.custom_nav-container .navbar-toggler {
  outline: none;
}

.custom_nav-container .navbar-toggler .navbar-toggler-icon {
  background-image: url(../images/menu.png);
  background-size: 55px;
}

/*end header section*/

.slider_section {
  flex: 1;
  display: flex;
  align-items: center;
  color: $white;

  #carouselExampleIndicators {
    width: 100%;
  }

  .row {
    align-items: center;
  }

  .box {
    margin: 125px 0;
  }

  .detail-box {
    text-align: center;

    h1,
    h2,
    h3 {
      text-transform: uppercase;
      font-weight: bold;

    }

    h2 {
      font-size: 2.5rem;
    }

    h1 {
      font-size: 3.5rem;
      font-weight: bold;
      letter-spacing: .5rem;
    }



    p {
      margin-top: 25px;
    }

    a {
      @include hero_btn($white, $black, 8px, 35px, 0px);
      text-transform: uppercase;
      margin-top: 35px;
    }
  }



  #carouselExampleIndicators {
    .carousel-indicators {
      position: unset;
      margin: 0;
      margin-top: 45px;
      align-items: center;

      li {
        width: 14px;
        height: 14px;
        background-color: transparent;
        border: 2px solid $white;
        border-radius: 100%;
        opacity: 1;

        &.active {
          border: 4px solid $white;
        }
      }
    }
  }
}

// end slider section


// us section

.us_section {
  background-image: url(../images/us-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: $white;

  .us_container {
    padding-top: 25px;

    .box {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin: 25px 10px 0 10px;

      .img-box {
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;

        img {
          max-width: 100%;
        }
      }

      .detail-box {
        h5 {
          font-weight: bold;
        }
      }
    }
  }
}


// end us section

// heathy section

.heathy_section {
  background-image: url(../images/healthy-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: $white;
  text-align: center;

  h2 {
    font-weight: bold;
  }

  p {
    margin-top: 35px;
  }

  .btn-box {
    display: flex;
    justify-content: center;
    margin-top: 45px;

    a {
      @include hero_btn($white, $black, 8px, 35px, 0);
      text-transform: uppercase;

    }
  }
}

// end heathy section


// trainer section

.trainer_section {
  background-image: url(../images/trainer-bg.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: $white;

  .box {
    margin-top: 55px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;

    .name {
      h5 {
        font-weight: bold;
        margin-bottom: 15px;
      }

    }

    .img-box {
      border-radius: 15px;
      overflow: hidden;

      img {
        width: 100%;
      }
    }

    .social_box {
      display: flex;
      justify-content: space-between;
      width: 225px;
      padding: 12px 45px;
      background-color: $white;
      border-radius: 50px;
      margin-top: -25px;
    }
  }
}


// end trainer section


// contact section
.contact_section {
  position: relative;
  background-color: #27223f;
  color: $white;

  .heading_container {
    justify-content: start;

    h2 {
      &::before {
        text-align: left;
        left: 0;
        transform: none;
      }
    }
  }

  .row {
    align-items: center;
  }

  .img-box {
    img {
      width: 100%;
    }
  }



  .form_container {
    padding: 45px 0 45px 15px;

  }

  form {}

  input {
    width: 100%;
    border: none;
    background-color: $white;
    outline: none;
    color: $black;
    margin-top: 25px;
    padding: 12px;

    &::placeholder {
      color: #2a2a2c;
    }

    &.message-box {
      padding: 45px 12px;
    }
  }

  button {
    padding: 10px 65px;
    outline: none;
    border: none;
    color: $white;
    background: #ff2953;
    margin: 45px 0 0 auto;
    text-transform: uppercase;
  }

}

// end contact section





// info section
.info_section {
  background-color: #252233;
}

.info_items {
  width: 70%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;

  .item {
    width: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;

    .img-box {
      width: 80px;
      height: 80px;
      border-radius: 100%;
      background-repeat: no-repeat;
      background-position: center;
    }

    .detail-box {
      margin-top: 5px;
      color: #fff;
    }
  }
}

.info_items {
  position: relative;

  a {
    position: relative;
  }

  .item {
    .img-box {
      &.box-1 {
        background-image: url(../images/location-white.png);
      }

      &.box-2 {
        background-image: url(../images/telephone-white.png);
      }

      &.box-3 {
        background-image: url(../images/envelope-white.png);
      }
    }
  }
}

// end info section




/* footer section*/

.footer_section {
  background-color: #fbfdfd;
  padding: 20px;
  font-weight: 500;
}

.footer_section p {
  color: #292929;
  margin: 0;
  text-align: center;
}

.footer_section a {
  color: #292929;
}

/* end footer section*/
```
# dod
```bash

{
    "version": 3,
    "mappings": "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",
    "sources": [
        "style.scss"
    ],
    "names": [],
    "file": "style.css"
}

```




# DOC-LAB-8-HOSTING-STATIC-WEBSITE
# Step 1: Clone GitHub Repository

```bash
git clone https://github.com/alfi-teachs/DOC-LAB-8-HOSTING-STATIC-WEBSITE.git
```
# Step 2: Go Inside Project Folder
```bash
cd DOC-LAB-8-HOSTING-STATIC-WEBSITE
```
# Step 3: Build Docker Image
```bash
docker build -t gym .
```
# Step 4: Run Docker Container
```bash
docker run -d -p 2000:80 --name gym-container gym
```
# Step 5: Check Running Containers 
```bash
docker ps
```
# Step 6: Open Website
```bash
http://localhost:2000
```
# Optional Commands

Stop Container
```bash
docker stop gym-container
```
Start Container Again
```bash
docker start gym-container
```
Remove Container
```bash
docker rm -f gym-container
```
Check Logs
```bash
docker logs gym-container
```
