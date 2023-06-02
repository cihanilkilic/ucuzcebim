class Items:
    def __init__(self):
        self.os = sorted({"ANDROİD", "IOS"})
        self.memory_memory = sorted(
    {"1GB", "2GB", "4GB", "8GB", "16GB", "32GB", "64GB", "128GB", "256GB", "512GB", "1TB"},
    key=lambda x: (
        float('inf') if x == '1TB' else float(x[:-2]),
        x[-2:]
    )
)

        self.ram_memory = sorted({"512MB", "1GB", "2GB", "3GB", "4GB", "6GB", "8GB", "12GB", "16GB"}, 
        key=lambda x: (int(x[:-2]) if x.endswith("GB") else 0, 
        int(x[:-2]) if x.endswith("MB") else 0))
        
        self.situation = {"SIFIR", "İKİNCİ EL"}
        self.garanti = {"DİSTRİBÜTÖR GARANTİLİ", "İTHALATÇI GARANTİLİ", "GARANTİSİ YOK"}
        self.swap = {"EVET", "HAYIR"}


# Örnek kullanım
# items = Items()
# print(items.os)
# print(items.ram_memory)
# print(items.memory)
# print(items.situation)
# print(items.garanti)
# print(items.swap)
