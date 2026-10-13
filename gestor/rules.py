"""Static catalogs: VAT treatments of sales, expense categories, countries, currencies, regions, visas."""
from .i18n import N_

EU = {"AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "EL", "GR", "ES", "FI", "FR", "HR", "HU", "IE",
      "IT", "LT", "LU", "LV", "MT", "NL", "PL", "PT", "RO", "SE", "SI", "SK"}

# Invoice currencies: EUR plus every currency with an ECB euro reference rate (data-api.ecb.europa.eu, EXR, checked
# 08.10.2026). Art. 79.Once LIVA allows the ECB rate, so gestor can convert each of them on its own.
CURRENCIES = {
    "EUR": N_("евро"), "USD": N_("доллар США"), "GBP": N_("фунт стерлингов"), "CHF": N_("швейцарский франк"),
    "AUD": N_("австралийский доллар"), "BRL": N_("бразильский реал"), "CAD": N_("канадский доллар"), "CNY": N_("китайский юань"),
    "CZK": N_("чешская крона"), "DKK": N_("датская крона"), "HKD": N_("гонконгский доллар"), "HUF": N_("венгерский форинт"),
    "IDR": N_("индонезийская рупия"), "ILS": N_("израильский шекель"), "INR": N_("индийская рупия"), "ISK": N_("исландская крона"),
    "JPY": N_("японская иена"), "KRW": N_("южнокорейская вона"), "MXN": N_("мексиканское песо"), "MYR": N_("малайзийский ринггит"),
    "NOK": N_("норвежская крона"), "NZD": N_("новозеландский доллар"), "PHP": N_("филиппинское песо"), "PLN": N_("польский злотый"),
    "RON": N_("румынский лей"), "SEK": N_("шведская крона"), "SGD": N_("сингапурский доллар"), "THB": N_("тайский бат"),
    "TRY": N_("турецкая лира"), "ZAR": N_("южноафриканский рэнд"),
}

# Sales VAT treatment. `vat`: default IVA rate; `mention`: legal text printed on the invoice.
TREATMENTS = {
    "es_b2b": {
        "label": N_("Испания, бизнес (IVA + retención)"),
        "vat": 21, "mention": "", "sources": ["liva-90", "lirpf-101"],
    },
    "es_b2c": {
        "label": N_("Испания, частное лицо (IVA)"),
        "vat": 21, "mention": "", "sources": ["liva-90"],
    },
    "eu_b2b": {
        "label": N_("ЕС, бизнес (inversión del sujeto pasivo)"),
        "vat": 0,
        "mention": "Operación no sujeta al IVA español (art. 69.Uno.1º Ley 37/1992). "
                   "Inversión del sujeto pasivo / Reverse charge — art. 196 Directiva 2006/112/CE.",
        "sources": ["liva-69", "dir2006-196", "rd1619-6", "riva-79"],
    },
    "eu_b2c": {
        "label": N_("ЕС, частное лицо (IVA Испании до порога OSS 10 000 €)"),
        "vat": 21, "mention": "", "sources": ["liva-69", "liva-90"],
    },
    "extra_eu": {
        "label": N_("Вне ЕС (no sujeta, reglas de localización)"),
        "vat": 0,
        "mention": "Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE). "
                   "Not subject to Spanish VAT — place of supply outside Spain.",
        "sources": ["liva-69", "rd1619-2", "liva-94"],
    },
}

VISAS = {
    "emprendedor": N_("Виза предпринимателя (Ley 14/2013, art. 70)"),
    "nomada_digital": N_("Виза цифрового кочевника (teletrabajo internacional)"),
    "cuenta_propia": N_("ВНЖ cuenta propia (Reglamento de Extranjería)"),
    "none": N_("Гражданин ЕС / без ограничений"),
}
VISA_SOURCES = {
    "emprendedor": ["ley14-2013-69", "ley14-2013-70", "rirpf-113"],
    "nomada_digital": ["ley14-2013-74bis", "ley14-2013-74quater", "ley14-2013-74quinquies"],
    "cuenta_propia": ["rd1155-2024-83", "rd1155-2024-86", "rd1155-2024-87"],
    "none": ["lirpf-9"],
}

REGIONS = {"valencia": "Comunitat Valenciana", "asturias": "Principado de Asturias", "madrid": "Comunidad de Madrid",
           "cataluna": "Cataluña", "andalucia": "Andalucía", "other": N_("Другой регион (государственная шкала ×2)")}

# Expense categories. `irpf`: default % deductible for income tax; `vat`: default % of input VAT deductible.
EXPENSE_CATEGORIES = {
    "reta": {"label": N_("Cuota RETA (соцстрах)"), "irpf": 100, "vat": 0, "sources": ["lirpf-30-reta"]},
    "gestoria": {"label": N_("Gestoría / asesoría / софт для учёта"), "irpf": 100, "vat": 100, "sources": ["lirpf-28", "liva-94", "liva-97"]},
    "software": {"label": N_("Софт, SaaS, хостинг"), "irpf": 100, "vat": 100, "sources": ["lirpf-28", "liva-94", "liva-84"]},
    "equipment": {"label": N_("Техника (≤300 € — сразу; дороже — амортизация)"), "irpf": 100, "vat": 100,
                  "sources": ["amort-simplificada", "lis-12", "liva-108"]},
    "office": {"label": N_("Канцтовары, мелочи для работы"), "irpf": 100, "vat": 100, "sources": ["lirpf-28", "liva-94"]},
    "phone": {"label": N_("Телефон и интернет (только рабочая линия)"), "irpf": 100, "vat": 100, "sources": ["lirpf-28", "liva-95"]},
    "home": {"label": N_("Коммуналка дома (30% × доля площади)"), "irpf": 0, "vat": 0,
             "sources": ["lirpf-30", "liva-95", "irpf-dgt-v2548-18"]},
    "rent": {"label": N_("Аренда офиса / коворкинг (у аренды помещения — retención 19 %)"), "irpf": 100, "vat": 100,
             "sources": ["lirpf-28", "rirpf-75", "rirpf-100"]},
    "travel": {"label": N_("Командировки: транспорт, отель"), "irpf": 100, "vat": 100, "sources": ["lirpf-28", "liva-96"]},
    "meals": {"label": N_("Питание в поездках: укажите % в пределах 26,67 €/день (53,34 € с ночёвкой; за рубежом 48,08/91,35 €)"),
              "irpf": 0, "vat": 100, "sources": ["lirpf-30", "irpf-rirpf-9", "liva-96"]},
    "training": {"label": N_("Обучение, книги, конференции"), "irpf": 100, "vat": 100, "sources": ["lirpf-28", "liva-94"]},
    "health": {"label": N_("Медстраховка autónomo (вычет до 500 €/год)"), "irpf": 100, "vat": 0, "sources": ["lirpf-30"]},
    "insurance": {"label": N_("Страховки бизнеса (RC и т.п.)"), "irpf": 100, "vat": 0, "sources": ["lirpf-28"]},
    "bank": {"label": N_("Банковские комиссии"), "irpf": 100, "vat": 0, "sources": ["lirpf-28"]},
    "admin_pay": {"label": N_("SL: вознаграждение administrador (брутто)"), "irpf": 100, "vat": 0, "sources": ["rirpf-80", "lis-15"]},
    "taxes": {"label": N_("Пошлины и налоги, связанные с деятельностью"), "irpf": 100, "vat": 0, "sources": ["lirpf-28"]},
    "marketing": {"label": N_("Реклама, домены, маркетинг"), "irpf": 100, "vat": 100, "sources": ["lirpf-28", "liva-94"]},
    "other": {"label": N_("Прочее для деятельности"), "irpf": 100, "vat": 100, "sources": ["lirpf-28", "liva-94", "liva-97"]},
    "personal": {"label": N_("Не вычитается (только для учёта)"), "irpf": 0, "vat": 0, "sources": []},
}

VAT_KINDS = {
    "domestic": N_("Испанский IVA в чеке"),
    "reverse_eu": N_("Поставщик из ЕС без IVA (autorrepercusión)"),
    "reverse_non_eu": N_("Поставщик вне ЕС без IVA (autorrepercusión)"),
    "none": N_("Без IVA (exento / не облагается)"),
}
VAT_KIND_SOURCES = {"domestic": ["liva-94", "liva-97"], "reverse_eu": ["liva-84", "riva-79"], "reverse_non_eu": ["liva-84"],
                    "none": []}


def suggest_treatment(client) -> str:
    country = (client["country"] or "ES").upper()
    if country == "ES":
        return "es_b2b" if client["is_business"] else "es_b2c"
    if country in EU:
        return "eu_b2b" if client["is_business"] else "eu_b2c"
    return "extra_eu"


def suggest_irpf_rate(treatment: str, settings: dict, regime: str, year: int) -> float:
    """Retención only when an autónomo profesional invoices a Spanish business client:
    general IRPF 15 % (7 % in the start year and the next two), Beckham 24 % (IRNR rules, art. 114 RIRPF)."""
    if treatment != "es_b2b" or regime == "sl" or settings.get("activity_kind") == "empresarial":
        return 0
    if regime == "beckham":
        return 24
    start = (settings.get("activity_start") or "")[:4]
    return 7 if settings["new_activity_irpf_7"] and start.isdigit() and year <= int(start) + 2 else 15
