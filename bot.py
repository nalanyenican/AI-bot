import discord
from discord.ext import commands
import os
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def analiz(ctx):
    if ctx.message.attachments :
        for attachment in  ctx.message.attachments :
            file_name = attachment.filename 
            file_path = os.path.join(IMAGE_DIR, file_name)
            await attachment.save(file_path)
            await ctx.send("Görselinizi basariyla kaydettik :))")
            class_name, score= get_class(file_path)
            await ctx.send(f"Görselinizin sinifi : {class_name}, ve tahmin puani:{score:.0%}")
           information = {
    "gul": (
        "Güller, güneşi seven ve iyi toprakta yetişen çok yıllık bitkilerdir. "
        "Asya, Avrupa ve Orta Doğu'da yaygın olarak bulunurlar. Türkiye'de özellikle Isparta, gülleriyle ünlüdür.\n\n"
        "Güller binlerce yıldır güzellik, sevgi ve zarafetin sembolü olarak görülür. "
        "Kırmızı gül aşkı, beyaz gül saflığı, pembe gül şefkati, sarı gül ise dostluğu temsil eder. "
        "Gövdelerinde kendilerini koruyan küçük ve sivri dikenler bulunur.\n\n"
        "Efsanesi:\n"
        "Antik Yunan efsanesine göre Afrodit'in sevdiği Adonis yaralandığında, onun kanından kırmızı güller doğmuştur. "
        "Bu yüzden kırmızı gül, aşkın, tutkunun ve fedakarlığın sembolü olarak kabul edilir. 🌹"
    ),
    "papatya": (
        "Papatyalar, güneşi seven ve genellikle çayırlarda, tarlalarda ve yol kenarlarında yetişen narin çiçeklerdir. "
        "Avrupa, Asya ve Kuzey Amerika'nın birçok bölgesinde bulunurlar. İlkbahar ve yaz aylarında sıkça açarlar.\n\n"
        "Papatya, saflığın, masumiyetin, sadakatin ve umudun sembolüdür. "
        "Beyaz yaprakları ve sarı ortasıyla sadeliği ve doğallığı temsil eder.\n\n"
        "Efsanesi:\n"
        "Eski bir inanışa göre, sevdiğinin kendisini sevip sevmediğini merak eden kişi bir papatyanın yapraklarını tek tek koparır. "
        "Her yaprakta 'seviyor' ve 'sevmiyor' denir. Son yaprakta çıkan cevap, kişinin aşkının kaderini belirler. "
        "Bu yüzden papatya, aşkın ve umut dolu bekleyişin sembolü olarak görülür. 🌼"
    ),
    "lilyum": (
        "Lilyumlar, güneşi veya hafif gölgeyi seven soğanlı çiçeklerdir. "
        "Avrupa, Asya ve Kuzey Amerika'nın birçok bölgesinde yetişirler. "
        "Yaz aylarında açar ve güzel kokularıyla dikkat çekerler.\n\n"
        "Lilyum, saflığın, zarafetin, yenilenmenin ve umudun sembolüdür. "
        "Özellikle beyaz lilyum, temizliği ve masumiyeti temsil eder.\n\n"
        "Efsanesi:\n"
        "Eski inanışlara göre lilyum, her yıl yeniden açtığı için 'ölümsüzlüğün çiçeği' olarak görülmüştür. "
        "Yeniden açması, yaşamın devamını ve yeniden doğuşu simgeler. 🌸"
    ),
    "yasemin": (
        "Yasemin, sıcak iklimleri seven ve çoğunlukla bahçelerde, duvar kenarlarında yetişen güzel kokulu bir çiçektir."
        "Özellikle geceleri daha yoğun kokmasıyla bilinir."
        "Asya, Avrupa ve Orta Doğu’da yaygın olarak yetişir.\n\n"
        "Yasemin, sevginin, zarafetin, mutluluğun ve saflığın sembolüdür."
        "Beyaz çiçekleri temizliği ve masumiyeti temsil eder.\n\n"
        "Efsanesi:\n"
        "Güney Asya’daki eski inanışlarda yasemin, düğünlerde ve özel törenlerde kullanılırdı."
        "Bu yüzden mutluluğu, sevgiyi ve yeni başlangıçları simgeleyen özel bir çiçek olarak kabul edilmiştir. 🌿"

    ),
    "lale": (
        "Laleler, ilkbaharda açan ve güneşli yerleri seven soğanlı çiçeklerdir."
        "İyi drene olan topraklarda yetişirler."
        "Asya’dan Avrupa’ya kadar birçok bölgede yetişirler."
        "Türkiye ve Hollanda laleleriyle ünlüdür.\n\n"
        "Lale, aşkın, güzelliğin, zarafetin ve umudun sembolüdür."
        "Kırmızı lale özellikle güçlü aşkı ve tutkuyu temsil eder.\n\n"
        "Efsanesi:\n"
        "Lale, Osmanlı kültüründe güzellik ve zarafetin önemli bir sembolüydü."
        "Özellikle Lale Devri, adını bu çiçekten almıştır."
    ),
    "lavanta": (
        "Lavanta, güneşi ve sıcak havayı seven, fazla suya ihtiyaç duymayan dayanıklı bir bitkidir."
        "Mor çiçekleri ve güzel kokusuyla dikkat çeker.\n\n"
        "Lavanta, huzurun, sakinliğin, saflığın ve sevginin sembolüdür."
        "Mor rengi zarafeti ve dinginliği temsil eder.\n\n"
        "Efsanesi:\n"
        "Eski Akdeniz inanışlarında lavantanın kokusunun kötü düşünceleri uzaklaştırdığına ve insanın içini sakinleştirdiğine inanılırdı. "
        "Bu nedenle lavanta, huzurun, arınmanın ve içsel dinginliğin sembolü olarak kabul edilmiştir."
    ),
    "gelincik": (
        "Gelincikler, güneşi seven ve genellikle tarlalarda, çayırlarda ve yol kenarlarında yetişen narin çiçeklerdir."
        "İlkbahar ve yaz aylarında açarlar."  
        "Kırmızı, ince ve zarif yapraklarıyla dikkat çekerler.\n\n"
        "Gelincik, huzurun, uykunun, hatırlamanın ve umudun sembolüdür."
        "Özellikle kırmızı gelincik, güçlü duyguları ve yaşamın geçiciliğini temsil eder.\n\n"
        "Efsanesi:\n"
        "Antik Yunan’da gelincik, uyku ve huzurla ilişkilendirilirdi."
        "Özellikle kırmızı gelincik, sakinlik ve dinlenmenin sembolü olarak görülürdü."
        "Bu nedenle gelincik, huzuru ve dinginliği hatırlatan özel bir çiçek kabul edilmiştir."
    )
}
        info = information.get(class_name)
        await ctx.send(info)
           
    else: 
        await ctx.send("Lütfen görsel gönderiniz")


bot.run("")