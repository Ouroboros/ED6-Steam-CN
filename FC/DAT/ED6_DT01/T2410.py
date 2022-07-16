import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2410   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特蕾莎院长'),
    TXT(0x02, '达尼艾尔'),
    TXT(0x03, '玛丽'),
    TXT(0x04, '克拉姆'),
    TXT(0x05, '波利'),
    TXT(0x06, '壶'),
    TXT(0x07, '红茶'),
    TXT(0x08, '红茶'),
    TXT(0x09, '红茶'),
    TXT(0x0A, '红茶'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2410.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x144B
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH02573._CH', 'ED6_DT07/CH02573P._CP'),
    ]

# id: 0x10002 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -3700,
            z                   = 0,
            y                   = 14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 35100,
            z                   = 0,
            y                   = 2300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 35300,
            z                   = 0,
            y                   = -35300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -3400,
            z                   = 0,
            y                   = 1700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 32500,
            z                   = 0,
            y                   = -34400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703944,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638408,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638408,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638408,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638408,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x242
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x242
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x242
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x242
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_24C',
    )

    Jump('loc_28A')

    def _loc_24C(): pass

    label('loc_24C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_256',
    )

    Jump('loc_28A')

    def _loc_256(): pass

    label('loc_256')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 0, 0x420)),
            Expr.Return,
        ),
        'loc_260',
    )

    Jump('loc_28A')

    def _loc_260(): pass

    label('loc_260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_26A',
    )

    Jump('loc_28A')

    def _loc_26A(): pass

    label('loc_26A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_279',
    )

    ClearChrFlags(0x000B, 0x0080)

    Jump('loc_28A')

    def _loc_279(): pass

    label('loc_279')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 0, 0x410)),
            Expr.Return,
        ),
        'loc_283',
    )

    Jump('loc_28A')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_28A',
    )

    def _loc_28A(): pass

    label('loc_28A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_298',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0008)

    def _loc_298(): pass

    label('loc_298')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_2AF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0009)

    def _loc_2AF(): pass

    label('loc_2AF')

    Return()

# id: 0x0001 offset: 0x2B0
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x2B1
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2C6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2C6(): pass

    label('loc_2C6')

    Return()

# id: 0x0003 offset: 0x2C7
@scena.Code('func_03_2C7')
def func_03_2C7():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_369',
    )

    ChrTalk(
        0x0008,
        (
            '#0390040854V#750F那些孩子也都很喜欢热闹，\n',
            '你们有空一定要过来玩哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040855V这里也没什么别的东西能招待你们……\n',
            '我会准备好香草茶和点心，\n',
            '等你们过来品尝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_369(): pass

    label('loc_369')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x36D
@scena.Code('func_04_36D')
def func_04_36D():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_3BD',
    )

    ChrTalk(
        0x00FE,
        (
            '#0400040906V#770F科洛丝姐姐，\n',
            '下次再来玩啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040907V大家都盼望着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BD(): pass

    label('loc_3BD')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0x3C1
@scena.Code('func_05_3C1')
def func_05_3C1():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_41A',
    )

    ChrTalk(
        0x00FE,
        (
            '#0420040856V科洛丝姐姐做的\n',
            '苹果派最好吃了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0420040857V不管有多少我都能吃下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41A(): pass

    label('loc_41A')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x41E
@scena.Code('func_06_41E')
def func_06_41E():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_458',
    )

    ChrTalk(
        0x00FE,
        (
            '#0430040858V艾丝蒂尔和约修亚，\n',
            '你们要再来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_458(): pass

    label('loc_458')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0x45C
@scena.Code('func_07_45C')
def func_07_45C():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_4D9',
    )

    ChrTalk(
        0x00FE,
        (
            '#0410040859V我们院的克拉姆给你们添麻烦了，\n',
            '真是对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410040860V那孩子\n',
            '总是这个样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410040861V真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D9(): pass

    label('loc_4D9')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x4DD
@scena.Code('func_08_4DD')
def func_08_4DD():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0136, 0x0004)
    SetChrChipByIndex(0x0101, 5)
    SetChrChipByIndex(0x0102, 6)
    SetChrChipByIndex(0x0136, 7)
    SetChrPos(0x0101, -5240, 200, 7350, 90)
    SetChrPos(0x0102, -5240, 200, 6050, 90)
    SetChrPos(0x0136, -2550, 200, 6100, 270)
    SetChrPos(0x0008, -2550, 200, 7350, 270)
    SetChrChipByIndex(0x0008, 10)
    OP_4A(0x0008, 255)
    SetChrPos(0x000D, -4100, 750, 5310, 0)
    SetChrPos(0x000E, -4550, 700, 6860, 0)
    SetChrPos(0x000F, -4530, 700, 6060, 0)
    SetChrPos(0x0010, -3810, 700, 6860, 0)
    SetChrPos(0x0011, -3710, 700, 6060, 0)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    CameraMove(-2580, 0, 14700, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在特蕾莎院长的款待之下，\n',
            '艾丝蒂尔他们一边喝茶吃苹果派，\n',
            '一边做自我介绍并说出之前发生的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1500, 0)
    CameraMove(-3770, 100, 7530, 3000)

    ChrTalk(
        0x0008,
        (
            '#0390040764V#756F原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040765V那孩子本性并不坏，\n',
            '只是喜欢恶作剧而且做事又欠考虑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040766V#754F真是非常抱歉。\n',
            '我作为他的监护人也感到十分羞愧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040767V#000F啊，已经没事了。\n',
            '反正他已经把徽章还给我们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040768V#001F而且还喝到这么棒的香草茶，\n',
            '吃上这么美味的苹果派。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040769V#750F呵呵，你们太过奖了。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040770V#010F不过，这茶真的是非常清甜可口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040771V和玛诺利亚村旅馆的\n',
            '香草茶同样美味。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040772V这难道是从外面\n',
            '那些茶树上采下的茶叶吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040773V#750F嗯。\n',
            '栽种茶树算是我的兴趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040774V而且承蒙旅馆老板的好意，\n',
            '他经常到我们这里收购茶叶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040775V#501F原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040776V刚才吃的苹果派\n',
            '味道也很棒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040777V#751F呵呵，那不是我做的，\n',
            '而是这孩子亲手做的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040778V#004F啊，科洛丝吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040779V#045F真是不好意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040780V#043F那个……\n',
            '刚才实在是太失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040781V我并不是有意的，\n',
            '只是听到那孩子的叫嚷才会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040782V#006F不要放在心上啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040783V我抓到那孩子的时候，\n',
            '自己也有点太过冲动了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040784V不过呢，\n',
            '那只白鹰真是差点把我吓坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040785V#040F啊，你说的是基库吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040786V它是只白隼哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040787V#010F白隼……\n',
            '是利贝尔的国鸟吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040788V看得出它经过了严格训练。\n',
            '是你的宠物吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040789V#041F呵呵，\n',
            '其实并不是我饲养的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040790V应该说我们是好朋友吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040791V#004F哇～你有这么厉害的朋友啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040792V#000F话说回来，\n',
            '科洛丝你是杰尼丝王立学院的学生吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040793V为什么你会住在这里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040794V#040F不是呢……\n',
            '我是住在学院宿舍里面的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040795V因为学院离这里不远，\n',
            '所以我经常在休息的时候来玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040796V#045F也给老师添了很多麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 1)

    ChrTalk(
        0x0008,
        (
            '#0390040797V#751F哎呀哎呀。\n',
            '哪里有给我添麻烦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040798V你每次来都帮我做家务，\n',
            '是我给你添麻烦才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040799V而且看到你来，孩子们都很开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0136, 2)

    ChrTalk(
        0x0136,
        (
            '#0060040800V#040F特蕾莎老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040801V#750F不过，可不要为了经常来这里\n',
            '而影响了学院的生活哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040802V呵呵，我可能是多说了，\n',
            '不过你不会让我这么担心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040803V#045F嗯，我会铭记于心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040804V#501F啊，学院生活……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040805V我也想体验一下呢，\n',
            '就算只有一次也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040806V#010F我也有同感。\n',
            '毕竟主日学校一个星期才上一次课。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040807V不过，我听说王立学院的\n',
            '入学考试不是一般的难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040808V#007F唉，要是我去考试，\n',
            '肯定没法通过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    Sleep(300)

    SetChrSubChip(0x0136, 0)

    ChrTalk(
        0x0136,
        (
            '#0060040809V#040F呵呵，没有这回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040810V我倒是觉得要成为游击士\n',
            '才不是一般的难呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040811V#041F而且这么年轻就……\n',
            '是我该羡慕你们才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040812V#008F嘿嘿……\n',
            '我都被你说得难为情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040813V说是游击士，\n',
            '其实我们只是见习的而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040814V#010F为了能成为独当一面的游击士，\n',
            '我们正在到王国各地修行的途中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040815V最近正打算在\n',
            '卢安地区进行活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040816V#750F这样啊，说不定以后\n',
            '还会有需要你们照顾的地方呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040817V#751F那些孩子也都很喜欢热闹，\n',
            '你们有空一定要过来玩哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040818V我会准备好香草茶和点心，\n',
            '等你们过来品尝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2400._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x110D
@scena.Code('func_09_110D')
def func_09_110D():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0083, 4, 0x41C))
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0009, 37220, 0, -33090, 180)
    SetChrPos(0x000A, 37310, 1700, -33090, 180)
    SetChrPos(0x000C, 37220, 0, -36830, 180)
    SetChrPos(0x000B, 37220, 1700, -36830, 180)
    SetChrPos(0x0008, 36300, 0, 42360, 270)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x0008, 255)
    CameraMove(38522, 0, -31220, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(500, 0)
    CameraMove(35522, 0, -34220, 3000)
    Sleep(2000)

    Fade(1000)
    CameraMove(36570, 0, 42820, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0390930011V#750F呵呵，要修补的东西还真多，\n',
            '这也说明孩子们的精力都很旺盛吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050002V好了，差不多该休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    SetChrPos(0x0008, 35780, 0, 42330, 270)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_12A1')
    def lambda_12A1():
        CameraMove(35930, 0, 43280, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_12A1)

    ChrWalkTo(0x0008, 34780, 0, 42310, 1000, 0x00)
    ChrWalkTo(0x0008, 34380, 0, 43600, 1000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0390050003V#754F女神啊， \n',
            '请赐予这些孩子健康的明天吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在这里能渐渐听到火苗燃烧的声音＃',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0390050004V#753F这是什么声音？\n',
            '好像是柴火的声音……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050005V#753F……还有这气味是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0008, 180, 500)

    ChrTalk(
        0x0008,
        (
            '#0390050006V#755F………………难道！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T2400._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
