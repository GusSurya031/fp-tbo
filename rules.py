RULES_CFG = {
    "K": [["S", "P"], ["P1", "O"], ["P1", "Pel"], ["P1", "Ket"],  ["P2", "Pel"],  ["P2", "Ket"],  ["P3", "Ket"], ["P4", "Ket"]],
    "P1": [["S", "P"]],
    "P2" :[["P1", "O"]],
    "P3" : [["P1", "Pel"]],
    "P4" : [["P2", "Pel"]],
    "S": [["NP", "AdjP"], ["NumP","NP"], ["NP","Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["nenek"], ["orang"], ["pengunjung"], ["sekitar"],["mahasiswa"], ["dewasa"], ["pemadam"], ["kebakaran"], ["anak"], ["laki-laki"], ["para"], ["siswa"], ["polisi"], ["burung"], ["merpati"], ["ikan"], ["koi"], ["kuda"], ["monyet"], ["kelinci"], ["lumba-lumba"], ["kupu-kupu"], ["sapi"], ["lebah"], ["seekor"], ["buaya"], ["siti"], ["rahayu"], ["ani"], ["adi"], ["santoso"], ["bu"], ["ratna"], ["hadi"], ["prayitno"], ["ibu"], ["sintia"], ["bapak"], ["haryono"], ["kiki"], ["mediterania"], ["bukit"], ["tinggi"], ["baikal"], ["copacabana"], ["rio"], ["de"], ["janeiro"], ["bali"], ["bandung"],["bogor"], ["denpasar"], ["surabaya"], ["jawa"], ["pentas"], ["ogoh-ogoh"], ["arab"], ["saudi"], ["indonesia"], ["dia"], ["saya"], ["teman"],  ["jepang"], ["guru"], ["medan"], ["kakek"],["pelatih"], ["kita"], ["gadis"], ["kucing"]],
    "P": [["Prep", "NP"],["Prep", "AdjP"], ["AdvP", "VP"], ["Adv", "AdjP"], ["NumP", "VP"], ["VP", "NP"], ["NP", "PropNoun"], ["NumP", "NP"], ["mengambil"], ["menghadiri"], ["mengikuti"], ["diperbolehkan"], ["mempunyai"],  ["bermain"], ["memasak"], ["belanja"], ["belajar"], ["menjaga"], ["terbang"], ["berenang"],["berlari"], ["bergelantungan"], ["melompat-lompat"], ["hinggap"], ["mengunyah"], ["mengumpulkan"], ["hadir"], ["berjemur"], ["memberikan"], ["berlibur"], ["merupakan"], ["adalah"],["menjadi"], ["membantu"], ["menaiki"], ["memiliki"], ["terkenal"], ["dikenal"], ["dilakukan"], ["digunakan"], ["terpajang"], ["tahap"], ["kontruksi"], ["sedang"], ["berisi"], ["membeli"], ["meneliti"], ["kursus"], ["menyukai"], ["disusun"], ["berlangsung"]] ,
    "O": [["NP", "AdjP"], ["NumP", "NP"], ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["daun"], ["ubi"], ["acara"],["kegiatan"],["pengabdian"], ["waktu"], ["makanan"], ["ketertiban"], ["tersebut"], ["rumput"], ["nektar"], ["kuliah"], ["tetangga"], ["pemandangan"],["alam"], ["rio"], ["de"], ["janeiro"], ["jawa"], ["bungkus"], ["rokok"], ["sejarah"], ["kebudayaan"], ["bali"], ["jepang"], ["medan"], ["kursi"], ["rotan"]],
    "Pel": [["NP", "AdjP"], ["NumP", "NP"], ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["VP", "NP"], ["VP", "AdjP"],["PP", "NP"], ["menaiki"], ["untuk"], ["penduduk"], ["desa"], ["dengan"], ["pemimpin"], ["proyek"], ["pemilik"], ["warung"], ["pakar"], ["bidang"], ["ekologi"], ["pembicara"], ["juara"], ["keindahan"], ["pantainya"], ["ikon"], ["rio"], ["de"], ["janeiro"], ["kulinernya"], ["hujan"], ["budaya"], ["terbesar"], ["menyambut"], ["tahun"], ["baru"], ["penghasil"], ["minyak"], ["negara"], ["kepulauan"], ["harus"], ["bahasa"], ["jepang"], ["pemain"], ["kebanggan"]],
    "Ket": [["PP", "NP"], ["Prep", "AdjP"], ["Adv", "AdjP"], ["Num", "NP"], ["di"], ["perpustakaan"], ["kampus"], ["taman"], ["kota"], ["jalan"], ["siang"], ["pagi"], ["malam"], ["hari"], ["kolam"], ["kebun"], ["lintasan"], ["pacu"], ["ranting"], ["pohon"], ["laut"], ["lepas"], ["bunga"], ["padang"], ["tepi"], ["danau"], ["universitas"], ["pantai"], ["dalam"], ["seminar"], ["pada"], ["lomba"], ["dunia"], ["jawa"], ["rak"], ["belakang"], ["rumah"], ["setiap"]],
    "NP": [["NP", "AdjP"], ["NumP", "NP"], ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["NP", "VP"],["nenek"], ["banyak"], ["sekitar"], ["lima"], ["tujuh"], ["puluh"], ["sepuluh"], ["dua"], ["tiga"], ["delapan"], ["belas"], ["mahasiswa"], ["orang"], ["pengunjung"], ["dewasa"], ["saja"], ["pemadam"], ["kebakaran"], ["anak"], ["laki-laki"], ["para"], ["siswa"], ["polisi"], ["burung"], ["merpati"], ["ikan"], ["koi"], ["perpustakaan"], ["kampus"], ["daun"], ["ubi"], ["acara"], ["pengabdian"], ["wahana"], ["sedikit"], ["waktu"], ["untuk"], ["penduduk"], ["desa"], ["taman"], ["kota"], ["makanan"], ["lezat"], ["ketertiban"], ["jalan"], ["siang"],["malam"], ["hari"], ["kolam"], ["kebun"], ["tersebut"], ["kuda"], ["pacuan"], ["lintasan"], ["pacu"], ["monyet"], ["ranting"], ["pohon"], ["kelinci"], ["putih"], ["lumba-lumba"], ["laut"], ["lepas"], ["kupu-kupu"], ["bunga"], ["sapi"], ["rumput"], ["padang"], ["lebah"], ["nektar"], ["seekor"], ["buaya"], ["tepi"], ["danau"], ["dr."], ["siti"], ["rahayu"], ["kuliah"], ["universitas"], ["ani"], ["pantai"], ["adi"], ["santoso"], ["pemimpin"], ["proyek"], ["bu"], ["ratna"],["pemilik"], ["warung"], ["prof."], ["hadi"], ["prayitno"], ["pakar"], ["bidang"], ["ekologi"], ["ibu"], ["sintia"], ["pembicara"], ["dalam"], ["seminar"], ["bapak"], ["haryono"], ["tetangga"],["kegiatan"], ["kiki"], ["juara"], ["pada"],["lomba"], ["menyanyi"], ["mediterania"], ["keindahan"], ["pantainya"], ["bukit"], ["tinggi"], ["pemandangan"],["alam"], ["indah"], ["baikal"], ["terindah"], ["dunia"], ["copacabana"], ["ikon"], ["rio"], ["de"], ["janeiro"], ["bali"] , ["medan"],["bogor"],["bandung"],["kulinernya"], ["hujan"], ["budaya"], ["denpasar"], ["surabaya"], ["jawa"], ["timur"], ["pentas"], ["ogoh-ogoh"], ["tahun"], ["baru"], ["saka"], ["arab"], ["saudi"], ["penghasil"], ["minyak"], ["negara"], ["indonesia"], ["kepulauan"], ["pasang"], ["sepatu"], ["rak"], ["buah"], ["tahap"], ["kontruksi"], ["ekor"], ["kucing"], ["belakang"], ["rumah"], ["kamar"], ["pertunjukan"], ["teater"], ["setiap"], ["mobil"], ["kotak"], ["mainan"], ["hitam"], ["dia"], ["buku"], ["bungkus"], ["rokok"], ["saya"], ["sejarah"], ["kebudayaan"],["teman"], ["bahasa"],["jepang"], ["asrama"], ["putri"], ["pemain"], ["sepak"], ["bola"], ["guru"], ["kakek"], ["kursi"], ["rotan"],["pelatih"], ["tari"], ["rencana"], ["perjalanan"], ["kita"], ["pengembangan"], ["teknologi"],["gadis"], ["boneka"], ["barunya"], ["air"], ["terjun"], ["pegunungan"], ["pertunjukan"], ["seni"], ["panjang"], ["yang"], ["mekar"], ["kebanggan"]] ,
    "VP": [["Prep", "NP"], ["Prep", "AdjP"], ["AdvP", "VP"], ["Adv","AdjP"], ["VP", "NP"], ["mengambil"], ["menghadiri"], ["mengikuti"], ["diperbolehkan"],["mempunyai"], ["bermain"], ["memasak"], ["belanja"], ["belajar"], ["menjaga"], ["terbang"], ["berenang"], ["menaiki"], ["menyelamatkan"],["berlari"], ["dengan"],  ["bergelantungan"], ["melompat-lompat"], ["hinggap"], ["mengunyah"], ["mengumpulkan"], ["hadir"], ["berjemur"], ["memberikan"], ["berlibur"], ["merupakan"], ["adalah"],  ["menjadi"], ["membantu"], ["menyanyi"], ["memiliki"], ["dikenal"], ["dilakukan"], ["digunakan"],["menyambut"], ["terpajang"], ["tidur"], ["harus"], ["disiram"], ["berisi"] , ["membeli"], ["meneliti"], ["kursus"], ["menyukai"], ["disusun"], ["berlangsung"]],
    "PP": [["PP", "NP"], ["Prep","AdjP"] , ["di"], ["dari"], ["perpustakaan"], ["kampus"], ["taman"], ["kota"], ["jalan"], ["siang"], ["setiap"], ["malam"],["hari"], ["kebun"], ["lintasan"], ["pacu"], ["bunga"], ["lomba"], ["dunia"], ["jawa"], ["timur"],["rak"], ["belakang"], ["rumah"],["pagi"]],
    "AdjP": [["Adv", "AdjP"], ["lezat"], ["cepat"], ["kecil"], ["terkenal"], ["indah"], ["terindah"], ["ramai"], ["terbesar"], ["baru"], ["nyaman"],["lama"], ["besar"], ["luas"], ["baik"], ["pesat"], ["senang"], ["barunya"] , ["menghibur"], ["tua"]],
    "AdvP": [["Adv", "AdvP"], ["hanya"], ["jarang"], ["sering"], ["selalu"], ["dengan"], ["sedang"], ["akan"], ["sangat"], ["harus"], ["sudah"]],
    "NumP": [["Num", "NumP"], ["NumP", "VP"], ["NP", "NumP"], ["lima"], ["tujuh"], ["puluh"],["sepuluh"], ["dua"],["tiga"],  ["delapan"], ["belas"], ["banyak"], ["sedikit"]],
    "PropNoun": [["merpati"], ["koi"], ["siti"], ["rahayu"], ["ani"], ["adi"], ["santoso"], ["ratna"],["hadi"], ["prayitno"], ["sintia"], ["haryono"], ["kiki"], ["mediterania"], ["bukit"], ["tinggi"], ["baikal"], ["copacabana"], ["rio"], ["de"], ["janeiro"], ["bali"], ["medan"], ["bandung"],["bogor"], ["denpasar"], ["surabaya"], ["jawa"], ["saka"], ["arab"], ["saudi"], ["indonesia"],  ["jepang"]],
    "Verb": [["mengambil"], ["menghadiri"], ["mengikuti"], ["diperbolehkan"], ["mempunyai"], ["bermain"], ["memasak"], ["belanja"], ["belajar"], ["menjaga"], ["terbang"], ["berenang"], ["menaiki"], ["menyelamatkan"], ["berlari"], ["bergelantungan"], ["melompat-lompat"], ["hinggap"], ["mengunyah"], ["mengumpulkan"], ["memberikan"], ["berlibur"], ["merupakan"], ["adalah"], ["membantu"], ["menyanyi"], ["memiliki"], ["dikenal"], ["dilakukan"], ["digunakan"],["menyambut"], ["terpajang"], ["tidur"], ["disiram"] , ["berisi"], ["membeli"], ["meneliti"], ["kursus"], ["menyukai"],  ["disusun"] , ["berlangsung"]],
    "Prep":[["di"], ["dari"], ["hadir"], ["berjemur"], ["menjadi"]],
    "Noun": [["nenek"], ["orang"], ["pengunjung"], ["sekitar"], ["mahasiswa"], ["dewasa"], ["saja"], ["pemadam"], ["kebakaran"], ["anak"], ["laki-laki"], ["para"], ["siswa"], ["polisi"], ["burung"], ["ikan"], ["perpustakaan"], ["kampus"], ["daun"],["ubi"], ["pengabdian"], ["wahana"], ["waktu"], ["untuk"], ["penduduk"], ["desa"], ["taman"], ["kota"], ["makanan"], ["jalan"], ["siang"] , ["setiap"], ["pagi"],["malam"],["hari"], ["kebun"], ["kuda"], ["pacuan"], ["lintasan"], ["pacu"], ["monyet"], ["ranting"], ["pohon"], ["kelinci"], ["putih"], ["lumba-lumba"], ["laut"], ["lepas"], ["kupu-kupu"], ["bunga"], ["sapi"], ["rumput"], ["padang"], ["lebah"], ["nektar"], ["acara"], ["seekor"], ["buaya"], ["tepi"], ["danau"],["dr."], ["kuliah"], ["universitas"], ["pantai"], ["pemimpin"], ["proyek"], ["bu"], ["pemilik"], ["warung"], ["prof."], ["pakar"], ["bidang"], ["ekologi"], ["ibu"], ["pembicara"], ["dalam"], ["seminar"], ["bapak"], ["tetangga"],["kegiatan"], ["juara"], ["pada"],["lomba"], ["keindahan"], ["pantainya"], ["pemandangan"],["alam"], ["dunia"], ["ikon"], ["kulinernya"], ["hujan"], ["budaya"], ["timur"], ["pentas"], ["ogoh-ogoh"], ["tahun"], ["penghasil"], ["minyak"], ["negara"], ["kepulauan"], ["pasang"], ["sepatu"], ["rak"], ["buah"], ["rumah"], ["tahap"], ["kontruksi"], ["ekor"], ["kucing"], ["belakang"], ["kamar"], ["pertunjukan"], ["teater"], ["mobil"], ["kotak"] , ["mainan"], ["hitam"] , ["buku"], ["bungkus"], ["rokok"], ["sejarah"], ["kebudayaan"], ["teman"], ["bahasa"], ["asrama"], ["putri"], ["pemain"], ["sepak"], ["bola"], ["guru"], ["kakek"], ["kursi"], ["rotan"],["pelatih"], ["tari"], ["rencana"], ["perjalanan"], ["pengembangan"], ["teknologi"], ["gadis"], ["boneka"] , ["air"], ["terjun"], ["pegunungan"], ["pertunjukan"], ["seni"], ["panjang"], ["yang"], ["mekar"], ["kebanggan"]],
    "Adv" : [["hanya"], ["jarang"], ["sering"], ["ketertiban"], ["kolam"], ["selalu"], ["dengan"], ["sedang"], ["akan"], ["sangat"], ["harus"], ["sudah"]],
    "Adj" : [["lezat"], ["cepat"], ["kecil"], ["terkenal"], ["indah"], ["terindah"], ["ramai"], ["terbesar"], ["baru"], ["nyaman"], ["lama"] , ["besar"], ["luas"], ["baik"], ["pesat"], ["senang"], ["barunya"], ["menghibur"], ["tua"]],
    "Pronoun":[["itu"], ["ini"], ["tersebut"], ["dia"], ["saya"], ["kita"]],
    "Num": [["lima"],["tujuh"], ["puluh"], ["sepuluh"], ["dua"], ["tiga"], ["delapan"],["belas"], ["banyak"], ["sedikit"]],
}