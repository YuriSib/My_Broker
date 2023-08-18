from bs4 import BeautifulSoup

html = """<tbody class="ui-sortable" id="tbody_overview_45552930">
<tr data-is-open-by="exchange" data-is-pair-exchange-open="1" data-pair-exchange-id="40" data-pair-id="13716" id="sort_13716" rel="45552930_13716">
<td class="left dragHandle"><span class="checkers"></span></td>
<td class="flag"><span class="ceFlags Russian_Federation" title="Россия"> </span></td>
<td class="symbol plusIconTd left bold elp alert js-injected-user-alert-container" data-column-name="name" data-pair-id="13716">
<span class="aqPopupWrapper js-hover-me-wrapper"><a class="aqlink js-hover-me" data-pairid="13716" hoverme="markets" href="/equities/surgutneftegas_rts" target="_blank" title="Сургутнефтегаз ПАО">Сургутнефтегаз</a></span>
<span class="js-plus-icon alertBellGrayPlus genToolTip oneliner" data-tooltip="Создать уведомление" data-tooltip-alt="Уведомление активно"></span>
</td>
<td class="left bold" data-column-name="symbol"><a href="/equities/surgutneftegas_rts" target="_blank" title="SNGS">SNGS</a></td>
<td class="left displayNone" data-column-name="exchange" title="Москва">MCX</td>
<td class="pid-13716-last" data-column-name="last" id="45552930_last_13716">30,380</td>
<td class="pid-13716-bid displayNone" data-column-name="bid" id="45552930_bid_13716">30,375</td>
<td class="pid-13716-ask displayNone" data-column-name="ask" id="45552930_ask_13716">30,380</td>
<td class="js-extended-hours js-extended-last Font pidExt-13716-last displayNone" data-column-name="extended_hours">--</td>
<td class="js-extended-hours js-extended-percent Font pidExt-13716-pcp displayNone" data-column-name="extended_hours_percent">--</td>
<td class="" data-column-name="open">30,520</td>
<td class="displayNone" data-column-name="prev">30,280</td>
<td class="pid-13716-high" data-column-name="high" id="45552930_high_13716">30,720</td>
<td class="pid-13716-low" data-column-name="low" id="45552930_low_13716">29,905</td>
<td class="bold greenFont pid-13716-pc" data-column-name="chg" id="45552930_chg_13716">+0,000</td>
<td class="bold greenFont pid-13716-pcp" data-column-name="chgpercent" id="45552930_p_chg_13716">+0,00%</td>
<td class="pid-13716-turnover" data-column-name="vol" data-value="0">-</td>
<td class="left textNum displayNone" data-column-name="next_earning" data-value="1698364800">27.10.2023</td>
<td class="pid-13716-time" data-column-name="time" data-value="1692305397" id="45552930_time_13716">17/08</td>
<td class="icon" id="45552930_isopen_13716"><span class="greenClockIcon middle isOpenExch-40"></span></td>
<td class="icon"><a class="bugCloseIcon genToolTip oneliner" data-pair-id="13716" data-portfolio-id="45552930" data-tooltip="Удалить" href="javascript:void(0)" rel="removePairFromPortfolio_45552930"> </a></td>
</tr><tr data-is-open-by="exchange" data-is-pair-exchange-open="1" data-pair-exchange-id="40" data-pair-id="13707" id="sort_13707" rel="45552930_13707">
<td class="left dragHandle"><span class="checkers"></span></td>
<td class="flag"><span class="ceFlags Russian_Federation" title="Россия"> </span></td>
<td class="symbol plusIconTd left bold elp alert js-injected-user-alert-container" data-column-name="name" data-pair-id="13707">
<span class="aqPopupWrapper js-hover-me-wrapper"><a class="aqlink js-hover-me" data-pairid="13707" hoverme="markets" href="/equities/rosneft_rts" target="_blank" title="Роснефть">Роснефть</a></span>
<span class="js-plus-icon alertBellGrayPlus genToolTip oneliner" data-tooltip="Создать уведомление" data-tooltip-alt="Уведомление активно"></span>
</td>
<td class="left bold" data-column-name="symbol"><a href="/equities/rosneft_rts" target="_blank" title="ROSN">ROSN</a></td>
<td class="left displayNone" data-column-name="exchange" title="Москва">MCX</td>
<td class="pid-13707-last" data-column-name="last" id="45552930_last_13707">544,45</td>
<td class="pid-13707-bid displayNone" data-column-name="bid" id="45552930_bid_13707">544,45</td>
<td class="pid-13707-ask displayNone" data-column-name="ask" id="45552930_ask_13707">544,60</td>
<td class="js-extended-hours js-extended-last Font pidExt-13707-last displayNone" data-column-name="extended_hours">--</td>
<td class="js-extended-hours js-extended-percent Font pidExt-13707-pcp displayNone" data-column-name="extended_hours_percent">--</td>
<td class="" data-column-name="open">539,00</td>
<td class="displayNone" data-column-name="prev">532,50</td>
<td class="pid-13707-high" data-column-name="high" id="45552930_high_13707">544,90</td>
<td class="pid-13707-low" data-column-name="low" id="45552930_low_13707">532,00</td>
<td class="bold greenFont pid-13707-pc" data-column-name="chg" id="45552930_chg_13707">+0,00</td>
<td class="bold greenFont pid-13707-pcp" data-column-name="chgpercent" id="45552930_p_chg_13707">+0,00%</td>
<td class="pid-13707-turnover" data-column-name="vol" data-value="0">-</td>
<td class="left textNum displayNone" data-column-name="next_earning" data-value="1699574400">10.11.2023</td>
<td class="pid-13707-time" data-column-name="time" data-value="1692305396" id="45552930_time_13707">17/08</td>
<td class="icon" id="45552930_isopen_13707"><span class="greenClockIcon middle isOpenExch-40"></span></td>
<td class="icon"><a class="bugCloseIcon genToolTip oneliner" data-pair-id="13707" data-portfolio-id="45552930" data-tooltip="Удалить" href="javascript:void(0)" rel="removePairFromPortfolio_45552930"> </a></td>
</tr><tr data-is-open-by="exchange" data-is-pair-exchange-open="1" data-pair-exchange-id="40" data-pair-id="13683" id="sort_13683" rel="45552930_13683">
<td class="left dragHandle"><span class="checkers"></span></td>
<td class="flag"><span class="ceFlags Russian_Federation" title="Россия"> </span></td>
<td class="symbol plusIconTd left bold elp alert js-injected-user-alert-container" data-column-name="name" data-pair-id="13683">
<span class="aqPopupWrapper js-hover-me-wrapper"><a class="aqlink js-hover-me" data-pairid="13683" hoverme="markets" href="/equities/gmk-noril-nickel_rts" target="_blank" title="ГМК Норильский Никель ПАО">Норникель</a></span>
<span class="js-plus-icon alertBellGrayPlus genToolTip oneliner" data-tooltip="Создать уведомление" data-tooltip-alt="Уведомление активно"></span>
</td>
<td class="left bold" data-column-name="symbol"><a href="/equities/gmk-noril-nickel_rts" target="_blank" title="GMKN">GMKN</a></td>
<td class="left displayNone" data-column-name="exchange" title="Москва">MCX</td>
<td class="pid-13683-last" data-column-name="last" id="45552930_last_13683">15.924,0</td>
<td class="pid-13683-bid displayNone" data-column-name="bid" id="45552930_bid_13683">15,916.0</td>
<td class="pid-13683-ask displayNone" data-column-name="ask" id="45552930_ask_13683">15,930.0</td>
<td class="js-extended-hours js-extended-last Font pidExt-13683-last displayNone" data-column-name="extended_hours">--</td>
<td class="js-extended-hours js-extended-percent Font pidExt-13683-pcp displayNone" data-column-name="extended_hours_percent">--</td>
<td class="" data-column-name="open">16.000,0</td>
<td class="displayNone" data-column-name="prev">15.948,0</td>
<td class="pid-13683-high" data-column-name="high" id="45552930_high_13683">16.098,0</td>
<td class="pid-13683-low" data-column-name="low" id="45552930_low_13683">15.700,0</td>
<td class="bold greenFont pid-13683-pc" data-column-name="chg" id="45552930_chg_13683">+0,0</td>
<td class="bold greenFont pid-13683-pcp" data-column-name="chgpercent" id="45552930_p_chg_13683">+0,00%</td>
<td class="pid-13683-turnover" data-column-name="vol" data-value="0">-</td>
<td class="left textNum displayNone" data-column-name="next_earning" data-value="1698796800">01.11.2023</td>
<td class="pid-13683-time" data-column-name="time" data-value="1692305397" id="45552930_time_13683"></td>
<td class="icon" id="45552930_isopen_13683"><span class="greenClockIcon middle isOpenExch-40"></span></td>
<td class="icon"><a class="bugCloseIcon genToolTip oneliner" data-pair-id="13683" data-portfolio-id="45552930" data-tooltip="Удалить" href="javascript:void(0)" rel="removePairFromPortfolio_45552930"> </a></td>
</tr><tr data-is-open-by="exchange" data-is-pair-exchange-open="1" data-pair-exchange-id="40" data-pair-id="13711" id="sort_13711" rel="45552930_13711">
<td class="left dragHandle"><span class="checkers"></span></td>
<td class="flag"><span class="ceFlags Russian_Federation" title="Россия"> </span></td>
<td class="symbol plusIconTd left bold elp alert js-injected-user-alert-container" data-column-name="name" data-pair-id="13711">
<span class="aqPopupWrapper js-hover-me-wrapper"><a class="aqlink js-hover-me" data-pairid="13711" hoverme="markets" href="/equities/sberbank_rts" target="_blank" title="Сбербанк ПАО">Сбербанк</a></span>
<span class="js-plus-icon alertBellGrayPlus genToolTip oneliner" data-tooltip="Создать уведомление" data-tooltip-alt="Уведомление активно"></span>
</td>
<td class="left bold" data-column-name="symbol"><a href="/equities/sberbank_rts" target="_blank" title="SBER">SBER</a></td>
<td class="left displayNone" data-column-name="exchange" title="Москва">MCX</td>
<td class="pid-13711-last" data-column-name="last" id="45552930_last_13711">258,50</td>
<td class="pid-13711-bid displayNone" data-column-name="bid" id="45552930_bid_13711">258,47</td>
<td class="pid-13711-ask displayNone" data-column-name="ask" id="45552930_ask_13711">258,50</td>
<td class="js-extended-hours js-extended-last Font pidExt-13711-last displayNone" data-column-name="extended_hours">--</td>
<td class="js-extended-hours js-extended-percent Font pidExt-13711-pcp displayNone" data-column-name="extended_hours_percent">--</td>
<td class="" data-column-name="open">257,15</td>
<td class="displayNone" data-column-name="prev">256,61</td>
<td class="pid-13711-high" data-column-name="high" id="45552930_high_13711">258,80</td>
<td class="pid-13711-low" data-column-name="low" id="45552930_low_13711">255,50</td>
<td class="bold greenFont pid-13711-pc" data-column-name="chg" id="45552930_chg_13711">+0,00</td>
<td class="bold greenFont pid-13711-pcp" data-column-name="chgpercent" id="45552930_p_chg_13711">+0,00%</td>
<td class="pid-13711-turnover" data-column-name="vol" data-value="0">-</td>
<td class="left textNum displayNone" data-column-name="next_earning" data-value="1698883200">02.11.2023</td>
<td class="pid-13711-time" data-column-name="time" data-value="1692305398" id="45552930_time_13711">17/08</td>
<td class="icon" id="45552930_isopen_13711"><span class="greenClockIcon middle isOpenExch-40"></span></td>
<td class="icon"><a class="bugCloseIcon genToolTip oneliner" data-pair-id="13711" data-portfolio-id="45552930" data-tooltip="Удалить" href="javascript:void(0)" rel="removePairFromPortfolio_45552930"> </a></td>
</tr><tr data-is-open-by="exchange" data-is-pair-exchange-open="1" data-pair-exchange-id="40" data-pair-id="13684" id="sort_13684" rel="45552930_13684">
<td class="left dragHandle"><span class="checkers"></span></td>
<td class="flag"><span class="ceFlags Russian_Federation" title="Россия"> </span></td>
<td class="symbol plusIconTd left bold elp alert js-injected-user-alert-container" data-column-name="name" data-pair-id="13684">
<span class="aqPopupWrapper js-hover-me-wrapper"><a class="aqlink js-hover-me" data-pairid="13684" hoverme="markets" href="/equities/gazprom_rts" target="_blank" title="Газпром ПАО">Газпром</a></span>
<span class="js-plus-icon alertBellGrayPlus genToolTip oneliner" data-tooltip="Создать уведомление" data-tooltip-alt="Уведомление активно"></span>
</td>
<td class="left bold" data-column-name="symbol"><a href="/equities/gazprom_rts" target="_blank" title="GAZP">GAZP</a></td>
<td class="left displayNone" data-column-name="exchange" title="Москва">MCX</td>
<td class="pid-13684-last" data-column-name="last" id="45552930_last_13684">174,14</td>
<td class="pid-13684-bid displayNone" data-column-name="bid" id="45552930_bid_13684">174,05</td>
<td class="pid-13684-ask displayNone" data-column-name="ask" id="45552930_ask_13684">174,13</td>
<td class="js-extended-hours js-extended-last Font pidExt-13684-last displayNone" data-column-name="extended_hours">--</td>
<td class="js-extended-hours js-extended-percent Font pidExt-13684-pcp displayNone" data-column-name="extended_hours_percent">--</td>
<td class="" data-column-name="open">174,71</td>
<td class="displayNone" data-column-name="prev">173,82</td>
<td class="pid-13684-high" data-column-name="high" id="45552930_high_13684">174,95</td>
<td class="pid-13684-low" data-column-name="low" id="45552930_low_13684">172,80</td>
<td class="bold greenFont pid-13684-pc" data-column-name="chg" id="45552930_chg_13684">+0,00</td>
<td class="bold greenFont pid-13684-pcp" data-column-name="chgpercent" id="45552930_p_chg_13684">+0,00%</td>
<td class="pid-13684-turnover" data-column-name="vol" data-value="0">-</td>
<td class="left textNum displayNone" data-column-name="next_earning" data-value="0">--</td>
<td class="pid-13684-time" data-column-name="time" data-value="1692305397" id="45552930_time_13684">17/08</td>
<td class="icon" id="45552930_isopen_13684"><span class="greenClockIcon middle isOpenExch-40"></span></td>
<td class="icon"><a class="bugCloseIcon genToolTip oneliner" data-pair-id="13684" data-portfolio-id="45552930" data-tooltip="Удалить" href="javascript:void(0)" rel="removePairFromPortfolio_45552930"> </a></td>
</tr> </tbody>"""

# soup = BeautifulSoup(html, 'lxml')
# ticker_list = soup.find_all('tr', {'data-pair-exchange-id': '40'})
# quantity_tickers = len(ticker_list)


def ticker_data(soup_obj):
    data_ticker_ = []
    name = soup_obj.find('a', class_='aqlink js-hover-me').get_text(strip=True)
    ticker_ = soup_obj.find('td', class_='left bold').get_text(strip=True)
    price = soup_obj.find('td', {'data-column-name': 'last'}).get_text(strip=True)
    open_ = soup_obj.find('td', {'data-column-name': 'open'}).get_text(strip=True)
    max_ = soup_obj.find('td', {'data-column-name': 'high'}).get_text(strip=True)
    min_ = soup_obj.find('td', {'data-column-name': 'low'}).get_text(strip=True)
    vol = soup_obj.find('td', {'data-column-name': 'vol'}).get_text(strip=True)
    time = soup_obj.find('td', {'data-column-name': 'time'}).get_text(strip=True)
    data_ticker_.append(name), data_ticker_.append(ticker_), data_ticker_.append(price), data_ticker_.append(open_),
    data_ticker_.append(max_), data_ticker_.append(min_), data_ticker_.append(vol), data_ticker_.append(time)

    return data_ticker_




