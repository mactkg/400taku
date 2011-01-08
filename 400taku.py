#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import random

kdata = {u"1" : u"秋の他のかりほの庵の苫をあらみ",
		 u"2" : u"春過ぎて夏来にけらし白妙の",
		 u"3" : u"あしびきの山鳥の尾のしだり尾の",
		 u"4" : u"田子の浦にうちいでて見れば白妙の",
		 u"5" : u"奥山にもみぢふみわけ鳴く鹿の",
		 u"6" : u"かささぎの渡せる橋におく霜の",
		 u"7" : u"天の原ふりさけ見れば春日なる",
		 u"8" : u"わが庵は都のたつみしかぞすむ",
		 u"9" : u"花の色はうつりにけりないたづらに",
		 u"10" : u"これやこの行くも帰るもわかれては",
		 u"11" : u"わたの原八十島かけてこぎいでぬと",
		 u"12" : u"天つ風雲のかよひ路吹きとぢよ",
		 u"13" : u"つくばねの峰よりおつるみなの川",
		 u"14" : u"みちのくのしのぶもぢずり誰ゆゑに",
		 u"15" : u"君がため春の野にいでて若菜つむ",
		 u"16" : u"立ちわかれいなばの山の峰に生ふる",
		 u"17" : u"ちはやぶる神代もきかず竜田川",
		 u"18" : u"すみの江の岸に寄る波よるさへや",
		 u"19" : u"難波潟みじかき葦のふしのまも",
		 u"20" : u"わびぬればいまはたおなじ難破なる",
		 u"21" : u"いま来むといひしばかりに長月の",
		 u"22" : u"吹くからに秋の草木のしをるれば",
		 u"23" : u"月見ればちぢに物こそかなしけれ",
		 u"24" : u"このたびは幣もとりあへず手向山",
		 u"25" : u"名にしおはば逢う坂山のさねかづら",
		 u"26" : u"小倉山峰のもみぢば心あらば",
		 u"27" : u"みかの原わきて流るるいづみ川",
		 u"28" : u"山里は冬ぞさびしきさまりける",
		 u"29" : u"こころあてに折らばや折らむ",
		 u"30" : u"ありあけのつれなく見えし別れより",
		 u"31" : u"朝ぼらけありあけの月と見るまでに",
		 u"32" : u"山川に風のかけたるしがらみは",
		 u"33" : u"ひさかたの光のどけき春の日に",
		 u"34" : u"誰をかも知る人にせむ高砂の",
		 u"35" : u"人はいさ心もしらずふるさとは",
		 u"36" : u"夏の夜はまだ宵ながら明けぬるを",
		 u"37" : u"白露に風の吹きしく秋の野は",
		 u"38" : u"忘らるる身をば思はずちかひてし",
		 u"39" : u"浅芽生の小野の篠原しのぶれど",
		 u"40" : u"しのぶれど色にいでにけりわが恋は",
		 u"41" : u"恋すてふ我が名はまだき立ちにけり",
		 u"42" : u"ちぎりきなかたみに袖をしぼりつつ",
		 u"43" : u"あひみてののちの心にくらぶれば",
		 u"44" : u"あふことのたえてしなくはなかなかに",
		 u"45" : u"あはれともいふべき人は思ほえで",
		 u"46" : u"由良のとをわたる舟人かぢを絶え",
		 u"47" : u"八重むぐらしげれる宿のさびしさに",
		 u"48" : u"風をいたみ岩うつ波のおのれのみ",
		 u"49" : u"みかきもり衛士のたく火の夜は燃え",
		 u"50" : u"君がため惜しからざりし命さへ",
		 u"51" : u"かくとだにえやはいぶきのさしも草",
		 u"52" : u"あけぬれば暮るるものとはしりながら",
		 u"53" : u"嘆きつつひとり寝る夜のあくるまは",
		 u"54" : u"忘れじのゆくすゑまではかたければ",
		 u"55" : u"滝の音はたえて久しくなりぬれど",
		 u"56" : u"あらぎらむこの世のほかの思ひ出に",
		 u"57" : u"めぐりあひてめしやそれともわかぬまに",
		 u"58" : u"ありま山ゐなの笹原風吹けば",
		 u"59" : u"やすらはで寝なましものをさ夜ふけて",
		 u"60" : u"大江山いく野の道の遠ければ",
		 u"61" : u"いにしへの奈良の都の八重桜",
		 u"62" : u"夜をこめて鳥のそらねんははかるとも",
		 u"63" : u"いまはただ思ひ絶えなむとばかりを",
		 u"64" : u"朝ぼらけ宇治の川霧たえだえに",
		 u"65" : u"うらみわびほさぬ袖だにあるものを",
		 u"66" : u"もろともにあはれと思へ山桜",
		 u"67" : u"春の夜の夢ばかりなる手枕に",
		 u"68" : u"心にもあらでうき世にながらへば",
		 u"69" : u"あらしふく三室の山のもみぢばは",
		 u"70" : u"さびしさに宿をたちいでてながむれば",
		 u"71" : u"夕されば門田の稲葉おとづれて",
		 u"72" : u"音にきくたかしの浜のあだ波は",
		 u"73" : u"かみさ後のをのへの桜咲きにけり",
		 u"74" : u"憂かりける人を初瀬の山おろしよ",
		 u"75" : u"ちぎりおきしさせもが露をいのちにて",
		 u"76" : u"わたの原こぎいでてみれば久方の",
		 u"77" : u"瀬をはやみ岩にせかるる滝川の",
		 u"78" : u"淡路島かよふ千鳥のなく声に",
		 u"79" : u"秋風にたなびく雲のたえ間より",
		 u"80" : u"長からむ心もしらず黒髪の",
		 u"81" : u"ほととぎす鳴きつる方をながむれば",
		 u"82" : u"思ひわびさてもいのちはあるものを",
		 u"83" : u"世の中よ道こそなけれ思ひ入る",
		 u"84" : u"ながらへばまたこのごろやしのばれむ",
		 u"85" : u"夜もすがら思ふころは明けやらで",
		 u"86" : u"なげけとて月やは物を思はする",
		 u"87" : u"村雨の露もまだひぬまきの葉に",
		 u"88" : u"難破江の葦のかりねのひとよゆゑ",
		 u"89" : u"玉の緒よたえなばたえねながらへば",
		 u"90" : u"見せばやな雄島のあまの袖だにも",
		 u"91" : u"きりぎりす鳴くや霜夜のさむしろに",
		 u"92" : u"我が袖は潮干に見えぬ沖の石の",
		 u"93" : u"世の中のつねにもがもななぎさこぐ",
		 u"94" : u"み吉野の山の秋風さ夜ふけて",
		 u"95" : u"おほけなくうき世の民におほふかな",
		 u"96" : u"花さそ嵐の庭の雪ならで",
		 u"97" : u"こぬ人をまつほの浦の夕なぎに",
		 u"98" : u"風そよぐならの小川の夕ぐれは",
		 u"99" : u"人もをし人もうらめしあぢきなく",
		 u"100" : "ももしきやふるき軒ばのしのぶにも"}
sdata = {u"1" : u"わが衣手に露はぬれつつ",
		 u"2" : u"衣ほすてふ天の香具山",
		 u"3" : u"ながながし夜をひとりかも寝む",
		 u"4" : u"富士の高嶺に雪は降りつつ",
		 u"5" : u"声聞く時ぞ秋はかなしき",
		 u"6" : u"白きを見れば夜ぞふけにける",
		 u"7" : u"三笠の山にいでし月かも",
		 u"8" : u"世をうぢ山と人はいふなり",
		 u"9" : u"わが身よにふるながめせしまに",
		 u"10" : u"知るも知らぬもあふ坂の関",
		 u"11" : u"人には告げよあまのつり舟",
		 u"12" : u"をとめの姿しばしとどめむ",
		 u"13" : u"恋ぞつもりて淵となりぬる",
		 u"14" : u"乱れそめにしわれならなくに",
		 u"15" : u"わが衣手に雪はふりつつ",
		 u"16" : u"まつとし聞かば今帰り来む",
		 u"17" : u"からくれなゐに水くくるとは",
		 u"18" : u"夢通ひ路人めよくらむ",
		 u"19" : u"あはでこの世をすぐしてよとや",
		 u"20" : u"みをつくしてもあはむとぞ思ふ",
		 u"21" : u"ありあけの月を待ちいでるつるかな",
		 u"22" : u"むべ山風を嵐をいふらむ",
		 u"23" : u"わが身ひとつの秋にはあらねど",
		 u"24" : u"もみぢの錦神のまにまに",
		 u"25" : u"人にしられでくるよしもがな",
		 u"26" : u"いまひとたびのみゆき待たなむ",
		 u"27" : u"いつ見きとてか恋したるらむ",
		 u"28" : u"ひとめも草もかれぬと思へば",
		 u"29" : u"おきまどはせる白菊の花",
		 u"30" : u"あかつきばかりうきものはなし",
		 u"31" : u"吉野の里にふれる白雪",
		 u"32" : u"流れもあへぬもみぢなりけり",
		 u"33" : u"しづ心なく花のちるらむ",
		 u"34" : u"松も昔も友ならなくに",
		 u"35" : u"花ぞ昔の香ににほひける",
		 u"36" : u"雲のいづこに月やどるらむ",
		 u"37" : u"つらぬきとめぬ玉ぞ散りける",
		 u"38" : u"人のいのちの惜しくもあるかな",
		 u"39" : u"あまりてなどか人の恋しき",
		 u"40" : u"物や思ふと人のとふまで",
		 u"41" : u"人知れずこそ思ひそめしか",
		 u"42" : u"末の松山波こさじとは",
		 u"43" : u"昔は物を思はざりけり",
		 u"44" : u"人をも身をも恨みざらまし",
		 u"45" : u"身のいたづらになりぬべきかな",
		 u"46" : u"ゆくも知らぬ恋の道かな",
		 u"47" : u"人こそ見えね秋は来にけり",
		 u"48" : u"くだけて物を思ふころかな",
		 u"49" : u"昼は消えつつ物をこそ思へ",
		 u"50" : u"長くもがなと思ひけるかな",
		 u"51" : u"さしもしらじなもゆる思ひを",
		 u"52" : u"なほうらめしき朝ぼらけかな",
		 u"53" : u"いかに久しきものとかはしる",
		 u"54" : u"今日をかぎりのいのちともがな",
		 u"55" : u"名こそ流れてなほ聞こえけれ",
		 u"56" : u"いまひとたびのあふこともがな",
		 u"57" : u"雲隠れにし夜半の月かな",
		 u"58" : u"いでそよ人を忘れやはする",
		 u"59" : u"かたぶくまでの月を見しかな",
		 u"60" : u"まだふみも見ず天の橋立",
		 u"61" : u"けふ九重ににほひけるかな",
		 u"62" : u"よに逢坂の関はゆるさじ",
		 u"63" : u"人づてならで言ふよしもがな",
		 u"64" : u"あらはれわたる瀬々の網代木",
		 u"65" : u"恋にくちなむ名こそをしけれ",
		 u"66" : u"花よりほかにしる人もなし",
		 u"67" : u"かひなくたたむ名こそをしけれ",
		 u"68" : u"恋しかるべき夜半の月かな",
		 u"69" : u"竜田の川の錦なりけり",
		 u"70" : u"いづこもおなじ秋の夕暮れ",
		 u"71" : u"葦のまろやに秋風ぞ吹く",
		 u"72" : u"かけじや袖のぬれもこそすれ",
		 u"73" : u"外山のかすみただずもあらなむ",
		 u"74" : u"はげしかれとは折らぬものを",
		 u"75" : u"あはれ今年の秋もいぬめり",
		 u"76" : u"雲ゐにまがふ沖つ白波",
		 u"77" : u"われても末にあはむとぞ思ふ",
		 u"78" : u"幾夜ねざめぬ須磨の関守",
		 u"79" : u"もれいづる月の影のさやけさ",
		 u"80" : u"みだれてけさは物をこそ思へ",
		 u"81" : u"ただありあけの月ぞ残れる",
		 u"82" : u"憂きにたへぬは涙なりけり",
		 u"83" : u"山の奥にも鹿ぞ鳴くなる",
		 u"84" : u"憂しと見し世ぞ今は恋しき",
		 u"85" : u"閨のひまさへつれなかりけり",
		 u"86" : u"かこち顔なるわが涙かな",
		 u"87" : u"霧たちのぼる秋の夕暮れ",
		 u"88" : u"みをつくしてや恋ひわたるべき",
		 u"89" : u"忍ぶることの弱りもぞする",
		 u"90" : u"ぬれにぞぬれし色のはかはらず",
		 u"91" : u"衣かたしきひとりかも寝む",
		 u"92" : u"人こそしらねかわくまもなし",
		 u"93" : u"あまの小舟のつなでかなしも",
		 u"94" : u"ふるさと寒く衣うつなり",
		 u"95" : u"わがたつ杣に黒染めの袖",
		 u"96" : u"ふりゆくものは我が身なりけり",
		 u"97" : u"焼くやもしほの身もこがれつつ",
		 u"98" : u"みそぎぞ夏のしるしなりける",
		 u"99" : u"世を思ふゆゑに物思ふ身は",
		 u"100" : u"なほあまりある昔なりけり"}


def printq(trueans, returnlist):
	print kdata[str(trueans)]
	f = 0
	for i in returnlist:
		f = f + 1
		print str(f) + "." + sdata[str(returnlist[f - 1])]

def howmany():
	how = int(raw_input(u"howmanytimes(<101):"))
	if how > 101:
		howmany()
	return how

def main():
	per = 0
	returnlist = []
	leftlist = []
	how = howmany()
	for i in range(1,101):
		leftlist.append(i)

	for i in range(how):
		print "----------"
		random.shuffle(leftlist)
		trueans = leftlist[0]
		returnlist.append(trueans)
		for k in range(3):
			returnlist.append(random.randint(1,101))
		random.shuffle(returnlist)

		printq(trueans, returnlist)
		ans = raw_input("ans:")

		if returnlist[int(ans)-1] == trueans:
			print u"right."
			per = per + 1.0
		else:
			print u"wrong"
		print u"ans:" + kdata[str(trueans)] + " " + sdata[str(trueans)] + " :" + str(trueans)
		del returnlist[:]
	print str(100 * per / how) + "% (" + str(int(per)) + "/" + str(how) + ")" 

if __name__ == '__main__':
	main()
	raw_input('Press return key.')
