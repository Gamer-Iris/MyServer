######################################################################################################################################################
# ファイル   : fgo_main.py
# 
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 【修正履歴】
# V-001      : 2025/05/25                 Gamer-Iris   新規作成
# 
######################################################################################################################################################

# [環境設定エリア]
######################################################################################################################################################
# sshExecのモジュール
from sshExec import sshExec # type: ignore

# GameAutomationのモジュール
from GameAutomation import GameAutomation

# OS関連のモジュール
import os
import glob

# fgoの編集ファイル
from fgo_edit import fgo_edit

# [定数定義エリア]
######################################################################################################################################################
# 各キャラスキル座標テーブル
CHAR_SKILL_XY             = [110,870],[245,870],[380,870],[585,870],[720,870],[855,870],[1060,870],[1195,870],[1330,870]

# 各キャラ対象座標テーブル（3名用）
CHAR_3_TARGET_XY          = [490,650],[960,650],[1430,650]

# 各キャラ対象座標テーブル（6名用）
CHAR_6_TARGET_XY          = [205,520],[505,520],[805,520],[1105,520],[1405,520],[1705,520]

# 各マスタースキル座標テーブル
MASTER_SKILL_XY           = [1360,465],[1495,465],[1630,465]

# 各キャラ宝具合座標テーブル（3名用）
CHAR_HOUGU_XY             = [620,300],[970,300],[1320,300]

# 各エネミー対象座標テーブル（3体用）
CHAR_3_ENEMY_XY           = [815,65],[440,65],[65,65]

# 各エネミー対象座標テーブル（6体用）
CHAR_6_ENEMY_XY           = [810,50],[510,50],[210,50],[665,195],[365,195],[65,195]

# ボタン連打用座標テーブル
BOTTAN_CLLICK_XY          = [1910,1070]
X_BC                      = BOTTAN_CLLICK_XY[0]
Y_BC                      = BOTTAN_CLLICK_XY[1]

# 各イベントボックス座標テーブル
BOTTAN_CLLICK1_XY         = [1100,200]
X1_BC                     = BOTTAN_CLLICK1_XY[0]
Y1_BC                     = BOTTAN_CLLICK1_XY[1]

# イベントボックスオープンボタン連打用座標テーブル
BOTTAN_CLLICK2_XY         = [530,620]
X2_BC                     = BOTTAN_CLLICK2_XY[0]
Y2_BC                     = BOTTAN_CLLICK2_XY[1]

# 画面中央座標テーブル
SCREEN_CENTER_XY          = [950,550]
X_SC                      = SCREEN_CENTER_XY[0]
Y_SC                      = SCREEN_CENTER_XY[1]

# パーティ種類入力用
INPUT_PARTY_FRIEND_POINT  = "フレンドポイント"
INPUT_PARTY_ORBIT         = "周回"
INPUT_PARTY_QP            = "QP"

# パーティ種類check用
CHECK_PARTY_FRIEND_POINT  = "フレンドポイント"
CHECK_PARTY_ORBIT         = "周回"
CHECK_PARTY_QP            = "QP"

# 画像パス
## battlle関連
ARTS                      = '././img/fgo/battle/arts.PNG'
ATTACK                    = '././img/fgo/battle/attack.PNG'
BUSTER                    = '././img/fgo/battle/buster.PNG'
CHANGE                    = '././img/fgo/battle/change.PNG'
MASTER_SKILL              = '././img/fgo/battle/master_skill.PNG'
QUICK                     = '././img/fgo/battle/quick.PNG'
## 周回関連
EVENT_BOX_RESET           = '././img/fgo/orbit/event_box_reset.PNG'
EVENT_CLOSE               = '././img/fgo/orbit/event_close.PNG'
EVENT_REWARD              = '././img/fgo/orbit/event_reward.PNG'
EVENT_RUN                 = '././img/fgo/orbit/event_run.PNG'
ORBIT_PASS                = '././img/fgo/orbit'
## フレンド関連
CLASS_ICON                = '././img/fgo/friend/class_icon.PNG'
FRIEND_PASS               = '././img/fgo/friend'
## その他
AP_HEAL                   = '././img/fgo/other/ap_heal.PNG'
APPLE                     = '././img/fgo/other/apple.PNG'
DECIDE                    = '././img/fgo/other/decide.PNG'
DECIDE_SUMMMON            = '././img/fgo/other/decide_summon.PNG'
FGO_ICON                  = '././img/fgo/other/fgo_icon.PNG'
FRIEND_POINT              = '././img/fgo/other/friend_point.PNG'
FRIEND_POINT_SUMMON       = '././img/fgo/other/friend_point_summon.PNG'
LIST_UPDATE               = '././img/fgo/other/list_update.PNG'
MENU                      = '././img/fgo/other/menu.PNG'
NEXT                      = '././img/fgo/other/next.PNG'
NEXT_PARTY                = '././img/fgo/other/next_party.PNG'
NOTICE                    = '././img/fgo/other/notice.PNG'
ORBIT                     = '././img/fgo/other/orbit.PNG'
QEST_START1               = '././img/fgo/other/qest_start1.PNG'
QEST_START2               = '././img/fgo/other/qest_start2.PNG'
QP                        = '././img/fgo/other/qp.PNG'
RENZOKU_SYUTUGEKI         = '././img/fgo/other/renzoku_syutugeki.PNG'
SCROLL                    = '././img/fgo/other/scroll.PNG'
SCROLL_AP                 = '././img/fgo/other/scroll_AP.PNG'
SCROLL_END                = '././img/fgo/other/scroll_end.PNG'
SUMMON                    = '././img/fgo/other/summon.PNG'
SUMMON_10_TIMES           = '././img/fgo/other/summon_10_times.PNG'
SUMMON_10_TIMES_IN_A_ROW  = '././img/fgo/other/summon_10_times_in_a_row.PNG'
SURPORT_SELLECT           = '././img/fgo/other/surport_sellect.PNG'
YES                       = '././img/fgo/other/yes.PNG'

# アプリ通知時のメッセージ
FGO_APP_NOTTICE_MESSAGE1  = "処理に異常が発生しました。"
FGO_APP_NOTTICE_MESSAGE2  = "アプリ再立上げを実施します。"
FGO_APP_NOTTICE_MESSAGE3  = "アプリ再立上げに成功しました。"
FGO_APP_NOTTICE_MESSAGE4  = "処理を再開します。"

# [変数定義エリア]
######################################################################################################################################################
# 周回フラグ
orbitF                    = False

# リトライ回数
retryTimes                = 1

# マップ番号
mapNumber                 = 0

# マップ画像パス
orbitPicturePath          = []

# フレンド礼装画像パス
friendReisouPath          = []

# [前処理内容エリア]
######################################################################################################################################################

# [処理内容エリア]
######################################################################################################################################################
# fgo_mainクラス
# @param  GameAutomation         : GameAutomation
######################################################################################################################################################
class fgo_main(GameAutomation, sshExec):

    ##################################################################################################################################################
    # initメソッド
    # @param  self               : self
    ##################################################################################################################################################
    def __init__(self):
        super(fgo_main, self).__init__()
        self.function = "fgo_main"

    ##################################################################################################################################################
    # sampleメソッド
    # @param  self               : self
    ##################################################################################################################################################
    def sample(self):
        print(self.function)

    ##################################################################################################################################################
    # 周回メソッド
    # @param  self               : self
    ##################################################################################################################################################
    def orbit(self):

        # 無限ループさせる
        while 1:
            try:

                global orbitF

                # 周回フラグが立っていない事を確認 → 次処理遷移
                if(orbitF is False):
                    # 「マップ画像パスセットメソッド」の呼び出し
                    self.setOrbitPicturePath()

                    # 「マップ画像パスゲットメソッド」の呼び出し
                    searchPicture = self.getOrbitPicturePath()

                    # 「マップ番号ゲットメソッド」の呼び出し
                    mapNumber = self.getMapNumber()

                    # 「初期画面toサポート選択画面遷移メソッド」の呼び出し
                    self.initialScreenToSurportSellectScreen(searchPicture, mapNumber)

                # 「サポート選択メソッド」の呼び出し
                self.surportSellect()

                # 周回フラグが立っていない事を確認 → 「クエスト開始メソッド」の呼び出し
                if(orbitF is False):
                    # 「クエスト開始メソッド」の呼び出し
                    self.qestStart(INPUT_PARTY_ORBIT)

                # 「コマンドセレクトメソッド」の呼び出し
                fgo_edit.select_command(self)

                # 「結果確認メソッド」の呼び出し
                self.result()

                # 「連続出撃メソッド」の呼び出し
                self.preparingForSortieAcccction()

                # 周回フラグを立てる
                if(orbitF is False):
                    orbitF = True

            # エラーハンドリング時処理
            except (FGOUniqueException, SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as e:
                self.FGOUniqueExceptionHandling(e)

    ##################################################################################################################################################
    # フレンドポイント召喚メソッド
    # @param  self               : self
    ##################################################################################################################################################
    def friendPointSummon(self):

        # 無限ループさせる
        while 1:
            try:

                global orbitF

                # 繰り返しフラグが立っている事を確認 → 次処理遷移
                if(orbitF):
                    flag1 = False
                    flag2 = False
                    num1 = 0
                    num2 = 0
                    while (flag1 is False):
                        # 決定ボタンを確認 → カウントアップ
                        flag1 = self.serch_click_image(wait_time = 0.7, img_path = DECIDE_SUMMMON, conf = 0.95, offset = (0, 0))
                        if(flag1):
                            if(num1 < 60):
                                num1+=1
                                continue
                            else:
                                raise FGOUniqueException("roopの為、処理中断")
                        # 決定ボタンを未確認 → 10回召喚ボタンへ
                        else:
                            # 続けて10回召喚ボタンを確認 → 続けて10回召喚ボタンを押下
                            flag2 = self.serch_click_image(wait_time = 0.7, img_path = SUMMON_10_TIMES_IN_A_ROW, conf = 0.95, offset = (0, 0))
                            if(flag2):
                                break
                            # 続けて10回召喚ボタンを未確認 → 画面端を連打
                            else:
                                if(num2 < 60):
                                    # 画面端を連打
                                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                                    num2+=1
                                    continue
                                else:
                                    raise FGOUniqueException("roopの為、処理中断")

                    # 決定ボタンを押下
                    flag1 = False
                    num1 = 0
                    while (flag1 is False):
                        # 決定ボタンを確認 → 決定ボタンを押下
                        flag1 = self.serch_click_image(wait_time = 0.7, img_path = DECIDE_SUMMMON, conf = 0.95, offset = (0, 0))
                        if(flag1):
                            break
                        # 決定ボタンを未確認 → カウントアップ
                        else:
                            if(num1 < 60):
                                num1+=1
                                continue
                            else:
                                raise FGOUniqueException("roopの為、処理中断")

                # 繰り返しフラグが立っていない事を確認 → 次処理遷移
                else:
                    # MENUボタンを押下
                    flag1 = False
                    num1 = 0
                    while (flag1 is False):
                        # MENUボタンを確認 → MENUボタンを押下
                        flag1 = self.serch_click_image(wait_time = 4.5, img_path = MENU, conf = 0.95, offset = (0, 0))
                        if(flag1):
                            break
                        # MENUボタンを未確認 → 画面端を連打
                        else:
                            if(num1 < 60):
                                # 画面端を連打
                                self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                                num1+=1
                                continue
                            else:
                                raise FGOUniqueException("roopの為、処理中断")

                    # 召喚ボタンを押下
                    flag1 = False
                    num1 = 0
                    while (flag1 is False):
                        # 召喚ボタンを確認 → 召喚ボタンを押下
                        flag1 = self.serch_click_image(wait_time = 0.7, img_path = SUMMON, conf = 0.95, offset = (0, 0))
                        if(flag1):
                            break
                        # 召喚ボタンを未確認 → カウントアップ
                        else:
                            if(num1 < 60):
                                num1+=1
                                continue
                            else:
                                raise FGOUniqueException("roopの為、処理中断")

                    # フレンドポイント召喚が見つかるまで左へタッチスクロール
                    flag1 = False
                    num1 = 0
                    while (flag1 is False):
                        # フレンドポイント召喚文言を確認 → 次処理遷移
                        flag1 = self.serch_image(wait_time = 0.7, img_path = FRIEND_POINT_SUMMON, conf = 0.95)
                        if(flag1):
                            break
                        # フレンドポイント召喚文言を未確認 → 左へタッチスクロール
                        else:
                            if(num1 < 60):
                                # 召喚画面を左へドラッグ
                                self.drag(wait_time = 0.7, img_x = X_SC + 800, img_y = Y_SC, offset = (-X_SC, 0), drag_time = 0.3)
                                num1+=1
                                continue
                            else:
                                raise FGOUniqueException("roopの為、処理中断")

                    # 10回召喚ボタンを押下
                    flag1 = False
                    num1 = 0
                    while (flag1 is False):
                        # 10回召喚ボタンを確認 → 10回召喚ボタンを押下
                        flag1 = self.serch_click_image(wait_time = 0.7, img_path = SUMMON_10_TIMES, conf = 0.95, offset = (0, 0))
                        if(flag1):
                            break
                        # 10回召喚ボタンを未確認 → カウントアップ
                        else:
                            if(num1 < 60):
                                num1+=1
                                continue
                            else:
                                raise FGOUniqueException("roopの為、処理中断")

                    # 決定ボタンを押下
                    flag1 = False
                    num1 = 0
                    while (flag1 is False):
                        # 決定ボタンを確認 → 決定ボタンを押下
                        flag1 = self.serch_click_image(wait_time = 0.7, img_path = DECIDE_SUMMMON, conf = 0.95, offset = (0, 0))
                        if(flag1):
                            break
                        # 決定ボタンを未確認 → カウントアップ
                        else:
                            if(num1 < 60):
                                num1+=1
                                continue
                            else:
                                raise FGOUniqueException("roopの為、処理中断")

                    orbitF = True

            # エラーハンドリング時処理
            except (FGOUniqueException, SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as e:
                self.FGOUniqueExceptionHandling(e)

    ##################################################################################################################################################
    # イベントボックスオープンメソッド
    # @param  self               : self
    ##################################################################################################################################################
    def eventBoxOpen(self):

        # 無限ループさせる
        while 1:
            try:

                global orbitF

                # 繰り返しフラグが立っていない事を確認 → イベント報酬ボタンを押下
                if(orbitF is False):
                    # イベント報酬ボタンを押下
                    self.serch_click_image(wait_time = 0.7, img_path = EVENT_REWARD, conf = 0.95, offset = (0, 0))
                    # 各イベントボックス内容を押下
                    self.click(wait_time = 4.5, img_x = X1_BC, img_y = Y1_BC)

                # イベントボックスオープン処理
                flag1 = False
                while (flag1 is False):
                    # 景品をリセット文言を確認 → リセット実施
                    flag1 = self.serch_click_image(wait_time = 0.7, img_path = EVENT_BOX_RESET, conf = 0.95, offset = (0, 0))
                    if(flag1):
                        self.serch_click_image(wait_time = 0.7, img_path = EVENT_RUN, conf = 0.95, offset = (0, 0))
                        self.serch_click_image(wait_time = 0.7, img_path = EVENT_CLOSE, conf = 0.95, offset = (0, 0))
                        orbitF = True
                        break
                    # 景品をリセット文言を未確認 → 交換実施
                    else:
                        # 交換ボタン箇所を連打
                        self.click(wait_time = 0, img_x = X2_BC, img_y = Y2_BC)

            # エラーハンドリング時処理
            except (FGOUniqueException, SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as e:
                self.FGOUniqueExceptionHandling(e)

    ##################################################################################################################################################
    # 初期画面toサポート選択画面遷移メソッド
    # @param  self               : self
    # @param  searchPicture      : 希望クエスト画像
    # @param  mapNumber          : マップ番号
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def initialScreenToSurportSellectScreen(self, searchPicture, mapNumber):

        # イベント報酬文確認処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # お知らせ文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 4.5, img_path = NOTICE, conf = 0.95)
            if(flag1):
                break
            # お知らせ文言を未確認 → 画面端を連打
            else:
                if(num1 < 60):
                    # 画面端を連打
                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # サポート選択画像が確認出来るまで繰り返し処理
        i = 0
        flag1 = False
        num1 = 0
        for item in searchPicture:
            # サポート選択画像を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = SURPORT_SELLECT, conf = 0.95)
            if (flag1):
                break
            # サポート選択画像を未確認 → 希望クエスト画像をクリック
            else:
                firstTutchScroll = True
                flag2 = False
                num2 = 0
                while (flag2 is False):
                    # 希望クエスト画像を確認 → クリック
                    flag2 = self.serch_click_image(wait_time = 0.7, img_path = item, conf = 0.9, offset = (0, 0))
                    if(flag2):
                        self.serch_click_image(wait_time = 0.7, img_path = QEST_START2, conf = 0.9, offset = (0, 0))
                        i+=1
                        continue
                    # 希望クエスト画像を未確認 → スクロール画像を検索
                    else:
                        if((mapNumber == 0) or (i != mapNumber - 1)):
                            # スクロール画像を確認 → 下へスクロール
                            if(self.serch_image(wait_time = 0.7, img_path = SCROLL, conf = 0.95)):
                                # 初回操作時 → 画面初期化
                                if(firstTutchScroll):
                                    self.serch_drag_image(wait_time = 0.7, img_path = SCROLL, conf = 0.95, offset = (0, -1080), drag_time = 1.5)
                                    # フラグをFalseへ変更
                                    firstTutchScroll = False
                                # 画面を下へスクロール
                                self.serch_drag_image(wait_time = 0.7, img_path = SCROLL, conf = 0.95, offset = (0, 55), drag_time = 0.3)
                        # スクロール画像を未確認 → タッチスクロール
                        else:
                            # 初回操作時 → 画面初期化
                            if(firstTutchScroll):
                                flag3 = False
                                num3 = 0
                                while (flag3 is False):
                                    # MENUボタンを確認 → 画面初期化
                                    flag3 = self.serch_image(wait_time = 0.7, img_path = MENU, conf = 0.95)
                                    if(flag3):
                                        # 画面縮小
                                        self.keyPress(wait_time = 0.7, target_key = 'f5')
                                        self.keyPress(wait_time = 0.7, target_key = 'f5')
                                        self.keyPress(wait_time = 0.7, target_key = 'f5')
                                        self.keyPress(wait_time = 0.7, target_key = 'f5')
                                        self.keyPress(wait_time = 0.7, target_key = 'f5')
                                        self.keyPress(wait_time = 0.7, target_key = 'f5')
                                        self.keyPress(wait_time = 0.7, target_key = 'f5')
                                        # 画面を一番上へドラッグ
                                        self.drag(wait_time = 0.5, img_x = X_SC * 2, img_y = Y_SC, offset = (0, Y_SC), drag_time = 1.5)
                                        # フラグをFalseへ変更
                                        firstTutchScroll = False
                                    # ターミナル文言を未確認 → カウントアップ
                                    else:
                                        if(num3 < 60):
                                            num3+=1
                                            continue
                                        else:
                                            raise FGOUniqueException("roopの為、処理中断")
                            # 画面を下へタッチスクロール
                            self.drag(wait_time = 0.7, img_x = X_SC * 2, img_y = Y_SC, offset = (0, -30), drag_time = 0.3)
                        if(num2 < 60):
                            if(i == 0):
                                # 画面端を連打
                                self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                            num2+=1
                            continue
                        else:
                            raise FGOUniqueException("roopの為、処理中断")
                if(num1 < 60):
                    if(i == 0):
                        # 画面端を連打
                        self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 「AP回復メソッドの呼び出し
        self.apHeal()

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # サポート選択メソッド
    # @param  self               : self
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def surportSellect(self):

        # クラスアイコン選択処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # クラスアイコンを確認 → クリック
            flag1 = self.serch_click_image(wait_time = 7.5, img_path = CLASS_ICON, conf = 0.95, offset = (0, 0))
            if(flag1):
                break
            # クラスアイコン画像を未確認 → カウントアップ
            else:
                if(num1 < 60):
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 「フレンド礼装画像パスセットメソッド」の呼び出し
        self.setFriendReisouPath()

        # 「フレンド礼装画像パスゲットメソッド」の呼び出し
        searchPicture = self.getFriendReisouPath()

        # サポート選択処理
        flag1 = False
        flag2 = False
        bF    = False
        num1 = 0
        while (flag1 is False):
            # 希望のフレンド礼装を確認 → クリック
            for item in searchPicture:
                flag1 = self.serch_click_image(wait_time = 0.75, img_path = item, conf = 0.85, offset = (0, 0))
                if(flag1):
                    bF = True
                    break
            item = 0
            if(bF):
                break
            # 希望のフレンド礼装を未確認 → スクロール画像を確認
            else:
                # スクロール画像を確認 → スクロール画像が末端にいるかを確認
                flag2 = self.serch_image(wait_time = 0.7, img_path = SCROLL, conf = 0.95)
                if(flag2):
                    # スクロール画像が末端にいるかを確認 → リスト更新ボタン押下
                    flag2 = self.serch_image(wait_time = 0.7, img_path = SCROLL_END, conf = 0.992)
                    if(flag2):
                        self.serch_click_image(wait_time = 0.7, img_path = LIST_UPDATE, conf = 0.95, offset = (0, 0))
                        self.serch_click_image(wait_time = 0.7, img_path = YES, conf = 0.95, offset = (0, 0))
                        num1+=1
                    # スクロールアイコンが末端にいない場合 → 画面スクロール
                    else:
                        self.serch_drag_image(wait_time = 0.7, img_path = SCROLL, conf = 0.95, offset = (0, 55), drag_time = 0.3)
                # スクロール画像を未確認 → リスト更新ボタン押下
                else:
                    self.serch_click_image(wait_time = 0.7, img_path = LIST_UPDATE, conf = 0.95, offset = (0, 0))
                    self.serch_click_image(wait_time = 0.7, img_path = YES, conf = 0.95, offset = (0, 0))
                    num1+=1
            if(num1 < 3):
                continue
            else:
                raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # クエスト開始メソッド
    # @param  self               : self
    # @param  party              : キャラ番号（実施者）
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def qestStart(self, party):

        partyPicturePath = ""
        # パーティ種類の特定
        if (party == CHECK_PARTY_ORBIT):
            partyPicturePath = ORBIT
        elif (party == CHECK_PARTY_FRIEND_POINT):
            partyPicturePath = FRIEND_POINT
        elif (party == CHECK_PARTY_QP):
            partyPicturePath = QP

        # パーティ選択処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # 指定文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 4.5, img_path = partyPicturePath, conf = 0.95)
            if (flag1):
                break
            # 上記以外 → 待機
            else:
                if(num1 < 60):
                    # パーティ選択画面を押下
                    self.serch_click_image(wait_time = 0.7, img_path = NEXT_PARTY, conf = 0.95, offset = (0, 0))
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # クエスト開始処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # クエスト開始文言を確認 → クリック
            flag1 = self.serch_click_image(wait_time = 0.7, img_path = QEST_START1, conf = 0.95, offset = (0, 0))
            if(flag1):
                break
            # クエスト開始文言を未確認 → カウントアップ
            else:
                if(num1 < 60):
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # キャラバフ１メソッド（バフ先が選択不可Ver）
    # @param  self               : self
    # @param  c                  : キャラ番号（実施者）
    # @param  s                  : スキル番号（実施者）
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def charBuff1(self, c, s):

        idx_cs = 0
        x_cs = 0
        y_cs = 0
        # 該当するスキル番号（実施者）の座標特定
        idx_cs = (c - 1) * 3 + (s - 1)
        x_cs, y_cs = CHAR_SKILL_XY[idx_cs]

        # キャラバフ１処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # Attack文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85)
            if(flag1):
                # キャラcのスキルsを使用
                self.click(wait_time = 0.7, img_x = x_cs, img_y = y_cs)
                break
            # Attack文言を未確認 → 画面端を連打
            else:
                if(num1 < 60):
                    # 画面端を連打
                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # キャラバフ２メソッド（バフ先が選択可Ver）
    # @param  self               : self
    # @param  c1                 : キャラ番号（実施者）
    # @param  s                  : スキル番号（実施者）
    # @param  c2                 : キャラ番号（受領者）
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def charBuff2(self, c1, s, c2):

        idx_cs = 0
        x_cs = 0
        y_cs = 0
        x_ct = 0
        y_ct = 0
        # 該当するスキル番号（実施者）、スキル番号（受領者）の座標特定
        idx_cs = (c1 - 1) * 3 + (s - 1)
        x_cs, y_cs = CHAR_SKILL_XY[idx_cs]
        x_ct, y_ct = CHAR_3_TARGET_XY[c2 - 1]

        # キャラバフ２処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # Attack文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85)
            if(flag1):
                # キャラcのスキルsを使用
                self.click(wait_time = 0.7, img_x = x_cs, img_y = y_cs)
                self.click(wait_time = 0.7, img_x = x_ct, img_y = y_ct)
                break
            # Attack文言を未確認 → 画面端を連打
            else:
                if(num1 < 60):
                    # 画面端を連打
                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # マスタースキル１メソッド（バフ先が選択不可Ver）
    # @param  self               : self
    # @param  s                  : スキル番号
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def masterSkill1(self, s):

        x1_ms = 0
        y1_ms = 0
        # 該当するスキル番号の座標特定
        x1_ms, y1_ms = MASTER_SKILL_XY[s - 1]

        # マスタースキル１処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # Attack文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85)
            if(flag1):
                # バフを使用
                self.serch_click_image(wait_time = 0.7, img_path = MASTER_SKILL, conf = 0.95, offset = (0, 0))
                self.click(wait_time = 0.7, img_x = x1_ms, img_y = y1_ms)
                break
            # Attack文言を未確認 → 画面端を連打
            else:
                if(num1 < 60):
                    # 画面端を連打
                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # マスタースキル２メソッド（バフ先が単体選択可Ver）
    # @param  self               : self
    # @param  s                  : スキル番号
    # @param  c                  : キャラ番号
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def masterSkill2(self, s, c):

        x1_ms = 0
        y1_ms = 0
        x_ct = 0
        y_ct = 0
        # 該当するスキル番号、キャラ番号の座標特定
        x1_ms, y1_ms = MASTER_SKILL_XY[s - 1]
        x_ct, y_ct   = CHAR_3_TARGET_XY[c - 1]

        # マスタースキル２処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # Attack文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85)
            if(flag1):
                # バフを使用
                self.serch_click_image(wait_time = 0.7, img_path = MASTER_SKILL, conf = 0.95, offset = (0, 0))
                self.click(wait_time = 0.7, img_x = x1_ms, img_y = y1_ms)
                self.click(wait_time = 0.7, img_x = x_ct, img_y = y_ct)
                break
            # Attack文言を未確認 → 画面端を連打
            else:
                if(num1 < 60):
                    # 画面端を連打
                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # マスタースキル３メソッド（バフ先が2体選択可Ver）
    # @param  self               : self
    # @param  s                  : スキル番号
    # @param  c1                 : キャラ番号1
    # @param  c2                 : キャラ番号2
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def masterSkill3(self, s, c1, c2):

        x1_ms = 0
        y1_ms = 0
        x1_coc = 0
        y1_coc = 0
        x2_coc = 0
        y2_coc = 0
        # 該当するスキル番号、キャラ番号1、キャラ番号2の座標特定
        x1_ms, y1_ms     = MASTER_SKILL_XY[s - 1]
        x1_coc, y1_coc   = CHAR_6_TARGET_XY[c1 - 1]
        x2_coc, y2_coc   = CHAR_6_TARGET_XY[c2 - 1]

        # マスタースキル３処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # Attack文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85)
            if(flag1):
                # バフを使用
                self.serch_click_image(wait_time = 0.7, img_path = MASTER_SKILL, conf = 0.95, offset = (0, 0))
                self.click(wait_time = 0.7, img_x = x1_ms, img_y = y1_ms)
                self.click(wait_time = 0.7, img_x = x1_coc, img_y = y1_coc)
                self.click(wait_time = 0.7, img_x = x2_coc, img_y = y2_coc)
                self.serch_click_image(wait_time = 0.7, img_path = CHANGE, conf = 0.95, offset = (0, 0))
                break
            # Attack文言を未確認 → 画面端を連打
            else:
                if(num1 < 60):
                    # 画面端を連打
                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # エネミー選択１メソッド（エネミーが3体以下Ver）
    # @param  self               : self
    # @param  c                  : エネミー番号（右上から）
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def selectEnemy1(self, c):

        # 該当するエネミー番号の座標取得
        x_ce, y_ce = CHAR_3_ENEMY_XY[c - 1]

        # エネミー選択処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # Attack文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85)
            if(flag1):
                self.click(wait_time = 0.7, img_x = x_ce, img_y = y_ce)
                break
            # Attack文言を未確認 → 画面端を連打
            else:
                if(num1 < 60):
                    # 画面端を連打
                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # エネミー選択２メソッド（エネミーが4体以上Ver）
    # @param  self               : self
    # @param  c                  : エネミー番号（右上から）
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def selectEnemy2(self, c):

        # 該当するエネミー番号の座標取得
        x_ce, y_ce = CHAR_6_ENEMY_XY[c - 1]

        # エネミー選択処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # Attack文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85)
            if(flag1):
                self.click(wait_time = 0.7, img_x = x_ce, img_y = y_ce)
                break
            # Attack文言を未確認 → 画面端を連打
            else:
                if(num1 < 60):
                    # 画面端を連打
                    self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # アタック１メソッド
    # @param  self               : self
    # @param  aN                 : Attack回数
    # @param  aF                 : 初回Attackフラグ
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def attack1(self, aN, aF):

        # 初回Attackフラグチェック → 次処理遷移
        if aF:
            flag1 = False
            num1 = 0
            while flag1 is False:
                # Attack文言を確認 → クリック
                flag1 = self.serch_click_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85, offset = (0, 0))
                if flag1:
                    break
                # Attack文言を未確認 → 画面端を連打
                else:
                    if num1 < 60:
                        # 画面端を連打
                        self.click(wait_time=0, img_x=X_BC, img_y=Y_BC)
                        num1 += 1
                        continue
                    else:
                        raise FGOUniqueException("roopの為、処理中断")

        # アタック処理
        card_paths = [BUSTER, ARTS, QUICK]
        num1 = 0
        for path in card_paths:
            for _ in range(3):
                if num1 >= aN:
                    return True
                if self.serch_click_image(wait_time=0.7, img_path=path, conf=0.95, offset=(0, 0)):
                    num1 += 1

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # 宝具１メソッド（個人宝具Ver）
    # @param  self               : self
    # @param  c                  : キャラ番号
    # @param  aF                 : 初回Attackフラグ
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def hougu1(self, c, aF):

        x_ch = 0
        y_ch = 0
        # 該当するキャラ番号の座標特定
        x_ch, y_ch = CHAR_HOUGU_XY[c - 1]

        # 初回Attackフラグチェック → 次処理遷移
        if aF:
            flag1 = False
            num1 = 0
            while flag1 is False:
                # Attack文言を確認 → クリック
                flag1 = self.serch_click_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85, offset = (0, 0))
                if flag1:
                    break
                # Attack文言を未確認 → 画面端を連打
                else:
                    if num1 < 60:
                        # 画面端を連打
                        self.click(wait_time=0, img_x=X_BC, img_y=Y_BC)
                        num1 += 1
                        continue
                    else:
                        raise FGOUniqueException("roopの為、処理中断")

        # 宝具１処理
        flag1 = False
        num1 = 0
        while True:
            # 宝具を打てた → 次処理遷移
            flag1 = self.click(wait_time = 1.5, img_x = x_ch, img_y = y_ch)
            if flag1:
                break
            # 宝具を打てなかった → カウントアップ
            else:
                if(num1 < 60):
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # 宝具２メソッド（複数人宝具Ver）
    # @param  self               : self
    # @param  c                  : キャラ番号の配列
    # @param  aF                 : 初回Attackフラグ
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def hougu2(self, c, aF):

        # 初回Attackフラグチェック → 次処理遷移
        if aF:
            flag1 = False
            num1 = 0
            while flag1 is False:
                # Attack文言を確認 → クリック
                flag1 = self.serch_click_image(wait_time = 0.7, img_path = ATTACK, conf = 0.85, offset = (0, 0))
                if flag1:
                    break
                # Attack文言を未確認 → 画面端を連打
                else:
                    if num1 < 60:
                        # 画面端を連打
                        self.click(wait_time=0, img_x=X_BC, img_y=Y_BC)
                        num1 += 1
                        continue
                    else:
                        raise FGOUniqueException("roopの為、処理中断")

        # 宝具２処理
        clicked_map = {item: False for item in c}
        num1 = 0
        while not all(clicked_map.values()):
            # キャラ番号の配列分繰り返し
            for item in c:
                # すでにクリック済みのものはスキップ
                if clicked_map[item]:
                    continue
                # 該当するキャラ番号の座標特定
                x_ch, y_ch = CHAR_HOUGU_XY[item - 1]
                # 宝具クリック → 成功時にフラグをTrueに
                if self.click(wait_time=1.5, img_x=x_ch, img_y=y_ch):
                    clicked_map[item] = True
            # 全て完了していればループ終了
            if all(clicked_map.values()):
                break
            # 未完了あり → カウントアップ
            else:
                if num1 < 60:
                    num1 += 1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # 結果確認メソッド
    # @param  self               : self
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def result(self):

        # 結果確認処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # 連続出撃文言を確認 → 次処理遷移
            flag1 = self.serch_image(wait_time = 0.7, img_path = RENZOKU_SYUTUGEKI, conf = 0.9)
            if(flag1):
                break
            # 連続出撃文言を未確認 → 待機
            else:
                flag2 = False
                # 次へ文言を確認 → クリック
                flag2 = self.serch_click_image(wait_time = 0.7, img_path = NEXT, conf = 0.95, offset = (0, 0))
                # 次へ文言を未確認 → 画面端を連打
                if(flag2 is False):
                    if(num1 < 60):
                        # 画面端を連打
                        self.click(wait_time = 0, img_x = X_BC, img_y = Y_BC)
                        num1+=1
                        continue
                    else:
                        raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # 連続出撃メソッド
    # @param  self               : self
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def preparingForSortieAcccction(self):

        # 連続出撃ボタンクリック処理
        flag1 = False
        num1 = 0
        while (flag1 is False):
            # 連続出撃文言を確認 → クリック
            flag1 = self.serch_click_image(wait_time = 0.7, img_path = RENZOKU_SYUTUGEKI, conf = 0.95, offset = (0, 0))
            if(flag1):
                break
            # 連続出撃を未確認 → カウントアップ
            else:
                if(num1 < 60):
                    num1+=1
                    continue
                else:
                    raise FGOUniqueException("roopの為、処理中断")

        # 「AP回復メソッドの呼び出し
        self.apHeal()

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # AP回復メソッド
    # @param  self               : self
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def apHeal(self):

        # AP回復画面確認処理
        aPHaalFlag = False

        # AP回復文言を確認 → AP回復フラグを立てる
        flag1 = False
        flag1 = self.serch_image(wait_time = 0.7, img_path = AP_HEAL, conf = 0.8)
        if(flag1):
            aPHaalFlag = True

        # AP回復フラグを確認 → 回復アイテムを選択する
        if(aPHaalFlag):
            firstTutchScroll = True
            flag1 = False
            num1 = 0
            while (flag1 is False):
                # 回復アイテムを確認 → クリック
                flag1 = self.serch_click_image(wait_time = 0.7, img_path = APPLE, conf = 0.95, offset = (0, 0))
                if(flag1):
                    break
                # 回復アイテムを未確認 → スクロール画像を検索
                else:
                    # スクロール画像を確認 → 下へスクロール
                    if(self.serch_image(wait_time = 0.7, img_path = SCROLL_AP, conf = 0.95)):
                        # 初回操作時 → 画面初期化
                        if(firstTutchScroll):
                            self.serch_drag_image(wait_time = 0.7, img_path = SCROLL_AP, conf = 0.95, offset = (0, -1440), drag_time = 0.3)
                            # フラグをFalseへ変更
                            firstTutchScroll = False
                        #画面を下へスクロール
                        self.serch_drag_image(wait_time = 0.7, img_path = SCROLL_AP, conf = 0.95, offset = (0, 55), drag_time = 0.3)
                    if(num1 < 60):
                        num1+=1
                        continue
                    else:
                        raise FGOUniqueException("roopの為、処理中断")

        # AP回復フラグを確認 → 回復アイテムを使用する
        if(aPHaalFlag):
            flag1 = False
            num1 = 0
            while (flag1 is False):
                # 回復アイテムを確認 → クリック
                flag1 = self.serch_click_image(wait_time = 0.7, img_path = DECIDE, conf = 0.8, offset = (0, 0))
                if(flag1):
                    break
                # 回復アイテムをを未確認 → カウントアップ
                else:
                    if(num1 < 60):
                        num1+=1
                        continue
                    else:
                        raise FGOUniqueException("roopの為、処理中断")

        # 処理結果を返す
        return True

    ##################################################################################################################################################
    # マップ画像パスセットメソッド
    # @param  self               : self
    ##################################################################################################################################################
    def setOrbitPicturePath(self):

        # マップ画像パスセット
        global orbitPicturePath
        orbitPicturePath = glob.glob(ORBIT_PASS + r'\orbit_picture*.PNG')

    ##################################################################################################################################################
    # マップ画像パスゲットメソッド
    # @param  self               : self
    # @return orbitPicturePath   : マップ画像パス
    ##################################################################################################################################################
    def getOrbitPicturePath(self):

        # マップ画像パスゲット
        return orbitPicturePath

    ##################################################################################################################################################
    # マップ番号セットメソッド
    # @param  self               : self
    # @param  setMapNumber       : マップ番号
    ##################################################################################################################################################
    def setMapNumber(self, setMapNumber):

        # マップ番号セット
        global mapNumber
        mapNumber = int(setMapNumber)

    ##################################################################################################################################################
    # マップ番号ゲットメソッド
    # @param  self               : self
    # @return getMapNumber       : マップ番号
    ##################################################################################################################################################
    def getMapNumber(self):

        # マップ番号ゲット
        return mapNumber

    ##################################################################################################################################################
    # フレンド礼装画像パスセットメソッド
    # @param  self               : self
    ##################################################################################################################################################
    def setFriendReisouPath(self):

        # フレンド礼装画像パスセット
        global friendReisouPath
        friendReisouPath = glob.glob(FRIEND_PASS + '/friend_reisou*.PNG')

    ##################################################################################################################################################
    # フレンド礼装画像パスゲットメソッド
    # @param  self               : self
    # @return friendReisouPath   : フレンド礼装画像パス
    ##################################################################################################################################################
    def getFriendReisouPath(self):

        # フレンド礼装画像パスゲット
        return friendReisouPath

    ##################################################################################################################################################
    # FGO独自例外キャッチ時処理
    # @param  self               : self
    # @param  e                  : Exception
    # @return True               : True（正常終了時）
    # @raise  FGOUniqueException : FGOUniqueException（異常終了時）
    ##################################################################################################################################################
    def FGOUniqueExceptionHandling(self, e):
        global orbitF
        global retryTimes

        # リトライ回数が3以下 → アプリ再立ち上げ
        if retryTimes <= 3:
            # アプリ通知
            message = FGO_APP_NOTTICE_MESSAGE1 + '\r\n' + FGO_APP_NOTTICE_MESSAGE2
            programName = os.path.basename(__file__)
            self.sshAppNotice(programName = programName, noticeMessage1 = message, noticeMessage2 = str(e))

            # タスクキル実施失敗 → 例外発行
            if(self.taskKill(wait_time = 0.7, conf = 0.95) is False):
                raise FGOUniqueException("タスクキル失敗の為、処理中断")

            # FGO再立ち上げ実施失敗 → 例外発行
            if(self.aplReboot(wait_time = 0.7, img_path = FGO_ICON, conf = 0.95) is False):
                raise FGOUniqueException("FGO再立ち上げ失敗の為、処理中断")

            # アプリ通知
            message = FGO_APP_NOTTICE_MESSAGE3 + '\r\n' + FGO_APP_NOTTICE_MESSAGE4
            programName = os.path.basename(__file__)
            self.sshAppNotice(programName = programName, noticeMessage1 = message, noticeMessage2 = "")

            # 周回フラグの初期化
            orbitF = False

            # リトライ回数を+1する
            retryTimes += 1

            # キャッチした例外を初期化
            del e

        # リトライ回数が4以上 → 例外発行
        else:
            raise FGOUniqueException("roopの為、処理中断")

# [例外処理内容エリア]
######################################################################################################################################################
# FGO独自例外クラス
# @param  Exception              : Exception
######################################################################################################################################################
class FGOUniqueException(Exception):
    pass
