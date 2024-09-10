

    <template>
      <footer>    

        <div class="flexFooter">

          <div>
            <p class="mailContact">
              <a href="mailto:contact@sysmic.ch">contact@sysmic.ch</a>
            </p>
            <p class="mailContact">
              <a href="mailto:webmaster@sysmic.ch">webmaster@sysmic.ch</a>  
            </p>
            <p class="infomaniakFooter">
              <a target="_BLANK" href="https://www.infomaniak.com/fr" >
                <img class = img-responsive src="@/assets/images/sponsors/infomaniak-sa-footer.png" />
              </a>
            </p>
          </div>  

          <div class="footerSocial">
            <a target="_BLANK" href="https://www.facebook.com/sysmic2021/" >
              <img class = img-responsive src="@/assets/images/utilitaries/facebook.svg" />
            </a>
            <a target="_BLANK" href="https://www.instagram.com/festival_sysmic/" >
              <img class = img-responsive src="@/assets/images/utilitaries/instagram.svg" />
            </a>
            <a target="_BLANK" href="https://www.youtube.com/channel/UCRymRQ502yvvwe0nwhj1kIw" >
              <img class = img-responsive src="@/assets/images/utilitaries/youtube.svg" />
            </a>
          </div>  

          <div class="footerPost">
            <p>
                Sysmic<br class="onlyDisplayFooter">
                EPFL-STI-BM, Station 17<br class="onlyDisplayFooter">
                1015 Lausanne
            </p>
          </div>  

        </div>
        <div class="copyright">
          <p>© Sysmic 2024</p>
        </div>    

      </footer>
    </template>

    <style scoped>
          /* Tooltip container */
        .tooltip {
          position: relative;
          display: inline-block;
        }   

        /* Tooltip text */
        .tooltip .tooltiptext {
          visibility: hidden;
          width: 130px;
          background-color: var(--primary);
          color: #fff;
          text-align: center;
          padding: 5px 0;
          border-radius: 6px;
          font-size: 15px;  

          /* Position the tooltip text */
          position: absolute;
          z-index: 1;
          bottom: 125%;
          left: 50%;
          margin-left: -60px;   

          /* Fade in tooltip */
          opacity: 0;
          transition: opacity 0.3s;
        }   

        /* Tooltip arrow */
        .tooltip .tooltiptext::after {
          content: "";
          position: absolute;
          top: 100%;
          left: 50%;
          margin-left: -5px;
          border-width: 5px;
          border-style: solid;
          border-color: var(--primary) transparent transparent transparent;
        }   

        /* Show the tooltip text when you mouse over the tooltip container */
        .tooltip:hover .tooltiptext {
          visibility: visible;
          opacity: 1;
        }   

        /********   FOOTER   ********/
        footer {
          font-size: calc(11pt + 0.5vw);
          color: var(--primary);
          text-align: center;

          z-index: 10;
          position: relative;
        }

        p{
          font-size: calc(11pt + 0.5vw) ;
          color: var(--grey-white) ;
          text-align: right ;
        }

        footer a{
          color: var(--grey-white);
        }
        footer a:hover{
          color: var(--primary-light);
        }
        footer img{
          height: 27px;
          position: relative;
          top: 7px;
          margin-right: 10px;
        }

        footer path{
          transition: fill, 0.4s
        }
        .infomaniakFooter img{
          height: 100%;
          width: auto;
          margin-left: 30px;
        }
        .flexFooter{
          display:flex;
          justify-content: space-between;
          align-items: center;
          flex-wrap: wrap;
          height: 180px;
          background-color: var(--secondary);
        }

        .footerPost{
          text-align:right !important;
          padding-right:30px;
        }

        .footerSocial{
          display: flex;
          justify-content: center;
        }

        .copyright{
          font-size: 12pt;
          color: var(--white);
          width:100% !important;
          display: flex;
          justify-content: center;
        }

        .copyright:hover{
          color: var(--secondary);
        }

        .onlyDisplayFooter{
          display:inline-block;
        }

        .mailContact{
          text-align: left;
          margin-left: 30px;
        }

        .img-responsive:hover{
          opacity: 0.90 ;
        }

        .copyright p{
          color: var(--white);
          text-align: center;
        }

        /******** FOOTER FOR PHONE ********/
      @media only screen and (max-width: 850px){
        footer img{
          width: 5vw;
        }
        .flexFooter{
            flex-direction: column;
            height: auto;
            padding: 10px;
            align-items:unset;
          
        }
        .flexFooter div{
            width: 100%;
        }
        .footerPost{
            display: flex;
            justify-content: center;
        }


        footer svg{
            height: 8vw;
            width: 15vw;
            vertical-align:middle;
        }
        footer p, footer a{
            font-size: 3.5vw;
            margin-right: 0 !important;
            margin-left: 0 !important;
        }


        .onlyDisplayFooter{
            display:none;
        }

        .mailContact{
          text-align: center;
          margin-left: 30px;
        }

        .infomaniakFooter a{
          margin-right: 0 !important;
          margin-left: 0 !important;
          display : flex;
          justify-content: center;
        }

      }

    </style>  