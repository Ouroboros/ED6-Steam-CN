import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1400   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1400.x'
    header.mapIndex       = 60
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xF11
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFF55B0,
            dword_04        = 0xFFFFFF74,
            dword_08        = 0x00005FB4,
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
            word_3A         = 60,
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
        ('ED6_DT09/CH10170._CH', 'ED6_DT09/CH10170P._CP'),
        ('ED6_DT09/CH10171._CH', 'ED6_DT09/CH10171P._CP'),
        ('ED6_DT09/CH11170._CH', 'ED6_DT09/CH11170P._CP'),
        ('ED6_DT09/CH11171._CH', 'ED6_DT09/CH11171P._CP'),
        ('ED6_DT09/CH11180._CH', 'ED6_DT09/CH11180P._CP'),
        ('ED6_DT09/CH11181._CH', 'ED6_DT09/CH11181P._CP'),
        ('ED6_DT09/CH11190._CH', 'ED6_DT09/CH11190P._CP'),
        ('ED6_DT09/CH11191._CH', 'ED6_DT09/CH11191P._CP'),
        ('ED6_DT09/CH10840._CH', 'ED6_DT09/CH10840P._CP'),
        ('ED6_DT09/CH10841._CH', 'ED6_DT09/CH10841P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -67060,
            z                   = -50,
            y                   = 102230,
            direction           = 143,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -68750,
            z           = 50,
            y           = 92910,
            word_0C     = 0x007F,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -84390,
            z           = -40,
            y           = 90590,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -112800,
            z           = -50,
            y           = 104070,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00BE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -86000,
            z           = 2020,
            y           = 104050,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -91980,
            z           = 2080,
            y           = 122080,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -78470,
            z           = 4059,
            y           = 133110,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -61710,
            z           = 4050,
            y           = 112490,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -46460,
            z           = 4080,
            y           = 83320,
            word_0C     = 0x00C6,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00C6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1FA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -65700,
            y           = 200,
            z           = 101220,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10005 offset: 0x21A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -86770,
            triggerZ            = 100,
            triggerY            = 113690,
            triggerRange        = 1500,
            actorX              = -86770,
            actorZ              = 1600,
            actorY              = 113690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -78820,
            triggerZ            = 90,
            triggerY            = 98230,
            triggerRange        = 1000,
            actorX              = -78790,
            actorZ              = 1590,
            actorY              = 97650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x262
@scena.Code('PreInit')
def PreInit():
    SetMapFlags(0x00000010)
    OP_11(0xFF, 0xFF, 0xFF, 33000, 54000, 0)

    Return()

# id: 0x0001 offset: 0x278
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 2, 0x362)),
            Expr.Return,
        ),
        'loc_288',
    )

    OP_71(0x0000, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_288(): pass

    label('loc_288')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 6, 0x376)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29A',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2A1')

    def _loc_29A(): pass

    label('loc_29A')

    OP_6F(0x0002, 60)

    def _loc_2A1(): pass

    label('loc_2A1')

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 5, 0x30D)),
            (Expr.Eval, "OP_29(0x0016, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0016, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 7, 0x387)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CF',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_2CF(): pass

    label('loc_2CF')

    Return()

# id: 0x0002 offset: 0x2D0
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2E5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2E5(): pass

    label('loc_2E5')

    Return()

# id: 0x0003 offset: 0x2E6
@scena.Code('func_03_2E6')
def func_03_2E6():
    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x02)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0011, 0x01, 0x0004)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3D4',
    )

    SetMapFlags(0x08000000)
    OP_28(0x0011, 0x01, 0x8000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 2, 0x362)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C9',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_377',
    )

    OP_71(0x0000, 0x0004)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x006C, 2, 0x362))

    Jump('loc_3C9')

    def _loc_377(): pass

    label('loc_377')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '发现了，\n',
            (TxtCtl.SetColor, 0x0),
            '不过现有的数量太多，不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_3C9(): pass

    label('loc_3C9')

    ClearMapFlags(0x08000000)
    TalkEnd(0x00FF)

    Jump('loc_B30')

    def _loc_3D4(): pass

    label('loc_3D4')

    OP_28(0x0011, 0x01, 0x0004)
    SetMapFlags(0x08000000)
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -86760, 110, 114850, 180)
    SetChrPos(0x0102, -87680, 70, 115430, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_427',
    )

    SetChrPos(0x0103, -85440, 180, 115460, 180)

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_446',
    )

    SetChrPos(0x0104, -86320, 140, 116900, 180)

    def _loc_446(): pass

    label('loc_446')

    OP_69(0x0101, 0)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 2, 0x362)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_509',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_4B7',
    )

    OP_71(0x0000, 0x0004)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x006C, 2, 0x362))

    Jump('loc_509')

    def _loc_4B7(): pass

    label('loc_4B7')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '发现了，\n',
            (TxtCtl.SetColor, 0x0),
            '不过现有的数量太多，不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_509(): pass

    label('loc_509')

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_9FE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010150990V#000F呼，终～于找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150991V接下来要做的就是\n',
            '把这个地方告诉超市的老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_628',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030150992V#020F那么，艾丝蒂尔，\n',
            '我问你一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030150993V你知道这里是什么地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150994V#502F嘿嘿，\n',
            '雪拉姐的问题真无聊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150995V『蜜猪峡谷』，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B2')

    def _loc_628(): pass

    label('loc_628')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150996V#014F艾丝蒂尔，\n',
            '你知道这个地方叫什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150997V#502F真是的，别把我当傻瓜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150995V『蜜猪峡谷』，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B2(): pass

    label('loc_6B2')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_771',
    )

    ChrTalk(
        0x0102,
        (
            '#0020150999V#015F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040151000V#030F哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040151001V不管怎么说\n',
            '真是个能引起食欲的名字啊。　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151002V#017F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151003V这里叫『迷雾峡谷』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_869')

    def _loc_771(): pass

    label('loc_771')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_816',
    )

    ChrTalk(
        0x0102,
        (
            '#0020150999V#015F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151005V#027F……真是个非常美味的名字啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151002V#017F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151003V这里叫『迷雾峡谷』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_869')

    def _loc_816(): pass

    label('loc_816')

    ChrTalk(
        0x0102,
        (
            '#0020150486V#018F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151009V#018F艾丝蒂尔……\n',
            '这里叫『迷雾峡谷』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_869(): pass

    label('loc_869')

    ChrTalk(
        0x0101,
        (
            '#0010151010V#008F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030151011V#025F……还好事先问了你一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_8F4')

    def _loc_8C3(): pass

    label('loc_8C3')

    ChrTalk(
        0x0102,
        (
            '#0020151012V#015F……还好事先问了你一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_8F4(): pass

    label('loc_8F4')

    ChrTalk(
        0x0101,
        (
            '#0010151013V#009F这、这也是没办法的事情啊，\n',
            '人家正处于生长发育旺盛的时期嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151014V#018F这算什么理由啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151015V#008F好、好啦好啦，\n',
            '我们这是在工作中啊，工作中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151016V快点出发吧，好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)

    ChrTalk(
        0x0102,
        (
            '#0020151017V#017F真拿你没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B29')

    def _loc_9FE(): pass

    label('loc_9FE')

    ChrTalk(
        0x0101,
        (
            '#0010151018V#000F嗯～这是『熊刺草』呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151019V说起来……\n',
            '好像有谁正在找这个东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ABA',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151020V#020F不是在公告板上写着的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151021V看看手册里的记载吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_B0D')

    def _loc_ABA(): pass

    label('loc_ABA')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151022V#010F是在公告板上写着的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151023V看看手册里的记载吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_B0D(): pass

    label('loc_B0D')

    ChrTalk(
        0x0101,
        (
            '#0010151024V#006F嗯，好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_B29(): pass

    label('loc_B29')

    EventEnd(0x00)
    ClearMapFlags(0x08000000)
    def _loc_B30(): pass

    label('loc_B30')

    Return()

# id: 0x0004 offset: 0xB31
@scena.Code('func_04_B31')
def func_04_B31():
    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
            TxtCtl.Enter,
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
        32,
        0,
        (
            TXT(0x00, '【消灭它】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_C16'),
        (-1, 'loc_CB0'),
    )

    def _loc_C16(): pass

    label('loc_C16')

    Fade(1000)
    SetChrPos(0x0000, -62850, 1270, 98430, 319)
    SetChrPos(0x0001, -62850, 1270, 98430, 319)
    SetChrPos(0x0002, -62850, 1270, 98430, 319)
    SetChrPos(0x0003, -62850, 1270, 98430, 319)
    SetChrPos(0x0004, -62850, 1270, 98430, 319)
    SetChrPos(0x0005, -62850, 1270, 98430, 319)
    SetChrPos(0x0006, -62850, 1270, 98430, 319)
    SetChrPos(0x0007, -62850, 1270, 98430, 319)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_CB0(): pass

    label('loc_CB0')

    Battle(0x000003F8, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrPos(0x0000, -62850, 1270, 98430, 319)
    SetChrPos(0x0001, -62850, 1270, 98430, 319)
    SetChrPos(0x0002, -62850, 1270, 98430, 319)
    SetChrPos(0x0003, -62850, 1270, 98430, 319)
    SetChrPos(0x0004, -62850, 1270, 98430, 319)
    SetChrPos(0x0005, -62850, 1270, 98430, 319)
    SetChrPos(0x0006, -62850, 1270, 98430, 319)
    SetChrPos(0x0007, -62850, 1270, 98430, 319)
    OP_69(0x0000, 0)
    OP_30(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_D5E'),
        (0x00000001, 'loc_D61'),
        (-1, 'loc_D64'),
    )

    def _loc_D5E(): pass

    label('loc_D5E')

    EventEnd(0x00)

    Return()

    def _loc_D61(): pass

    label('loc_D61')

    OP_B4(0x00)

    Return()

    def _loc_D64(): pass

    label('loc_D64')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '成功消灭了迷雾峡谷中被通缉的魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0016, 0x04, 0x10)
    OP_28(0x0016, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x0070, 7, 0x387))
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xDDD
@scena.Code('func_05_DDD')
def func_05_DDD():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 6, 0x376)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EC1',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x0022, 1)"),
            Expr.Return,
        ),
        'loc_E4F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '拳剑',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x006E, 6, 0x376))

    Jump('loc_EBE')

    def _loc_E4F(): pass

    label('loc_E4F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '拳剑',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '拳剑',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_EBE(): pass

    label('loc_EBE')

    Jump('loc_EF7')

    def _loc_EC1(): pass

    label('loc_EC1')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x15)
    def _loc_EF7(): pass

    label('loc_EF7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
