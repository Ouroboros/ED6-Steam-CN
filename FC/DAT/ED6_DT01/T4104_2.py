import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4104_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4104_2 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4104.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x19BE
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '比赛快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0001 offset: 0x81
@scena.Code('Init')
def Init():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '不管是谁取得优胜都很好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0002 offset: 0xA8
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我现在已经开始兴奋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0xCB
@scena.Code('func_03_CB')
def func_03_CB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哈～哈，因为兴奋过度，\n',
            '来得太早了些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xFD
@scena.Code('func_04_FD')
def func_04_FD():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今年为谁加油好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x11C
@scena.Code('func_05_11C')
def func_05_11C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '准决赛要开始了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x13B
@scena.Code('func_06_13B')
def func_06_13B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '完了，\n',
            '导力相机忘带了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x15F
@scena.Code('func_07_15F')
def func_07_15F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '可惜了！\n',
            '今年亲卫队没有出战呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x18B
@scena.Code('func_08_18B')
def func_08_18B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '团体赛比想象的要有趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1B0
@scena.Code('func_09_1B0')
def func_09_1B0():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我想还是国境警卫队\n',
            '会取得优胜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1DE
@scena.Code('func_0A_1DE')
def func_0A_1DE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天的对阵\n',
            '会是怎么样的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x206
@scena.Code('func_0B_206')
def func_0B_206():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '游击士的两个小组\n',
            '都还没有出局。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两组都要加油啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x24A
@scena.Code('func_0C_24A')
def func_0C_24A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '特务部队虽然让人觉得有些害怕，\n',
            '但实力相当强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x286
@scena.Code('func_0D_286')
def func_0D_286():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '比赛怎么还不开始啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2A7
@scena.Code('func_0E_2A7')
def func_0E_2A7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '每年的比赛\n',
            '我都很期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2CD
@scena.Code('func_0F_2CD')
def func_0F_2CD():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天是总决赛的日子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2F0
@scena.Code('func_10_2F0')
def func_10_2F0():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哪支小组会取胜呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我心里扑通扑通地响呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x32D
@scena.Code('func_11_32D')
def func_11_32D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我喜欢游击士组里面\n',
            '那个金色头发的小哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '外表英俊潇洒，\n',
            '而且射击方面也无懈可击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x38E
@scena.Code('func_12_38E')
def func_12_38E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我想看那个戴着红色面具的哥哥\n',
            '和那个像熊一样的叔叔\n',
            '打架的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x3DB
@scena.Code('func_13_3DB')
def func_13_3DB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '真不愧是总决赛的日子，\n',
            '一大早就已经有很多人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x419
@scena.Code('func_14_419')
def func_14_419():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '双方都是今年\n',
            '第一次参加比赛，\n',
            '哪一边会取胜的确是决赛的看点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x464
@scena.Code('func_15_464')
def func_15_464():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '游击士小组里面\n',
            '好像有个女孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可真了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x4A8
@scena.Code('func_16_4A8')
def func_16_4A8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '比赛还没有开始吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x4C7
@scena.Code('func_17_4C7')
def func_17_4C7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '每年只有我和老头子\n',
            '两个人来看比赛，\n',
            '感到无聊也没有办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x50E
@scena.Code('func_18_50E')
def func_18_50E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '因为太期待今天的比赛了，\n',
            '我昨天一夜都睡不着觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x54C
@scena.Code('func_19_54C')
def func_19_54C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我还是觉得\n',
            '特务部队会取胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一看名字就知道来头不小嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x594
@scena.Code('func_1A_594')
def func_1A_594():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '就算口干舌燥\n',
            '我也要全力为比赛呐喊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x5C4
@scena.Code('func_1B_5C4')
def func_1B_5C4():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我支持游击士组哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前我也曾受到\n',
            '游击士的很多关照啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x60C
@scena.Code('func_1C_60C')
def func_1C_60C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '要是把便当\n',
            '也带来就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一大早就过来排队，\n',
            '肚子都饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x657
@scena.Code('func_1D_657')
def func_1D_657():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '武术大会果然很有意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是看就已经爽呆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x69D
@scena.Code('func_1E_69D')
def func_1E_69D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '游击士组里的那个男孩子\n',
            '和我儿子的年纪差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何\n',
            '我也要支持游击士组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x6FA
@scena.Code('func_1F_6FA')
def func_1F_6FA():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '如果从综合实力来看的话，\n',
            '不用说也知道\n',
            '那个特务部队是最强的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x745
@scena.Code('func_20_745')
def func_20_745():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '没有想到决赛对阵\n',
            '会是这样的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x77A
@scena.Code('func_21_77A')
def func_21_77A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '王国军和游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得无论哪一方，\n',
            '都是保卫我们市民的、\n',
            '值得大家信赖的好战士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x7DD
@scena.Code('func_22_7DD')
def func_22_7DD():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '比赛快要开始了……\n',
            '我会全力为大家呐喊助威的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x817
@scena.Code('func_23_817')
def func_23_817():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_88B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 5, 0x635)),
            Expr.Return,
        ),
        'loc_88B',
    )

    ChrTalk(
        0x002F,
        (
            '#0340111727V#600F我从年轻的时候就喜欢\n',
            '观看每年一度的武术大会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111677V加油啊。\n',
            '艾丝蒂尔、约修亚，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_88B(): pass

    label('loc_88B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x88F
@scena.Code('func_24_88F')
def func_24_88F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_8FD',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说那些对手\n',
            '的确不容易对付，\n',
            '不过我坚信你们一定能够取胜的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120111627V我会给你们加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_988')

    def _loc_8FD(): pass

    label('loc_8FD')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '哟，两位新人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120950001V你们决赛的对手相当强劲，\n',
            '不过肯定会有胜算的。\n',
            '我坚信你们一定能够取胜的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120111627V我会给你们加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_988(): pass

    label('loc_988')

    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x98C
@scena.Code('func_25_98C')
def func_25_98C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_9EF',
    )

    ChrTalk(
        0x00FE,
        (
            '听好，一定要放松，\n',
            '像往常那样出战就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320111635V就连在气势上也要战胜对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5A')

    def _loc_9EF(): pass

    label('loc_9EF')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '啊，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听好，一定要放松，\n',
            '像往常那样出战就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320111635V就连在气势上也要战胜对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A5A(): pass

    label('loc_A5A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0026 offset: 0xA5E
@scena.Code('func_26_A5E')
def func_26_A5E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0027 offset: 0xA77
@scena.Code('func_27_A77')
def func_27_A77():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天我一大早\n',
            '就去叫了那两个人，\n',
            '然后来竞技场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为绝对不能错过总决赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0028 offset: 0xAD4
@scena.Code('func_28_AD4')
def func_28_AD4():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哪个小组会取胜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0029 offset: 0xAF3
@scena.Code('func_29_AF3')
def func_29_AF3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_B00',
    )

    Jump('loc_C07')

    def _loc_B00(): pass

    label('loc_B00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_B0A',
    )

    Jump('loc_C07')

    def _loc_B0A(): pass

    label('loc_B0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_B14',
    )

    Jump('loc_C07')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_B1E',
    )

    Jump('loc_C07')

    def _loc_B1E(): pass

    label('loc_B1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_BCE',
    )

    ChrTalk(
        0x00FE,
        (
            '想拿个观战的好位置，\n',
            '所以我在门外彻夜排队，\n',
            '不料被那些巡逻的士兵赶回了家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后，我偷偷地从家里溜出来，\n',
            '躲在大街上的草丛里等那些士兵撤走，\n',
            '然后才来排队的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C07')

    def _loc_BCE(): pass

    label('loc_BCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_BD8',
    )

    Jump('loc_C07')

    def _loc_BD8(): pass

    label('loc_BD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_BE2',
    )

    Jump('loc_C07')

    def _loc_BE2(): pass

    label('loc_BE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_BEC',
    )

    Jump('loc_C07')

    def _loc_BEC(): pass

    label('loc_BEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_BF6',
    )

    Jump('loc_C07')

    def _loc_BF6(): pass

    label('loc_BF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_C00',
    )

    Jump('loc_C07')

    def _loc_C00(): pass

    label('loc_C00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_C07',
    )

    def _loc_C07(): pass

    label('loc_C07')

    TalkEnd(0x00FE)

    Return()

# id: 0x002A offset: 0xC0B
@scena.Code('func_2A_C0B')
def func_2A_C0B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_C18',
    )

    Jump('loc_D6F')

    def _loc_C18(): pass

    label('loc_C18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_C22',
    )

    Jump('loc_D6F')

    def _loc_C22(): pass

    label('loc_C22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_C2C',
    )

    Jump('loc_D6F')

    def _loc_C2C(): pass

    label('loc_C2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_C36',
    )

    Jump('loc_D6F')

    def _loc_C36(): pass

    label('loc_C36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_CB2',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天真是辛苦我丈夫了，\n',
            '帮我拿到这么一个好座位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说我的要求很任性，\n',
            '不过没想到他能为我做到这种地步……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D6F')

    def _loc_CB2(): pass

    label('loc_CB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_CBC',
    )

    Jump('loc_D6F')

    def _loc_CBC(): pass

    label('loc_CBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_D25',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '明明和昨天同时来的，\n',
            '好的座位却都被占了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来明天的决赛\n',
            '我必须来早一点才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D6F')

    def _loc_D25(): pass

    label('loc_D25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_D2F',
    )

    Jump('loc_D6F')

    def _loc_D2F(): pass

    label('loc_D2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_D5E',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '今年又到了这个时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D6F')

    def _loc_D5E(): pass

    label('loc_D5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_D68',
    )

    Jump('loc_D6F')

    def _loc_D68(): pass

    label('loc_D68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_D6F',
    )

    def _loc_D6F(): pass

    label('loc_D6F')

    TalkEnd(0x00FE)

    Return()

# id: 0x002B offset: 0xD73
@scena.Code('func_2B_D73')
def func_2B_D73():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_D80',
    )

    Jump('loc_E48')

    def _loc_D80(): pass

    label('loc_D80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_D8A',
    )

    Jump('loc_E48')

    def _loc_D8A(): pass

    label('loc_D8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_D94',
    )

    Jump('loc_E48')

    def _loc_D94(): pass

    label('loc_D94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_D9E',
    )

    Jump('loc_E48')

    def _loc_D9E(): pass

    label('loc_D9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_E0F',
    )

    ChrTalk(
        0x00FE,
        (
            '今天大家都来到竞技场\n',
            '为你们呐喊助威。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310111632V作为游击士协会的代表，\n',
            '你们一定要为荣誉而战哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E48')

    def _loc_E0F(): pass

    label('loc_E0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_E19',
    )

    Jump('loc_E48')

    def _loc_E19(): pass

    label('loc_E19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_E23',
    )

    Jump('loc_E48')

    def _loc_E23(): pass

    label('loc_E23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_E2D',
    )

    Jump('loc_E48')

    def _loc_E2D(): pass

    label('loc_E2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_E37',
    )

    Jump('loc_E48')

    def _loc_E37(): pass

    label('loc_E37')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_E41',
    )

    Jump('loc_E48')

    def _loc_E41(): pass

    label('loc_E41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_E48',
    )

    def _loc_E48(): pass

    label('loc_E48')

    TalkEnd(0x00FE)

    Return()

# id: 0x002C offset: 0xE4C
@scena.Code('func_2C_E4C')
def func_2C_E4C():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 3, 0x633)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1019',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 3, 0x633))

    ChrTalk(
        0x0023,
        (
            '#0280111583V#151F啊，是小艾你们啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111584V真厉害～！\n',
            '你们打进决赛了～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111585V我真是兴奋得都要跳起来了～！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111586V#506F哈哈，别这么激动嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111587V#010F如果不静下心来集中精神的话，\n',
            '说不定会错过很多精彩的画面哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#0280111588V#150F哎嘿，不用担心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111589V因为我只有在静不下心的时候\n',
            '才能拍下一些好的照片呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111590V这样才有自然感哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111591V#019F是、是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111592V#007F不愧是朵洛希……\n',
            '完全是个另类的天才。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D4')

    def _loc_1019(): pass

    label('loc_1019')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1060',
    )

    ChrTalk(
        0x0110,
        (
            '#0280111593V#151F小艾你们的精彩表现，\n',
            '我一定会好好拍下来的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D4')

    def _loc_1060(): pass

    label('loc_1060')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_10D4',
    )

    ChrTalk(
        0x0110,
        (
            '#0280111594V#150F嘿嘿，\n',
            '因为我是负责报道的记者，\n',
            '所以拿到了特等席位哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0281080006V好了，要赶快准备好照相机了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10D4(): pass

    label('loc_10D4')

    TalkEnd(0x0023)

    Return()

# id: 0x002D offset: 0x10D8
@scena.Code('func_2D_10D8')
def func_2D_10D8():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 2, 0x632)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13A1',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 2, 0x632))

    ChrTalk(
        0x0022,
        (
            '#0150111565V#130F你们好啊。\n',
            '艾丝蒂尔、约修亚，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111566V#004F哎，是亚鲁瓦教授！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111567V#014F您也来观看比赛吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0150111568V#130F哈哈，\n',
            '因为受了你们好多的照顾嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111569V今天是恩人出战决赛的日子，\n',
            '我想无论如何也要来看一看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111570V#001F嘿嘿，谢谢啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111571V#006F不过，买决赛的门票\n',
            '肯定花了不少米拉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0150111572V#130F哈哈，那也不是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111573V资料馆的馆长突然有急事，\n',
            '不能前来观看比赛了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111574V所以就把这张票免费转让给了我。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111575V#506F什～么啊，果然还是没付钱嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0150111576V#130F哈哈……真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111577V不过，我支持你们的信念\n',
            '是绝对不会输给其他人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111578V请你们一定要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111579V#006F嗯，包在我们身上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111580V#010F我们必定全力出战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1400')

    def _loc_13A1(): pass

    label('loc_13A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1400',
    )

    ChrTalk(
        0x0022,
        (
            '#0150111581V#130F我支持你们的信念\n',
            '是绝对不会输给其他人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111578V请你们一定要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1400(): pass

    label('loc_1400')

    TalkEnd(0x0022)

    Return()

# id: 0x002E offset: 0x1404
@scena.Code('func_2E_1404')
def func_2E_1404():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 4, 0x634)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1922',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 4, 0x634))
    SetChrDirection(0x000C, 90, 0)

    ChrTalk(
        0x000C,
        (
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111597V#004F哎……\n',
            '克鲁茨前辈，你怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x000C, 15, 0, 300, 4000)
    ChrTurnDirection(0x000C, 0x0000, 400)

    ChrTalk(
        0x000C,
        (
            '哎……啊，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330111599V终于到了决赛呢。\n',
            '我很期待你们的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111600V#006F嗯，看我的吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111601V#505F……不过，克鲁茨前辈，\n',
            '你的脸色好像有点不对劲啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111602V#012F是啊。\n',
            '脸色铁青铁青呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '没什么……\n',
            '只是从刚才开始就觉得有点头晕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过奇怪的是……\n',
            '我的身体没有什么事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330111605V……难道是那个时候留下的后遗症……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111606V#580F后、后遗症……\n',
            '难道是说昨天的比赛吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈哈，不是不是。\n',
            '是三个月之前的一次事故。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330111608V那时候我好像执行任务失败了，\n',
            '还弄得自己伤痕累累。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111609V#505F好像执行任务失败了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111610V#012F好像是很模糊的说法啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊啊，不好意思。\n',
            '因为那次事故的记忆确实很模糊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '连那是件什么样的工作\n',
            '也完全记不起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330111613V虽然医生说，\n',
            '这是因事故所受的刺激……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111614V#012F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111615V#003F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111616V#002F不过，以这样的状态来参加比赛，\n',
            '不会有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我刚才已经说了，\n',
            '其实这不是身体上的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯，跟你们说了一会儿话，\n',
            '我感觉比刚才舒服多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330111619V已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111620V#505F是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111621V#010F看起来脸色确实好些了呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111622V不过……\n',
            '请不要勉强硬撑着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330111624V你们今天一定要\n',
            '全力出战获取冠军哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000C, 90, 400)

    Jump('loc_195C')

    def _loc_1922(): pass

    label('loc_1922')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_195C',
    )

    ChrTalk(
        0x00FE,
        (
            '要连我们的份也一起加油，\n',
            '全力出战获取冠军哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_195C(): pass

    label('loc_195C')

    TalkEnd(0x000C)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
