var express = require('express');
var router = express.Router();

var arr_apps_raw_low = [
  {"url":"https://play.google.com/store/apps/details?id=com.budgestudios.googleplay.BudgeWorld","appId":"com.budgestudios.googleplay.BudgeWorld","title":"Budge World - Pura Diversão","summary":"Mais de 100 atividades com 15 personagens preferidos das crianças!","developer":"Budge Studios","developerId":"7489594886728593506","icon":"//lh3.googleusercontent.com/jO0fvF-OUjcR7ybcb8N1rq31T0yZLlc_7bJzcRIgqJHjUL2fEFurwI01MbZzJOfUkdc=w340","score":"3.3","scoreText":"Com a classificação 3,3 de cinco estrelas","priceText":"","free":true},
  {"url":"https://play.google.com/store/apps/details?id=com.budgestudios.CaillouCheckUp","appId":"com.budgestudios.CaillouCheckUp","title":"Check Up do Caillou - Médico","summary":"Vá ao consultório médico com o Caillou e aprenda sobre check ups!","developer":"Budge Studios","developerId":"7489594886728593506","icon":"//lh3.googleusercontent.com/Ke63n_jNGtvJvAmSV0onlCb4Dxb5lOZn3FmbZDvOtkHGyy49fNePlHu87fbJ9j6y1A=w340","score":"3.2","scoreText":"Com a classificação 3,5 de cinco estrelas","priceText":"","free":true},
  {"url":"https://play.google.com/store/apps/details?id=com.toucangames.surgerygames.surgerysimulator.dentistgames.bracesgames","appId":"com.toucangames.surgerygames.surgerysimulator.dentistgames.bracesgames","title":"Suspensórios Simulador de","summary":"Experimente Grátis Este cintas jogo e se tornar um Suspensórios profissionais","developer":"Toucan Games 3D","developerId":"5304788608416827002","icon":"//lh3.googleusercontent.com/c1H3rHOc30JixZBZldVNIO5mz5hfFRLEWJ4WcBBhJE-0UXzijv0c6q05gAo6nsDK8X10=w340","score":"3.5","scoreText":"Com a classificação 3,2 de cinco estrelas","priceText":"","free":true},
  {"url":"https://play.google.com/store/apps/details?id=com.appways.potionmixer","appId":"com.appways.potionmixer","title":"Potion Mixer","summary":"Crie diferentes poções fazendo experimentos no laboratório seguindo as regras do laboratório.","developer":"Mixarium","developerId":"Mixarium","icon":"//lh3.ggpht.com/f7iv2k-TR68SVRbFL0V8gxqjZv9W_p8_GxRDY7vww4hQXvkEW-JDxSvjPVZF5PFiWo0=s180-rw","score":"2.9","scoreText":"Com a classificação 2,9 de cinco estrelas","priceText":"","free":true},
  {"url":"https://play.google.com/store/apps/details?id=com.beansprites.mypretendhousefamilyFREE","appId":"com.beansprites.mypretendhousefamilyFREE","title":"My Pretend House - Kids Family & Dollhouse Games","summary":"My Pretend house - Crianças Fazem Casa em Casa de Bonecas é muito divertido para crianças de todas as idades !!","developer":"Beansprites LLC","developerId":"Beansprites LLC","icon":"//lh3.googleusercontent.com/81RccLcaLY1gsGzjRbLdUKWC3O8_VC7GaThkXXUReYlxtO_PwGR8humpMUTLfC2sWbdM=s180-rw","score":"2.9","scoreText":"Com a classificação 2,9 de cinco estrelas","priceText":"","free":true}
]
var arr_apps_raw_high = [
  {"url":"https://play.google.com/store/apps/details?id=air.com.peppapig.paintbox","appId":"air.com.peppapig.paintbox","title":"Peppa Pig: Paintbox","summary":"é um aplicativo de desenho feito especialmente para os fãs da Peppa!","developer":"Entertainment One","developerId":"5920339924959681787","icon":"//lh3.googleusercontent.com/n5BfP13c0JQc7mR_aFmYcdEnp6iQjIAqM7vc7dusfsNwiJwBhSVZaF6nZedliheWVA8=w340","score":"4.0","scoreText":"Com a classificação 4,0 de cinco estrelas","priceText":"","free":true},
  {"url":"https://play.google.com/store/apps/details?id=com.miniklerogreniyor.quiz.kids.math","appId":"com.miniklerogreniyor.quiz.kids.math","title":"Jogos de Matemática","summary":"Adição, subtração, multiplicação, divisão, exponenciação, raiz quadrada.","developer":"Choloepus Apps","developerId":"4663374008815632170","icon":"//lh3.googleusercontent.com/-sQLnj5dYRB3kjK2TmJoO8IcDHc40QhY23zt5-4g74aySC_uo_lDCfEUkg8A9rgyKzG-=w340","score":"4.3","scoreText":"Com a classificação 4,3 de cinco estrelas","priceText":"","free":true},
  {"url":"https://play.google.com/store/apps/details?id=com.lego.duplo.trains","appId":"com.lego.duplo.trains","title":"LEGO® DUPLO® Train","summary":"Free educational game for toddlers and kids with NO in-app purchases and NO ads.","developer":"LEGO System A/S","developerId":"5382307214726356149","icon":"//lh3.googleusercontent.com/ACY6hsAubb7LV03YwnATpdDgGtrHlCMV-JuAnWZiotD9K_-qCAS0RePSAEDTInqRRw=w340","score":"3.9","scoreText":"Com a classificação 3,9 de cinco estrelas","priceText":"","free":true},
  {"url":"https://play.google.com/store/apps/details?id=air.com.tutotoons.app.babyhouse","appId":"air.com.tutotoons.app.babyhouse","title":"Bebé Doce - Casa","summary":"Bebé Doce - Casa","developer":"TutoTOONS","developerId":"6493980387780624296","icon":"//lh3.googleusercontent.com/dQ8LGHwsUMJa3Ibk50xBzy1MfN56ys9MBqeJl_hRZsd2dgQ3ka7WaYMYZ51EYkYJRz8k=s180-rw","score":"3.9","scoreText":"Com a classificação 3,9 de cinco estrelas","priceText":"","free":true},
  {"url":"https://play.google.com/store/apps/details?id=com.psvn.masha_and_the_bear_mini","appId":"com.psvn.masha_and_the_bear_mini","title":"Masha e o Urso para crianças","summary":"Continue por uma aventura! Traga a si mesmo e ao seu filho muita alegria. Nossos jogos familiares irão surpreendê-lo.","developer":"Hippo Baby Games for Girls and for Boys","developerId":"","icon":"//lh3.googleusercontent.com/nqmMRmMAbOzDuthNs_D3iE2AS5i7zVY6G_jmW7IeaNhJu23heQpYLEubyjjfGLjUZg=s180-rw","score":"4.3","scoreText":"Com a classificação 4,3 de cinco estrelas","priceText":"","free":true},
]

var arr_reviews_selected_low = []
var arr_reviews_selected_high = []

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { it_header: 'Home | Dashboard', title: 'Dashboard', it_footer: '2018 | Trabalho de cunho acadêmico científico' });
});

router.get('/about-project', function(req, res, next) {
  res.render('about_project', { it_header: 'ABOUT | Project', title: 'All informations about project', it_footer: '2018 | Trabalho de cunho acadêmico científico' });
});

router.get('/about-team', function(req, res, next) {
  res.render('about_team', { it_header: 'ABOUT | Team', title: 'Full team development', it_footer: '2018 | Trabalho de cunho acadêmico científico' });
});

router.get('/raw-data', function(req, res, next) {
  res.render('raw_data', { it_header: 'Data | Raw', title: 'All raw data', it_footer: '2018 | Trabalho de cunho acadêmico científico', raw_apps_low: arr_apps_raw_low, raw_apps_high: arr_apps_raw_high });
});

router.get('/clean-data', function(req, res, next) {
  res.render('clean_data', { it_header: 'Data | Clean', title: 'All clean data', it_footer: '2018 | Trabalho de cunho acadêmico científico' });
});

module.exports = router;
