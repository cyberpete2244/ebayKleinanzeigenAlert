from ebayAlert.core.configs import configs


class Settings:

    TELEGRAM_API_URL = "https://api.telegram.org/bot{bottoken}/sendMessage?chat_id={chat_id}&parse_mode=HTML&"

    KLEIN_URL_BASE = "https://www.kleinanzeigen.de"
    EBAY_BASE_ITEM = "https://www.ebay.de/itm/"

    URL_TYPE_GPU = "/s-pc-zubehoer-software/grafikkarten/anbieter:privat/anzeige:angebote/{NPAGE}{" \
                   "SEARCH_TERM}k0c225+pc_zubehoer_software.art_s:grafikkarten"
    URL_TYPE_HIFI = "/s-audio-hifi/anbieter:privat/{NPAGE}{SEARCH_TERM}k0c172"
    URL_TYPE_IPHONE = "/s-handy-telekom/apple/anbieter:privat/anzeige:angebote/{NPAGE}{" \
                      "SEARCH_TERM}k0c173+handy_telekom.art_s:apple+handy_telekom.condition_s:condition_used"
    URL_TYPE_MONITOR = "/s-pc-zubehoer-software/monitore/anbieter:privat/anzeige:angebote/{NPAGE}{" \
                       "SEARCH_TERM}k0c225+pc_zubehoer_software.art_s:monitore"
    URL_TYPE_CPU = "/s-pc-zubehoer-software/prozessor_cpu/anbieter:privat/anzeige:angebote/{NPAGE}{" \
                       "SEARCH_TERM}k0c225+pc_zubehoer_software.art_s:prozessor_cpu"
    URL_TYPE_MEMORY = "/s-pc-zubehoer-software/speicher/anbieter:privat/anzeige:angebote/{NPAGE}{" \
                       "SEARCH_TERM}k0c225+pc_zubehoer_software.art_s:speicher"
    URL_TYPE_TOYS = "/s-spielzeug/anbieter:privat/anzeige:angebote/{NPAGE}{" \
                       "SEARCH_TERM}k0c23"


settings = Settings()