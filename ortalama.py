def ortalama(notlar: list[float]) -> float:
    """Not listesinin aritmetik ortalamasını döndürür."""
    if not notlar:
        raise ValueError("Not listesi boş olamaz")
    return sum(notlar) / len(notlar)


if __name__ == "__main__":
        print(f"Ortalama: {ortalama([70, 85, 90]):.2f}")