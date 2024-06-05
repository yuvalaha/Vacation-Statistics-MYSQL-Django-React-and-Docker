-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2024 at 10:50 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `beautiful_vacation`
--
CREATE DATABASE IF NOT EXISTS `beautiful_vacation` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `beautiful_vacation`;

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `is_email_exist` (`user_email` VARCHAR(40))   BEGIN
	SELECT COUNT(*) > 0 AS email_exists
	FROM users
	WHERE email = user_email;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `all_vacations`
--

CREATE TABLE `all_vacations` (
  `vacation_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  `description` varchar(3000) NOT NULL,
  `vacation_start_date` date NOT NULL,
  `vacation_end_date` date NOT NULL,
  `price` int(11) NOT NULL,
  `vacation_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `all_vacations`
--

INSERT INTO `all_vacations` (`vacation_id`, `country_id`, `description`, `vacation_start_date`, `vacation_end_date`, `price`, `vacation_image`) VALUES
(1, 5, 'Escape to the captivating beauty of Italy for an unforgettable 16-day vacation. Embark on a journey through this enchanting country, where history, culture, and culinary delights await at every turn.\n\nBegin your adventure in the eternal city of Rome, where ancient ruins, Renaissance architecture, and world-class museums beckon. Explore iconic landmarks such as the Colosseum, Vatican City, and Trevi Fountain, and indulge in authentic Italian cuisine at charming trattorias and gelaterias.\n\nFrom Rome, venture to the picturesque region of Tuscany, where rolling hills, vineyards, and medieval towns await. Discover the art treasures of Florence, stroll through the enchanting streets of Siena, and savor the flavors of Chianti wine country.\n\nContinue your journey to the romantic city of Venice, where gondola rides along the winding canals and visits to historic landmarks such as St. Mark\'s Square and the Doge\'s Palace await. Explore the charming islands of Murano and Burano, known for their colorful houses and traditional craftsmanship.\n\nNext, travel to the stunning Amalfi Coast, where rugged cliffs, azure waters, and picturesque villages await. Explore the charming towns of Positano, Amalfi, and Ravello, and savor fresh seafood and limoncello while soaking up the Mediterranean sun.\n\nConclude your Italian adventure in the eternal city of Rome, where ancient ruins, Renaissance art, and vibrant street life await. Explore the iconic landmarks of the Vatican City, Colosseum, and Pantheon, and indulge in delicious Roman cuisine at local trattorias and cafes.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our 16-day vacation package promises an unforgettable journey through the heart of Italy. Book your trip today and experience the beauty and magic of this remarkable country.', '2024-11-07', '2024-11-23', 3000, '262e5d43-86e3-4a67-91e8-c57eb9c8900e.jpg'),
(2, 10, 'Discover the magic of Paris in July with our four-day vacation package. Immerse yourself in the romance, culture, and culinary delights of the City of Light as you explore iconic landmarks and hidden gems.\n\nBegin your adventure with a visit to the majestic Eiffel Tower, where you\'ll enjoy panoramic views of the cityscape. Then, wander through the historic streets of Montmartre, home to the Sacré-Cœur Basilica and charming artist\'s square, Place du Tertre.\n\nExperience Paris\'s rich history and artistry at the Louvre Museum, home to masterpieces like the Mona Lisa and Venus de Milo. Afterwards, explore the quaint streets of the Latin Quarter and visit the iconic Notre-Dame Cathedral.\n\nIndulge in French cuisine at local bistros and cafes, savoring delicious pastries and fine wines. Take a leisurely boat tour along the Seine River, passing by landmarks such as the Musée d\'Orsay and Place de la Concorde.\n\nSpend your final day exploring the vibrant neighborhoods of Saint-Germain-des-Prés and Le Marais, known for their trendy boutiques and lively atmosphere. Bid farewell to Paris with a delicious meal at a traditional brasserie.\n\nWith comfortable accommodations and expertly curated experiences, our Paris vacation package offers an unforgettable journey through one of the world\'s most enchanting cities. Book your escape today and let Paris captivate your heart!', '2024-07-02', '2024-07-06', 1255, 'bf45ce13-a464-4440-bf23-e3685652281c.jpg'),
(3, 1, 'Immerse yourself in the rich history, vibrant culture, and breathtaking landscapes of Israel with our four-day vacation package in March. From ancient ruins to modern cities, this itinerary offers a diverse and unforgettable journey through the Holy Land.\n\nBegin your adventure in the ancient city of Jerusalem, where history comes alive at every turn. Explore the winding streets of the Old City, home to iconic landmarks such as the Western Wall, Church of the Holy Sepulchre, and Dome of the Rock. Delve into the city\'s rich history with a visit to the Israel Museum and Yad Vashem Holocaust Memorial.\n\nVenture to the Judean Desert and discover the majestic fortress of Masada, overlooking the Dead Sea. Explore the ancient ruins, ride the cable car to the top, and soak in the stunning views of the surrounding desert landscape. Then, float effortlessly in the mineral-rich waters of the Dead Sea, known for their therapeutic properties.\n\nNext, journey to the vibrant city of Tel Aviv, where modernity meets tradition. Explore the bustling markets of Carmel and Levinsky, stroll along the picturesque beachfront promenade, and discover the vibrant street art scene of the Florentin neighborhood. Indulge in delicious Israeli cuisine at local eateries and sample fresh seafood at the bustling Jaffa Port.\n\nConclude your journey with a visit to the coastal city of Haifa, home to the stunning Baha\'i Gardens and Shrine. Explore the meticulously landscaped terraces, marvel at the golden-domed shrine, and soak in panoramic views of the city and sea from the top of Mount Carmel.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our four-day vacation package in Israel promises an unforgettable journey through this fascinating and diverse country. Book your trip today and discover the beauty and magic of Israel in March!', '2024-03-21', '2024-03-25', 2457, 'ecf74d74-1b23-4bfa-9ce5-3d367e4a3f29.jpg'),
(4, 3, 'Embark on an extraordinary 19-day adventure through the captivating landscapes, vibrant cities, and rich culture of Spain in March. From the bustling streets of Madrid to the sun-kissed beaches of the Mediterranean coast, this itinerary promises an unforgettable journey through one of Europe\'s most enchanting destinations.\n\nBegin your exploration in the bustling capital city of Madrid, where art, history, and culinary delights await at every turn. Explore world-class museums such as the Prado, Reina Sofia, and Thyssen-Bornemisza, stroll through the historic neighborhoods of Barrio de las Letras and La Latina, and indulge in delicious tapas and local wines at traditional tavernas.\n\nJourney south to the historic city of Toledo, a UNESCO World Heritage Site known for its medieval architecture, winding streets, and ancient synagogues, mosques, and churches. Discover the rich cultural heritage of this charming city as you explore landmarks such as the Alcázar, Cathedral, and Synagogue of Santa María la Blanca.\n\nNext, venture to the picturesque region of Andalusia, where Moorish palaces, whitewashed villages, and flamenco music await. Explore the majestic Alhambra Palace in Granada, marvel at the stunning architecture of the Mezquita in Córdoba, and wander through the narrow streets of the Albaicín and Santa Cruz neighborhoods.\n\nContinue your journey to the vibrant city of Seville, where the scent of orange blossoms fills the air and the sound of flamenco music echoes through the streets. Explore iconic landmarks such as the Alcázar, Plaza de España, and Seville Cathedral, and savor the flavors of Andalusian cuisine at local tapas bars and restaurants.\n\nFrom Seville, travel to the sun-drenched region of Costa del Sol, where golden beaches, crystal-clear waters, and charming coastal towns await. Relax on the beaches of Marbella, explore the historic center of Málaga, and indulge in fresh seafood and local wines at beachfront chiringuitos.\n\nConclude your journey in the vibrant city of Barcelona, where modernist architecture, world-class art, and vibrant street life await. Explore the iconic landmarks of Gaudí\'s Sagrada Familia and Park Güell, stroll down the lively boulevard of La Rambla, and discover the Gothic Quarter\'s medieval charm.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our 19-day vacation package in Spain promises an unforgettable journey through the heart and soul of this remarkable country. Book your trip today and discover the beauty and magic of Spain in March!', '2024-03-07', '2024-03-26', 2294, '1a9791e6-ea02-47d6-8902-53285911d607.jpg'),
(5, 13, 'Embark on the ultimate journey through the breathtaking landscapes, charming towns, and cultural treasures of Switzerland with our month-long vacation package in May and June. From the majestic Swiss Alps to the picturesque lakeside villages, this itinerary promises an unforgettable exploration of one of Europe\'s most stunning destinations.\n\nBegin your adventure in the vibrant city of Zurich, where historic architecture, world-class museums, and bustling markets await. Explore iconic landmarks such as the Grossmünster, Fraumünster, and Kunsthaus Zurich, and stroll along the picturesque shores of Lake Zurich. Indulge in delicious Swiss cuisine at local cafes and restaurants, and discover the city\'s vibrant nightlife with a visit to trendy bars and clubs.\n\nNext, travel to the charming town of Lucerne, nestled amidst the stunning scenery of Lake Lucerne and the surrounding mountains. Explore the medieval Old Town, cross the iconic Chapel Bridge, and visit the Swiss Transport Museum to learn about the country\'s transportation history. Take a scenic boat cruise on Lake Lucerne and ride the world\'s steepest cogwheel railway to the top of Mount Pilatus for panoramic views of the Alps.\n\nContinue your journey to the picturesque region of Interlaken, where towering mountains, lush valleys, and crystal-clear lakes await. Take a thrilling ride on the Jungfrau Railway to the Jungfraujoch, known as the \"Top of Europe,\" and marvel at the stunning views of the Aletsch Glacier and surrounding peaks. Explore the charming villages of Lauterbrunnen and Grindelwald, and embark on scenic hikes through the Bernese Oberland region.\n\nVenture into the heart of the Swiss Alps with a visit to the iconic resort town of Zermatt, home to the majestic Matterhorn. Explore the car-free streets of the town, take a scenic ride on the Gornergrat Railway to the Gornergrat summit, and enjoy outdoor activities such as hiking, mountain biking, and paragliding amidst stunning alpine scenery.\n\nConclude your journey with a visit to the picturesque lakeside town of Montreux, nestled on the shores of Lake Geneva. Explore the charming Old Town, visit the famous Chillon Castle, and take a leisurely boat cruise on Lake Geneva. Savor delicious Swiss cuisine at waterfront restaurants, and relax in the town\'s beautiful parks and gardens.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our month-long vacation package in Switzerland promises an unforgettable journey through the beauty and magic of this remarkable country. Book your trip today and immerse yourself in the natural wonders and cultural delights of Switzerland in May and June!', '2024-05-22', '2024-06-22', 596, 'f9258cd3-152b-4519-91a9-9b0875686c84.jpg'),
(6, 2, 'Experience the wonders of Greece during a spectacular 10-day vacation in June. From the ancient ruins of Athens to the idyllic islands of Santorini and Mykonos, immerse yourself in the rich history, vibrant culture, and stunning landscapes of this Mediterranean paradise.\n\nBegin your journey in the historic city of Athens, where ancient landmarks and modern attractions await. Explore the iconic Acropolis and its magnificent Parthenon, wander through the charming streets of Plaka, and discover the treasures of the National Archaeological Museum. Indulge in delicious Greek cuisine at traditional tavernas and rooftop restaurants overlooking the city.\n\nNext, venture to the picturesque island of Santorini, renowned for its breathtaking sunsets, whitewashed villages, and crystal-clear waters. Explore the cliffside town of Oia, stroll along the narrow streets of Fira, and relax on the black sand beaches of Perissa and Kamari. Visit the ancient ruins of Akrotiri and indulge in wine tasting at local vineyards overlooking the Aegean Sea.\n\nContinue your island-hopping adventure with a visit to the cosmopolitan island of Mykonos, famous for its vibrant nightlife, picturesque windmills, and beautiful beaches. Explore the charming town of Chora, stroll along the waterfront promenade of Little Venice, and party until dawn at world-renowned beach clubs such as Paradise and Super Paradise.\n\nConclude your journey with a visit to the historic city of Delphi, home to the legendary Oracle of Apollo and the Temple of Apollo. Explore the archaeological site, visit the Delphi Archaeological Museum, and marvel at the breathtaking views of the surrounding mountains and valleys.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our 10-day vacation package in Greece promises an unforgettable journey through the beauty and magic of this ancient land. Book your trip today and create memories that will last a lifetime!', '2024-04-06', '2024-06-14', 1200, 'cab99dea-5e1d-4593-8b4f-e2c9e52c3252.jpg'),
(7, 9, 'Embark on the adventure of a lifetime with a two-month vacation in Australia, spanning from January to the beginning of March. Explore the diverse landscapes, vibrant cities, and unique wildlife of this vast continent, experiencing everything from the iconic landmarks of Sydney to the natural wonders of the Outback.\n\nBegin your journey in Sydney, Australia\'s largest city and home to world-famous landmarks such as the Sydney Opera House and Sydney Harbour Bridge. Spend your days exploring the city\'s vibrant neighborhoods, relaxing on the golden sands of Bondi Beach, and cruising the iconic Sydney Harbour. Don\'t miss the chance to visit the nearby Blue Mountains for breathtaking views and outdoor adventures.\n\nFrom Sydney, travel north to the tropical paradise of Queensland. Explore the Great Barrier Reef, one of the Seven Natural Wonders of the World, and dive into the crystal-clear waters to discover an underwater world teeming with colorful marine life. Explore the lush rainforests of the Daintree and Cape Tribulation, and relax on the beautiful beaches of the Whitsunday Islands.\n\nContinue your journey to the Red Centre, where you\'ll discover the awe-inspiring landscapes of the Australian Outback. Explore the iconic Uluru-Kata Tjuta National Park, home to the stunning sandstone monolith of Uluru (Ayers Rock) and the ancient rock formations of Kata Tjuta (The Olgas). Experience the beauty of the Outback with guided tours, camel rides, and stargazing experiences under the vast desert sky.\n\nVenture south to the state of Victoria and discover the vibrant city of Melbourne, known for its diverse culture, thriving arts scene, and culinary delights. Explore the laneways and arcades of the city\'s historic center, visit world-class museums and galleries, and enjoy the city\'s famous coffee culture. Don\'t miss the chance to drive along the scenic Great Ocean Road and marvel at the Twelve Apostles, a series of limestone stacks rising majestically from the sea.\n\nConclude your Australian adventure in the stunning landscapes of Tasmania, where rugged mountains, pristine wilderness, and charming towns await. Explore the stunning landscapes of Cradle Mountain-Lake St Clair National Park, hike through the ancient forests of the Tarkine, and cruise the pristine waters of Wineglass Bay. Discover the rich history and heritage of Hobart, Tasmania\'s capital city, and indulge in fresh seafood and local produce at the famous Salamanca Market.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our two-month vacation package in Australia promises an unforgettable journey through the beauty and magic of this extraordinary continent. Book your trip today and create memories that will last a lifetime!', '2025-01-04', '2025-03-05', 6589, '8cc40e00-12a0-46e3-aee2-a1b942843e17.jpg'),
(8, 8, 'Embark on an unforgettable three-week vacation in Japan starting in April, the month when cherry blossoms bloom and the country comes alive with vibrant festivals and cultural celebrations. From the bustling streets of Tokyo to the tranquil temples of Kyoto, immerse yourself in the rich history, stunning landscapes, and unique culture of this fascinating destination.\n\nBegin your journey in the dynamic metropolis of Tokyo, where cutting-edge technology, ancient traditions, and modern pop culture converge. Explore iconic landmarks such as the historic Senso-ji Temple in Asakusa, the bustling Shibuya Crossing, and the futuristic district of Akihabara. Experience the city\'s vibrant nightlife, sample delicious street food at local markets, and immerse yourself in the world of manga and anime.\n\nNext, travel to the ancient city of Kyoto, known for its well-preserved temples, traditional tea houses, and serene gardens. Explore historic sites such as Kinkaku-ji (the Golden Pavilion), Fushimi Inari Taisha Shrine, and the iconic bamboo groves of Arashiyama. Experience a traditional tea ceremony, stroll through the picturesque streets of Gion, and witness the beauty of cherry blossoms in bloom at Maruyama Park.\n\nContinue your journey to the historic city of Nara, home to some of Japan\'s oldest and most significant temples and shrines. Visit the Todai-ji Temple, which houses a massive bronze Buddha statue, and explore the tranquil grounds of Nara Park, where friendly deer roam freely. Don\'t miss the chance to sample local delicacies such as Nara\'s famous sake and traditional mochi.\n\nFrom Nara, travel to the scenic region of Hakone, renowned for its hot springs, stunning views of Mount Fuji, and pristine natural beauty. Take a relaxing soak in an outdoor onsen, cruise the tranquil waters of Lake Ashi, and ride the Hakone Ropeway for panoramic views of the surrounding mountains. Explore the Hakone Open-Air Museum, home to a diverse collection of outdoor sculptures and artworks.\n\nConclude your journey with a visit to the vibrant city of Osaka, known for its bustling street food scene, historic landmarks, and lively entertainment districts. Indulge in delicious Osaka specialties such as takoyaki (octopus balls) and okonomiyaki (savory pancakes), visit iconic attractions such as Osaka Castle and the Dotonbori entertainment district, and experience the excitement of Universal Studios Japan.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our three-week vacation package in Japan promises an unforgettable journey through the beauty and magic of this extraordinary country. Book your trip today and discover the wonders of Japan in April!', '2025-04-01', '2025-04-22', 9999, '62c9fa14-c681-4c7c-b911-7a891019c88b.jpg'),
(9, 10, 'Escape to the romantic streets of Paris for a captivating three-day vacation in November. Immerse yourself in the city\'s rich history, vibrant culture, and culinary delights as you explore iconic landmarks and hidden gems.\n\nBegin your adventure with a visit to the majestic Eiffel Tower, where you\'ll be greeted by breathtaking views of the city\'s autumnal beauty. Then, wander through the charming cobblestone streets of Montmartre, home to the iconic Sacré-Cœur Basilica and bustling artist\'s square, Place du Tertre.\n\nDiscover Paris\'s artistic heritage at the Louvre Museum, home to world-renowned masterpieces such as the Mona Lisa and Venus de Milo. Afterwards, explore the historic Latin Quarter and marvel at the stunning architecture of Notre-Dame Cathedral.\n\nIndulge in French gastronomy at local cafes and brasseries, savoring hearty dishes like coq au vin and boeuf bourguignon. Take a leisurely cruise along the Seine River, admiring the city\'s enchanting landmarks illuminated against the night sky.\n\nOn your final day, explore the charming neighborhoods of Le Marais and Saint-Germain-des-Prés, known for their trendy boutiques and artisanal shops. Bid farewell to Paris with a visit to the iconic Champs-Élysées and a stroll through the romantic Tuileries Garden.\n\nWith comfortable accommodations and expertly curated experiences, our three-day Paris vacation package promises an unforgettable escape to the City of Light. Book your trip today and immerse yourself in the magic of Paris in November!', '2024-11-03', '2024-11-06', 8200, '1a29bcbb-d027-45ab-8fa7-a9a0bb53d940.jpg'),
(10, 3, 'Embark on an unforgettable week-long adventure through the vibrant landscapes, rich history, and cultural wonders of Spain in September. From the bustling streets of Barcelona to the historic landmarks of Madrid, this itinerary promises an immersive journey through some of Spain\'s most iconic destinations.\n\nBegin your journey in the cosmopolitan city of Barcelona, where stunning architecture, world-class art, and delicious cuisine await at every turn. Explore the architectural masterpieces of Antoni Gaudí, including the breathtaking Sagrada Familia and whimsical Park Güell, and stroll along the vibrant streets of the Gothic Quarter. Indulge in delicious tapas and seafood paella at local tavernas and beachfront restaurants along the Mediterranean coast.\n\nNext, travel to the historic city of Madrid, where grand boulevards, majestic plazas, and world-class museums await. Explore iconic landmarks such as the Royal Palace, Puerta del Sol, and Retiro Park, and immerse yourself in the art collections of the Prado and Reina Sofia museums. Experience the vibrant nightlife of Madrid with a visit to the lively neighborhoods of Malasaña and Chueca, where trendy bars and clubs abound.\n\nContinue your journey to the picturesque region of Andalusia, where Moorish palaces, whitewashed villages, and flamenco music await. Explore the stunning Alhambra Palace in Granada, stroll through the narrow streets of the Albaicín, and savor the flavors of Andalusian cuisine at local tapas bars and restaurants. Discover the rich cultural heritage of Seville with visits to the Alcázar, Plaza de España, and Seville Cathedral, and soak up the lively atmosphere of the city\'s historic neighborhoods.\n\nConclude your journey with a visit to the charming city of Valencia, where modern architecture, beautiful beaches, and delicious paella await. Explore the futuristic City of Arts and Sciences, wander through the historic center, and relax on the golden sands of Malvarrosa Beach. Savor the flavors of Valencia\'s famous dish, paella, and enjoy the city\'s vibrant nightlife with a visit to the trendy bars and clubs of the El Carmen neighborhood.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our week-long vacation package in Spain promises an unforgettable journey through the heart and soul of this remarkable country. Book your trip today and discover the beauty and magic of Spain in September!', '2024-12-09', '2024-12-16', 1856, '1a9791e6-ea02-47d6-8902-53285911d607.jpg'),
(11, 6, 'Experience the vibrant energy and endless possibilities of the city that never sleeps during a 17-day vacation in New York City in July. From iconic landmarks to hidden gems, cultural attractions to culinary delights, there\'s something for everyone to enjoy in this dynamic metropolis.\n\nBegin your journey by immersing yourself in the heart of Manhattan. Explore the neon-lit streets of Times Square, where bustling crowds and towering skyscrapers create an electric atmosphere. Take in a Broadway show, dine at world-class restaurants, and shop \'til you drop along Fifth Avenue.\n\nVenture uptown to Central Park, a sprawling oasis in the midst of the urban jungle. Spend leisurely afternoons picnicking on the Great Lawn, renting a rowboat on the lake, or exploring the park\'s many attractions, including the Central Park Zoo and Bethesda Terrace.\n\nDelve into New York\'s rich cultural scene with visits to renowned museums such as the Metropolitan Museum of Art, MoMA, and the Guggenheim. Marvel at masterpieces by Van Gogh, Picasso, and Warhol, and immerse yourself in exhibitions showcasing art from around the world.\n\nExplore the city\'s diverse neighborhoods, each offering its own unique charm and attractions. Stroll through the historic streets of Greenwich Village, sample international cuisine in Chinatown, and discover the vibrant street art scene in Bushwick, Brooklyn.\n\nIndulge your taste buds with culinary delights from around the globe. From gourmet food trucks to Michelin-starred restaurants, New York City is a paradise for food lovers. Savor classic New York-style pizza, bagels with lox and cream cheese, and decadent desserts from iconic bakeries.\n\nExperience the city\'s legendary nightlife, with rooftop bars boasting panoramic views, underground speakeasies serving craft cocktails, and live music venues showcasing the best local talent. Dance the night away in trendy clubs, catch a live jazz performance in Harlem, or simply stroll along the waterfront and take in the glittering skyline.\n\nThroughout your 17-day adventure, embrace the city\'s endless opportunities for exploration, adventure, and discovery. Whether you\'re admiring the skyline from atop the Empire State Building, cruising the Hudson River at sunset, or simply people-watching in one of the city\'s many parks, New York City promises an unforgettable experience that will leave you craving more.\n\n\n', '2024-07-12', '2024-07-29', 5000, '17af9124-3c2f-4288-8bd6-34d7e38a3a93.jpg'),
(12, 10, 'Experience the magic of Paris in the summertime with our unforgettable two-week vacation package! Immerse yourself in the rich culture, history, and romance of the City of Light as you explore iconic landmarks, savor delicious cuisine, and create lifelong memories.\n\nDuring your stay, you\'ll have the opportunity to visit world-famous attractions such as the Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and Arc de Triomphe. Stroll along the picturesque streets of Montmartre, cruise along the Seine River, and enjoy breathtaking views from the top of Montparnasse Tower.\n\nIndulge in the culinary delights of Paris with gastronomic experiences at charming bistros, quaint cafes, and Michelin-starred restaurants. Sample delectable pastries at local patisseries, sip on fine wines at intimate wine bars, and discover the flavors of French cuisine on a gourmet food tour.\n\nExplore the city\'s vibrant neighborhoods, from the historic Marais district to the trendy Le Marais and the artistic Saint-Germain-des-Prés. Browse chic boutiques along the Champs-Élysées, hunt for treasures at vintage markets, and soak up the bohemian atmosphere of the Latin Quarter.\n\nTake day trips to nearby attractions such as the Palace of Versailles, Claude Monet\'s Gardens in Giverny, and the Champagne region for a taste of luxury and elegance.\n\nWith comfortable accommodations, expertly curated activities, and personalized service, our Paris vacation package promises an unforgettable journey through one of the world\'s most enchanting cities. Book your dream vacation today and let Paris captivate your heart!\nArriving in Paris amidst the crisp autumn air, the city exuded an elegant charm. The Eiffel Tower, adorned in golden lights, painted the skyline with romance. Strolling along the Seine River, the Louvre\'s glass pyramid gleamed, and the Luxembourg Gardens offered a serene retreat in the heart of the bustling city.\n\nOctober 7, 2015 - Versailles: Palace Grandeur and Gardens Galore\n\nVenturing to Versailles, the opulent palace and its magnificent gardens unfolded a regal panorama. The Hall of Mirrors whispered tales of historical significance, and the expansive gardens, adorned with fountains and sculptures, provided a glimpse into the extravagance of French royalty.\n\nOctober 9, 2015 - Lyon: Gastronomic Delights and Silk Traditions\n\nThe journey continued to Lyon, the gastronomic capital, where culinary delights awaited. Traversing the traboules of Old Lyon, the city\'s silk trade history came alive. A stroll through the Croix-Rousse district and its colorful murals showcased the city\'s artistic and bohemian spirit.\n\nIn the pages of my travel journal, this short sojourn through France revealed the seasonal beauty of Paris in autumn, the regal splendor of Versailles, and the gastronomic wonders of Lyon. Each city, a chapter in a delightful French escapade—a tale woven with elegance, history, and culinary artistry. Au revoir, France  ', '2024-05-18', '2024-05-31', 128, 'd10f4290-f75e-4953-be6c-d7256cff100e.jpg'),
(13, 6, 'Start your adventure in the bustling metropolis of New York City, where you can explore iconic landmarks like Times Square, Central Park, and the Statue of Liberty. Dive into the city\'s rich cultural scene, sample diverse cuisine, and catch a Broadway show.\n\nFrom there, head to the nation\'s capital, Washington, D.C., to explore historic sites like the National Mall, the White House, and the Smithsonian museums. Learn about American history and politics while immersing yourself in the vibrant atmosphere of this dynamic city.\n\nNext, journey south to New Orleans, where you can experience the unique blend of French, Spanish, and Creole cultures. Explore the historic French Quarter, indulge in delicious Cajun cuisine, and soak up the lively music scene on Bourbon Street.\n\nContinue your journey to the awe-inspiring Grand Canyon in Arizona, where you can marvel at the breathtaking views and hike along scenic trails. Take a helicopter tour for a bird\'s-eye view of this natural wonder, and don\'t miss the chance to witness a stunning sunset over the canyon.\n\nNext, venture to the dazzling city of Las Vegas, where you can experience the excitement of the Las Vegas Strip, catch a world-class show, and try your luck at the casinos. Explore themed resorts, dine at gourmet restaurants, and take in the city\'s vibrant nightlife.\n\nAfter Las Vegas, head west to San Francisco, where you can explore iconic landmarks like the Golden Gate Bridge, Alcatraz Island, and Fisherman\'s Wharf. Discover eclectic neighborhoods, sample fresh seafood, and take a scenic drive along the Pacific Coast Highway.\n\nFinally, conclude your journey in Los Angeles, where you can soak up the sun on the beaches of Santa Monica, explore the entertainment capital of Hollywood, and visit famous attractions like the Hollywood Walk of Fame and Griffith Observatory.\n\nThroughout your 27-day vacation, you\'ll have the opportunity to experience the diversity and beauty of the United States, from bustling cities to natural wonders, historic landmarks to vibrant culture. It\'s a journey that promises unforgettable experiences and memories that will last a lifetime.', '2024-10-20', '2024-11-17', 561, '17af9124-3c2f-4288-8bd6-34d7e38a3a93.jpg'),
(14, 2, 'Embark on a magnificent two-week vacation in Greece during the vibrant month of August, immersing yourself in the rich history, stunning landscapes, and vibrant culture of this Mediterranean paradise. From the ancient wonders of Athens to the pristine beaches of the Greek islands, experience the best that Greece has to offer.\n\nBegin your adventure in the historic city of Athens, where ancient ruins and modern amenities blend seamlessly. Explore the iconic Acropolis and its awe-inspiring Parthenon, wander through the picturesque streets of Plaka, and visit the fascinating Acropolis Museum to learn about the city\'s rich history. Indulge in delicious Greek cuisine at traditional tavernas and rooftop restaurants overlooking the city\'s landmarks.\n\nNext, venture to the island of Crete, the largest and most diverse of the Greek islands. Explore the ancient Minoan ruins of Knossos, hike through the breathtaking Samaria Gorge, and relax on the beautiful beaches of Elafonissi and Balos. Discover charming villages such as Chania and Rethymno, where narrow streets are lined with Venetian architecture and cozy cafes.\n\nContinue your island-hopping adventure with a visit to the Cycladic island of Santorini, famous for its stunning sunsets and picturesque villages perched on cliff tops. Explore the charming town of Oia, stroll along the caldera rim in Fira, and relax on the black sand beaches of Perissa and Kamari. Visit local wineries to sample Santorini\'s renowned wines and enjoy a boat tour to the volcanic islands and hot springs.\n\nConclude your journey with a visit to the island of Rhodes, known for its medieval Old Town, pristine beaches, and ancient ruins. Explore the fortified city of Rhodes, a UNESCO World Heritage Site, visit the Acropolis of Lindos, and relax on the golden sands of Tsambika and Faliraki beaches. Discover hidden gems such as the Valley of the Butterflies and the Seven Springs, where lush landscapes and natural beauty abound.\n\nWith comfortable accommodations, expertly curated experiences, and personalized service, our two-week vacation package in Greece promises an unforgettable journey through the beauty and magic of this enchanting country. Book your trip today and create memories that will last a lifetime!', '2024-08-17', '2024-09-01', 555, 'cab99dea-5e1d-4593-8b4f-e2c9e52c3252.jpg'),
(15, 11, 'Embark on a mesmerizing 12-day journey through Portugal, a land of rich history, stunning landscapes, and vibrant culture. From the bustling streets of Lisbon to the sun-kissed shores of the Algarve, each day promises new discoveries and unforgettable experiences.\r\n\r\nBegin your adventure in Lisbon, the dynamic capital city where ancient history meets modern charm. Lose yourself in the winding alleyways of Alfama, savor traditional Portuguese delicacies in local eateries, and marvel at iconic landmarks such as Belém Tower and Jerónimos Monastery.\r\n\r\nNext, venture north to Porto, a city famed for its picturesque riverside setting and world-renowned port wine. Explore the historic Ribeira district, cruise along the Douro River past terraced vineyards, and sample exquisite wines in centuries-old cellars.\r\n\r\nContinue your journey to the Algarve, a region blessed with golden beaches, dramatic cliffs, and picturesque villages. Spend your days soaking up the sun on pristine sands, exploring charming coastal towns like Lagos and Faro, and indulging in fresh seafood delights.\r\n\r\nNo trip to Portugal would be complete without a visit to Sintra, a magical town nestled amidst lush greenery and dotted with fairytale palaces. Wander through the enchanting gardens of Pena Palace, explore the mystical Quinta da Regaleira, and admire the panoramic views from the Moorish Castle.\r\n\r\nConclude your adventure in Cascais, a charming coastal town where you can unwind on sandy beaches, stroll along scenic promenades, and sample delectable seafood dishes overlooking the shimmering sea.\r\n\r\nThroughout your journey, immerse yourself in Portugal\'s rich heritage, warm hospitality, and breathtaking beauty. Whether you\'re exploring historic cities, lounging on sun-drenched beaches, or savoring the flavors of Portuguese cuisine, each moment promises to be an unforgettable one in this captivating country.  ', '2025-01-03', '2025-01-15', 3698, '9580bc5d-8d21-4870-9cde-991fc56e51b8.jpg'),
(16, 12, 'Embark on an extraordinary two-week journey through Canada, where winter transforms the landscape into a magical wonderland of snow-capped mountains, frozen lakes, and cozy towns. From the vibrant cityscapes of Toronto and Montreal to the breathtaking wilderness of Banff and Jasper National Parks, this adventure promises to be an unforgettable exploration of Canada\'s diverse beauty and charm.\r\n\r\nBegin your journey in Toronto, Canada\'s largest city and cultural hub, where towering skyscrapers stand juxtaposed with lush green spaces. Discover iconic landmarks such as the CN Tower and explore vibrant neighborhoods like Kensington Market and Distillery District. Embrace the holiday spirit with festive events and dazzling light displays throughout the city.\r\n\r\nNext, travel to Montreal, a city renowned for its rich history, eclectic culture, and vibrant arts scene. Explore the historic streets of Old Montreal, visit world-class museums and galleries, and indulge in the city\'s culinary delights, from classic poutine to gourmet cuisine.\r\n\r\nContinue your adventure to Quebec City, a charming and picturesque destination steeped in French heritage. Wander through the narrow cobblestone streets of Old Quebec, admire the stunning architecture of Château Frontenac, and immerse yourself in the magical atmosphere of the city\'s Christmas markets and winter festivals.\r\n\r\nEscape to the pristine wilderness of Banff and Jasper National Parks, where towering mountains, frozen waterfalls, and sparkling glaciers await. Embark on exhilarating outdoor adventures such as skiing, snowshoeing, and ice skating, or simply marvel at the breathtaking scenery from the comfort of a cozy lodge.\r\n\r\nConclude your journey in Vancouver, a vibrant metropolis nestled between the mountains and the sea. Explore Stanley Park, Granville Island, and the bustling streets of downtown, and experience the city\'s diverse culinary scene, from fresh seafood to international cuisine.\r\n\r\nThroughout your two-week adventure, embrace the spirit of winter in Canada as you explore bustling cities, charming towns, and pristine wilderness. Whether you\'re enjoying outdoor adventures in the Rockies or sipping hot chocolate by a crackling fire, every moment promises to be filled with wonder and delight in this enchanting winter wonderland.  ', '2024-12-06', '2024-12-20', 8570, 'ea6eb767-79bd-4931-9240-638e06a433a8.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `country_id` int(11) NOT NULL,
  `country_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`country_id`, `country_name`) VALUES
(1, 'Israel'),
(2, 'Greece'),
(3, 'Spain'),
(4, 'Netherlands '),
(5, 'Italy'),
(6, 'Usa'),
(7, 'Brazil'),
(8, 'Japan'),
(9, 'Australia'),
(10, 'France'),
(11, 'Portugal'),
(12, 'Canada '),
(13, 'Switzerland'),
(14, 'Chile '),
(15, 'England'),
(16, 'Thailand');

-- --------------------------------------------------------

--
-- Table structure for table `likes`
--

CREATE TABLE `likes` (
  `user_id` int(11) NOT NULL,
  `vacation_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `likes`
--

INSERT INTO `likes` (`user_id`, `vacation_id`) VALUES
(2, 2),
(2, 3),
(2, 4),
(2, 13),
(3, 2),
(3, 3),
(3, 5),
(3, 15),
(4, 2),
(4, 3),
(4, 6),
(5, 3),
(5, 8),
(5, 13);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`role_id`, `role_name`) VALUES
(1, 'Admin'),
(2, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(400) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `password`, `role_id`) VALUES
(1, 'Yuval', 'Aharon', 'yuvalaharon@gmail.com', '5120eb43f0a337caae57262764db910724175a0d2d497ee10cdc391b9dc9afa76fec45650794d3bd112651a8b9c801fc0fdde65bf004ae4ce3e1462243507b4d', 1),
(2, 'George', 'Harrison', 'gh@gmail.com', 'da99190a60f3fc3f6a7bd557dca3f0db1e170aaa241ec04cd871a347ad516e9fdd608d5d9e66b328c075f135dd8f15975214eb4bef3a77fb83962c0a2329cc62', 2),
(3, 'John', 'Lennon', 'jl@gmail.com', '249b0640503500b08706e9d39fec5341833f0ea1ba694d5c855f0cfa609ab1e3bc0ed87d4346fbbee769fc7000c69c0c458adfad65beb0bcba41005e90a8853a', 2),
(4, 'Paul', 'McCartney', 'pm@hotmail.com', '3be817b3e5f29a30847ff25ff3ec9517ec46ab944003fbb0804ddc7b4b03176ea094114b772e1b1d7665e1d5eae6c9f77aaa51eed4464f6b947fe6ae55ee728e', 2),
(5, 'Ringo', 'Star', 'rs@yahoo.com', '0e64069b89197ea301fb935afa00284d9e67b16b0dee63faa1a376f7342cf9bc7eca236f36459613e3df264ef9a70e66919f37ceaabb7a29af3af028d0b309a7', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `all_vacations`
--
ALTER TABLE `all_vacations`
  ADD PRIMARY KEY (`vacation_id`),
  ADD KEY `country_id` (`country_id`);

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`country_id`);

--
-- Indexes for table `likes`
--
ALTER TABLE `likes`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `vacation_id` (`vacation_id`),
  ADD KEY `user_id_2` (`user_id`,`vacation_id`),
  ADD KEY `vacation_id_2` (`vacation_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `all_vacations`
--
ALTER TABLE `all_vacations`
  MODIFY `vacation_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `countries`
--
ALTER TABLE `countries`
  MODIFY `country_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `all_vacations`
--
ALTER TABLE `all_vacations`
  ADD CONSTRAINT `all_vacations_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`);

--
-- Constraints for table `likes`
--
ALTER TABLE `likes`
  ADD CONSTRAINT `likes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `likes_ibfk_2` FOREIGN KEY (`vacation_id`) REFERENCES `all_vacations` (`vacation_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
