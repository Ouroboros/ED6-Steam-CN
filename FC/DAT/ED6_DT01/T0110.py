import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0110   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0110.x'
    header.mapIndex       = 11
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x0000CB20,
            dword_04        = 0x00000000,
            dword_08        = 0x000280A0,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 11,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00014438,
            dword_04        = 0x00000000,
            dword_08        = 0x0001C520,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 11,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0x11E
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雷特拉',
            x                   = 93326,
            z                   = 0,
            y                   = 162898,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '赛拉',
            x                   = 58084,
            z                   = 0,
            y                   = 198250,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '玛茜婆婆',
            x                   = 51750,
            z                   = 0,
            y                   = 163200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '鲁克',
            x                   = 55045,
            z                   = 0,
            y                   = 164193,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '帕特',
            x                   = 88798,
            z                   = 0,
            y                   = 163093,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '日记',
            x                   = 52700,
            z                   = 700,
            y                   = 161650,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703941,
            chipIndex           = 5,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1DE
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1DE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1DE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 52860,
            triggerZ            = 0,
            triggerY            = 161440,
            triggerRange        = 800,
            actorX              = 52700,
            actorZ              = 700,
            actorY              = 161650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x202
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_211',
    )

    ChrClearFlags(0x000C, 0x0080)

    Jump('loc_227')

    def _loc_211(): pass

    label('loc_211')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_227',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)

    def _loc_227(): pass

    label('loc_227')

    Return()

# id: 0x0001 offset: 0x228
@scena.Code('func_01_228')
def func_01_228():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_240',
    )

    OP_B1('t0110_y')

    Jump('loc_249')

    def _loc_240(): pass

    label('loc_240')

    OP_B1('t0110_n')

    def _loc_249(): pass

    label('loc_249')

    Return()

# id: 0x0002 offset: 0x24A
@scena.Code('func_02_24A')
def func_02_24A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_25F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_24A')

    def _loc_25F(): pass

    label('loc_25F')

    Return()

# id: 0x0003 offset: 0x260
@scena.Code('func_03_260')
def func_03_260():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_283',
    )

    OP_8D(0x00FE, 51000, 165000, 56500, 163300, 2500)

    Jump('func_03_260')

    def _loc_283(): pass

    label('loc_283')

    Return()

# id: 0x0004 offset: 0x284
@scena.Code('func_04_284')
def func_04_284():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2A7',
    )

    OP_8D(0x00FE, 52766, 165023, 56498, 163482, 3000)

    Jump('func_04_284')

    def _loc_2A7(): pass

    label('loc_2A7')

    Return()

# id: 0x0005 offset: 0x2A8
@scena.Code('func_05_2A8')
def func_05_2A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2CB',
    )

    OP_8D(0x00FE, 87700, 161023, 91100, 164700, 3000)

    Jump('func_05_2A8')

    def _loc_2CB(): pass

    label('loc_2CB')

    Return()

# id: 0x0006 offset: 0x2CC
@scena.Code('func_06_2CC')
def func_06_2CC():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_3DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '看了利贝尔通讯\n',
            '才知道最近柏斯相继\n',
            '发生了多宗的盗窃案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起柏斯，\n',
            '那可是王国的经济中心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以说也有不少不法之徒\n',
            '也喜欢在这个城市作案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DA')

    def _loc_37E(): pass

    label('loc_37E')

    ChrTalk(
        0x00FE,
        (
            '说起柏斯，\n',
            '那可是王国的经济中心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以说也有不少不法之徒\n',
            '也喜欢在这个城市作案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DA(): pass

    label('loc_3DA')

    Jump('loc_B7C')

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_445',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来\n',
            '最近利贝尔通讯\n',
            '卖得很火啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不久前原本\n',
            '还只是仅在王都一带\n',
            '发行的小型杂志呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B7C')

    def _loc_445(): pass

    label('loc_445')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_552',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国\n',
            '被两个强大势力夹在中间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '分别是北边的埃雷波尼亚帝国\n',
            '和东边的卡尔瓦德共和国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但值得骄傲的是，\n',
            '王国自建国以来一直保持着独立。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_54F')

    def _loc_4F1(): pass

    label('loc_4F1')

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国\n',
            '被两个强大势力夹在中间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但值得骄傲的是，\n',
            '王国自建国以来一直保持着独立。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54F(): pass

    label('loc_54F')

    Jump('loc_B7C')

    def _loc_552(): pass

    label('loc_552')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_6B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_629',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '这个国家共分五个地区，\n',
            '每个地区都有各自的中心都市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '克劳斯市长就是五大都市之一的\n',
            '洛连特的负责人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他成天优哉游哉地打理庭院，\n',
            '还被人叫作克劳斯爷爷，\n',
            '但其实是个很了不起的人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B2')

    def _loc_629(): pass

    label('loc_629')

    ChrTalk(
        0x00FE,
        (
            '克劳斯市长就是五大都市之一的\n',
            '洛连特的负责人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他成天优哉游哉地打理庭院，\n',
            '还被人叫作克劳斯爷爷，\n',
            '但其实是个很了不起的人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B2(): pass

    label('loc_6B2')

    Jump('loc_B7C')

    def _loc_6B5(): pass

    label('loc_6B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_7CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_76B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '得知帕特去了翡翠之塔，\n',
            '我可是吓了一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这孩子虽然很乖，\n',
            '但小孩子总是好奇心旺盛的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这本身并不是什么坏事，\n',
            '但这次也太出格了，我狠狠骂了他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7CB')

    def _loc_76B(): pass

    label('loc_76B')

    ChrTalk(
        0x00FE,
        (
            '得知帕特去了翡翠之塔，\n',
            '我可是吓了一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这孩子虽然很乖，\n',
            '但小孩子总是好奇心旺盛的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7CB(): pass

    label('loc_7CB')

    Jump('loc_B7C')

    def _loc_7CE(): pass

    label('loc_7CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_90D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_804',
    )

    ChrTalk(
        0x0008,
        (
            '古代文明真是\n',
            '充满神奇的魅力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_90A')

    def _loc_804(): pass

    label('loc_804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8A9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0008,
        (
            '在利贝尔王国有四座巨大的塔，\n',
            '你们知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这四座塔非常的古老，\n',
            '书上记载着它们和\n',
            '古代文明有着密切的联系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '古代文明真是\n',
            '充满神奇的魅力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_90A')

    def _loc_8A9(): pass

    label('loc_8A9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '呼……\n',
            '终于把这本最近一直在找的书给找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不知道为何竟然\n',
            '和帕特的画册混在一起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_90A(): pass

    label('loc_90A')

    Jump('loc_B7C')

    def _loc_90D(): pass

    label('loc_90D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_A68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 3, 0x29B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A3E',
    )

    SetScenaFlags(ScenaFlag(0x0053, 3, 0x29B))

    ChrTalk(
        0x0008,
        (
            '最近因为飞艇来往频繁的缘故，\n',
            '洛连特这里也进了许多好书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因此我经常去店里\n',
            '一本一本地买了来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '待会儿老婆可能又要骂我了，\n',
            '我想我还是小心一点好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这本书是一套小说的第一卷，\n',
            '我就把它送给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0212, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第１卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_A65')

    def _loc_A3E(): pass

    label('loc_A3E')

    ChrTalk(
        0x0008,
        (
            '嗯，我想找的那本书\n',
            '果然不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A65(): pass

    label('loc_A65')

    Jump('loc_B7C')

    def _loc_A68(): pass

    label('loc_A68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B24',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '《王国的荣耀》……\n',
            '《导力器技术概论》……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '《洛连特的历程》……\n',
            '《七耀教会和游击士协会》……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '上次买的那本书\n',
            '到底放在哪里了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看来不好好整理一下不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B7C')

    def _loc_B24(): pass

    label('loc_B24')

    ChrTalk(
        0x0008,
        (
            '嗯～这本是……\n',
            '《吃遍世界之利贝尔篇》？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么搞的……\n',
            '竟然还买过这样一本书？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B7C(): pass

    label('loc_B7C')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0xB80
@scena.Code('func_07_B80')
def func_07_B80():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_BDD',
    )

    ChrTalk(
        0x00FE,
        (
            '最近老公和帕特那孩子\n',
            '多了很多话说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下终于\n',
            '有了家庭温馨的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A1')

    def _loc_BDD(): pass

    label('loc_BDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_CE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C9C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '救了帕特的两位游击士\n',
            '最近好像很活跃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说是一对\n',
            '年轻的男女搭档。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤其是那男孩，\n',
            '主妇们都说他很可爱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F（……难道约修亚是传说中的主妇杀手？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE0')

    def _loc_C9C(): pass

    label('loc_C9C')

    ChrTalk(
        0x00FE,
        (
            '洛连特聚集了不少有名的游击士，\n',
            '托他们的福，\n',
            '我们才能安居乐业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE0(): pass

    label('loc_CE0')

    Jump('loc_11A1')

    def _loc_CE3(): pass

    label('loc_CE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_DAA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D71',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '有个叫尤妮的女孩\n',
            '和帕特很要好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她上主日学校时\n',
            '她爸爸都会接送呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们父女感情真好，\n',
            '真叫人有点羡慕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DA7')

    def _loc_D71(): pass

    label('loc_D71')

    ChrTalk(
        0x00FE,
        (
            '我要不要也去接帕特呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但他可能不愿我去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DA7(): pass

    label('loc_DA7')

    Jump('loc_11A1')

    def _loc_DAA(): pass

    label('loc_DAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_E7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E32',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '不知我家的帕特\n',
            '将来想做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可不希望他也像鲁克那样\n',
            '梦想当什么游击士，\n',
            '最好是选个安全又稳定的职业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7C')

    def _loc_E32(): pass

    label('loc_E32')

    ChrTalk(
        0x00FE,
        (
            '我可不希望我家的孩子\n',
            '梦想当什么游击士，\n',
            '最好是选个安全又稳定的职业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E7C(): pass

    label('loc_E7C')

    Jump('loc_11A1')

    def _loc_E7F(): pass

    label('loc_E7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_F53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F31',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '昨天，\n',
            '全家三口开了个家庭会议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老公也好好\n',
            '批评了帕特一顿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帕特本来\n',
            '就是懂事的孩子，\n',
            '也好好反省过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次对大家来说\n',
            '也是个好教训呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F50')

    def _loc_F31(): pass

    label('loc_F31')

    ChrTalk(
        0x00FE,
        (
            '我们家也终于\n',
            '有点长进了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F50(): pass

    label('loc_F50')

    Jump('loc_11A1')

    def _loc_F53(): pass

    label('loc_F53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1018',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FE7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '我家那孩子\n',
            '刚才又跑到外面的街道去了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我一再的告诫他\n',
            '外面有魔兽出没很危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '回头我一定得让老公\n',
            '好好说说他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1015')

    def _loc_FE7(): pass

    label('loc_FE7')

    ChrTalk(
        0x0009,
        (
            '……看来我\n',
            '必须得开一次\n',
            '家庭会议才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1015(): pass

    label('loc_1015')

    Jump('loc_11A1')

    def _loc_1018(): pass

    label('loc_1018')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_10FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_108D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '我家的帕特\n',
            '一大早就跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '千万不要和鲁克\n',
            '一起去学坏了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F8')

    def _loc_108D(): pass

    label('loc_108D')

    ChrTalk(
        0x0009,
        (
            '而且老公从来不管孩子，\n',
            '只会呆在房间里面\n',
            '不知道干些什么事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '女神啊……\n',
            '家庭要面临崩溃的危机了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10F8(): pass

    label('loc_10F8')

    Jump('loc_11A1')

    def _loc_10FB(): pass

    label('loc_10FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1163',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '咳咳、咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的，\n',
            '老公竟然把书架给弄倒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '弄得屋子里\n',
            '到处都是灰尘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A1')

    def _loc_1163(): pass

    label('loc_1163')

    ChrTalk(
        0x0009,
        (
            '老公竟然\n',
            '把书架给弄倒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '弄得屋子里\n',
            '到处都是灰尘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A1(): pass

    label('loc_11A1')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x11A5
@scena.Code('func_08_11A5')
def func_08_11A5():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_11FF',
    )

    ChrTalk(
        0x00FE,
        (
            '之前没有发觉，\n',
            '我的爸爸\n',
            '懂得很多事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大人们果然\n',
            '都很厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1309')

    def _loc_11FF(): pass

    label('loc_11FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12C2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x000C,
        (
            '艾丝蒂尔姐姐，\n',
            '今天真是谢谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '如果姐姐你们\n',
            '没有来救我们的话，\n',
            '我们不知道会变成什么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我想鲁克也会非常\n',
            '感谢姐姐你们的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '姐姐就别再生他的气了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1309')

    def _loc_12C2(): pass

    label('loc_12C2')

    ChrTalk(
        0x000C,
        (
            '我想鲁克也会非常\n',
            '感谢姐姐你们的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '姐姐就别再生他的气了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1309(): pass

    label('loc_1309')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x130D
@scena.Code('func_09_130D')
def func_09_130D():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1395',
    )

    ChrTalk(
        0x00FE,
        (
            '儿子阿斯顿因为工作关系\n',
            '一直在关所驻守而不能回家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孙子鲁克也是\n',
            '一天到晚只会玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连我也感到\n',
            '真的很寂寞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F1')

    def _loc_1395(): pass

    label('loc_1395')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1410',
    )

    ChrTalk(
        0x00FE,
        (
            '我家的鲁克和邻居家的帕特\n',
            '性格完全是两个极端，\n',
            '但两人却是好朋友呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是鲁克能多学学\n',
            '帕特的优点就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F1')

    def _loc_1410(): pass

    label('loc_1410')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1477',
    )

    ChrTalk(
        0x00FE,
        (
            '上次的主日学校\n',
            '鲁克乖乖地去了，\n',
            '这孩子很少这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道是不是\n',
            '有什么开心的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F1')

    def _loc_1477(): pass

    label('loc_1477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1531',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1507',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我儿子是王国军的士兵哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前曾在王都的部队，\n',
            '现在驻守在\n',
            '西面的威尔特关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望他回来后\n',
            '好好教训教训鲁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_152E')

    def _loc_1507(): pass

    label('loc_1507')

    ChrTalk(
        0x00FE,
        (
            '希望儿子回来后\n',
            '好好教训教训鲁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_152E(): pass

    label('loc_152E')

    Jump('loc_17F1')

    def _loc_1531(): pass

    label('loc_1531')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1583',
    )

    ChrTalk(
        0x00FE,
        (
            '鲁克今天还是\n',
            '飞快地冲出去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他有好好地\n',
            '吸取上次的教训吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F1')

    def _loc_1583(): pass

    label('loc_1583')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1668',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1613',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '我最近太娇惯\n',
            '鲁克这孩子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没有想到他不仅不回家，\n',
            '还跑到翡翠之塔去玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果不是因为有\n',
            '游击士及时赶到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1665')

    def _loc_1613(): pass

    label('loc_1613')

    ChrTalk(
        0x000A,
        (
            '这都是因为我\n',
            '太娇惯他的缘故啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '等我儿子回来之后，\n',
            '一定要好好商量一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1665(): pass

    label('loc_1665')

    Jump('loc_17F1')

    def _loc_1668(): pass

    label('loc_1668')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1741',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16ED',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '鲁克就算是回家了，\n',
            '不一会儿又会飞跑出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '马上就到\n',
            '吃饭的时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是一个静不下来的孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173E')

    def _loc_16ED(): pass

    label('loc_16ED')

    ChrTalk(
        0x000A,
        (
            '鲁克就算是回家了，\n',
            '不一会儿又会飞跑出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是一个静不下来的孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_173E(): pass

    label('loc_173E')

    Jump('loc_17F1')

    def _loc_1741(): pass

    label('loc_1741')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17A9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '那个孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '鲁克那孩子\n',
            '到底跑到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '早饭也没有吃\n',
            '就飞跑了出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F1')

    def _loc_17A9(): pass

    label('loc_17A9')

    ChrTalk(
        0x000A,
        (
            '鲁克那孩子\n',
            '到底跑到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '早饭也没有吃\n',
            '就飞跑了出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17F1(): pass

    label('loc_17F1')

    TalkEnd(0x000A)

    Return()

# id: 0x000A offset: 0x17F5
@scena.Code('func_0A_17F5')
def func_0A_17F5():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1896',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x000B,
        (
            '哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '还是要谢谢\n',
            '你们救了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '而且……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '虽然不服气，\n',
            '但艾丝蒂尔你真的很厉害哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '虽然还远远比不上\n',
            '卡西乌斯叔叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C3')

    def _loc_1896(): pass

    label('loc_1896')

    ChrTalk(
        0x000B,
        (
            '决定了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我一定要\n',
            '成为一名游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18C3(): pass

    label('loc_18C3')

    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0x18C7
@scena.Code('func_0B_18C7')
def func_0B_18C7():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '桌子上放着一个笔记本。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '【阅读】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1965',
    )

    OP_B9(0x0376, 0x0000)

    def _loc_1965(): pass

    label('loc_1965')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
