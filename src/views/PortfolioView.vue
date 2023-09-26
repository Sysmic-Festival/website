<script setup>
</script>

<template>
    <div class="portfolio">
        <h1 class="large-title">Portfolio</h1>
        <div class="blue-line"></div>
        <div class="small-line"></div>
        <div class="xsmall-line"></div>
        <div class="years_list"></div>
          <section class="years_line">
            <router-link to="/portfolio/2022">
              <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2022.jpg">
              <h4>2022</h4>
            </div>
            </router-link>
            <router-link to="/portfolio/2021">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2021.jpg">
              <h4>2021</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2019">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2019.jpg">
              <h4>2019</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2018">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2018.jpg">
                <h4>2018</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2017">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2017.jpg">
                <h4>2017</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2016">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2016.jpg">
                <h4>2016</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2015">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2015.jpg">
                <h4>2015</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2014">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2014.jpg">
                <h4>2014</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2013">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2013.jpg">
                <h4>2013</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2012">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2012.jpg">
                <h4>2012</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2011">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2011.jpg">
                <h4>2011</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2010">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2010.jpg">
                <h4>2010</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2009">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2009.jpg">
                <h4>2009</h4>
            </div>
          </router-link>
          <router-link to="/portfolio/2008">
            <div class="year">
                <img class="year_image" src="https://www.sysmic.ch/ressources/portfolio/year_images/2008.jpg">
                <h4>2008</h4>
            </div>
          </router-link>
          </section>
        </div>

</template>

<style scoped>

.portfolio{
    margin: 10px;
    margin-top: calc(2*var(--global-margin) + var(--navbar-height));
}
.large-title {
  font-size: 90pt;
  font-weight: bold;
  color: var(--white);
}
.years_list{
    display: flex;
    max-width: 1200px;
    /* justify-content: space-evenly; */
    margin: auto;
}

.years_line{
    padding: 10px;
    display: inline-block;
    width: 100%;
    align-items: center;
}

.year_image{
    width: 80%;
    margin-top: 20px;
    height: auto;
}
.year{
  display: inline-block;
  align-items: center;
  width: 16%;
  margin: 1%;
  border-radius: 10px;
  border-bottom: 2px solid rgba(0, 0, 0, 0);
  border-top: 2px solid rgba(0, 0, 0, 0);
  border-left: 2px solid rgba(0, 0, 0, 0);
  border-right: 2px solid rgba(0, 0, 0, 0);
  box-shadow: 0 0 20px 10px var(--primary);
  background-color: var(--primary);
  transition: all 0.5s ease-in-out;
}

@media screen and (max-width: 850px) {
  .year{
    width: 50%;
  }
}
.year:hover{
  box-shadow: 0 0 30px 20px rgba(0,0,0,0.4);
  background-color: rgba(0,0,0,0.4);
  border-bottom: 2px solid var(--blue);
  border-top: 2px solid var(--blue);
  border-left: 2px solid var(--blue);
  border-right: 2px solid var(--blue);

}

.small-line{
  margin-bottom: 20px;
  margin-left: 37.5%;
  width: 25%;
  border: 1px solid var(--third);
}

.xsmall-line{
  margin-bottom: 75px;
  margin-left: 45%;
  width: 10%;
  border: 1px solid var(--third);
}

.blue-line{
  margin-bottom: 20px;
  width: 50%;
  margin-left: 25%;
  border: 1px solid var(--blue);
}

.year h4{
  text-align: center;
  font-size: 30pt;
  color: var(--white);
}

@media only screen and (max-width: 850px) {

    .large-title{
      font-size: 40pt;
    }

    h1{
      font-size: 25pt;
    }

    .apropos hr{
      max-width: 300px;
    }
    .small-line{
      margin-bottom: 10px;
    }
    .xsmall-line{
  margin-bottom: 50px;
    }
    .blue-line{
  margin-bottom: 10px;
    }
    .year{
      box-shadow: 0 0 30px 20px rgba(0,0,0,0.4);
      background-color: rgba(0,0,0,0.4);
      border-bottom: 2px solid var(--third);
      border-top: 2px solid var(--third);
      border-left: 2px solid var(--third);
      border-right: 2px solid var(--third);
      margin-bottom: 20px;
    }

}

</style>