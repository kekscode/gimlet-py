import blog

b = blog.BlogDB()
b.create_article(title="Sony Alpha 7 II im Test",
                 subtitle="Fast ins Schwarze getroffen",
                 body="Durch einen überarbeiteten Autofokus und einen beweglich aufgehängten Sensor soll Sonys Vollformat-Systemkamera Alpha 7 II glänzen. Ob das wirklich Vorteile bringt und wie es um die Bildqualität und die Bedienung steht, zeigt der Golem.de-Test.")

b.create_article(title="Lieferprobleme",
                 subtitle="Drogendrohnen in Mexiko und Norddeutschland abgestürzt",
                 body="Amazon will die Paketlieferung mit Drohnen revolutionieren - doch Versuche des organisierten Verbrechens zeigen, welche Probleme und Gefahren mit dieser Art der Lieferung verbunden sind.")

b.create_article(title="Raumfahrt",
                 subtitle="Nasa will Mars-Rover mit Helikopter ausstatten",
                 body="Künftig könnten Helikopter Mars-Rover begleiten und Bilder von fernen Planeten machen. Die Nasa testet Flugobjekte zur Erkundung der Marsoberfläche - und steht dabei vor einigen Herausforderungen.")

