from flet import *

def main(page: Page):
    page.padding = 0
    page.scroll = ScrollMode.ALWAYS

    vocabulary_button = ElevatedButton(
        "Vocabulary/Kelime Bilgisi Çöz 📖",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    gramer_button = ElevatedButton(
        "Grammar/Dil Bilgisi Çöz ✍️",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    cloze_button = ElevatedButton(
        "Cloze Test Çöz 📝",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    tamamlama_button = ElevatedButton(
        "Cümle Tamamlama Çöz 🧩",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    engtr_button = ElevatedButton(
        "İngilizce - Türkçe Çeviri Çöz 🇬🇧 ➔ 🇹🇷",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    treng_button = ElevatedButton(
        "Türkçe - İngilizce Çeviri Çöz 🇹🇷 ➔ 🇬🇧",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    paragraph_button = ElevatedButton(
        "Paragraf Çöz 📚",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    diyalog_button = ElevatedButton(
        "Diyalog Tamamlama Çöz 👥",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    esanlam_button = ElevatedButton(
        "Eş Anlamlı Cümle/Restatement Çöz ⚖️",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    durum_button = ElevatedButton(
        "Durum Soruları Çöz 👥",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    paragraftamam_button = ElevatedButton(
        "Paragraf Tamamlama Çöz 🧱",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    irrevelant_button = ElevatedButton(
        "Anlamı Bozan Cümle/Irrevelant Çöz 🕵️‍♂️",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    deneme_button = ElevatedButton(
        "Deneme Çöz ⏰",
        width=page.width * 0.8,
        style=ButtonStyle(
            bgcolor="#b65f0d",
            color="#FFFFFF",
            side=BorderSide(width=2, color="#FEF1A8"),
        )
    )

    logo = Image(
        src="/logo.png",
        width=page.width * 0.7
    )

    motto_text = Text(
        "YDT Soru Generatörü",
        color="#FFFFFF",
        font_family="Roboto",
        size=page.width * 0.02,
    )

    mainscreen = Container(
        width=page.width,
        height=page.height,
        bgcolor="#fba04d",
        content=Column(
            controls=[
                logo,
                motto_text,
                vocabulary_button,
                gramer_button,
                cloze_button,
                tamamlama_button,
                engtr_button,
                treng_button,
                paragraph_button,
                diyalog_button,
                esanlam_button,
                durum_button,
                paragraftamam_button,
                irrevelant_button,
                deneme_button
            ],
         horizontal_alignment=CrossAxisAlignment.CENTER,
         alignment=alignment.Alignment(0, -1),
         spacing=0.1
        ),
        #content=Text("Dilio",size=100,color="#FFFFFF",weight=FontWeight.W_500,text_align=TextAlign.JUSTIFY)
    )

    page.add(
        Column(
            controls=[mainscreen],
            expand=True
    ))

if __name__ == "__main__":
    app(target=main)