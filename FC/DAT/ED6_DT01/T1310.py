import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1310   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '赛罗斯副长'),
    TXT(0x02, '士兵阿萨'),
    TXT(0x03, '赛尔斯特队长'),
    TXT(0x04, '亚妮拉丝'),
    TXT(0x05, '士兵艾格尔'),
    TXT(0x06, '士兵迈奇'),
    TXT(0x07, '士兵卡多尔斯'),
    TXT(0x08, '器皿'),
    TXT(0x09, '器皿'),
    TXT(0x0A, '咖啡'),
    TXT(0x0B, '咖啡'),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1310.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4CC9
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x0000BB80,
            dword_04        = 0xFFFFF448,
            dword_08        = 0x00006978,
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
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20008._CH', 'ED6_DT06/CH20008P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 19990,
            z                   = 0,
            y                   = 22490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 22000,
            z                   = 0,
            y                   = 9500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 79860,
            z                   = 0,
            y                   = 13400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 21900,
            z                   = 0,
            y                   = 22100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 19990,
            z                   = 0,
            y                   = 7950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 76700,
            z                   = 0,
            y                   = 7590,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 25000,
            z                   = 0,
            y                   = 10500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65541,
            chipIndex           = 5,
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
            dword_10            = 65541,
            chipIndex           = 5,
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
            dword_10            = 1572869,
            chipIndex           = 5,
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
            dword_10            = 1572869,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x24A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x24A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 21950,
            triggerZ            = 0,
            triggerY            = 22540,
            triggerRange        = 400,
            actorX              = 19990,
            actorZ              = 1500,
            actorY              = 22490,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22050,
            triggerZ            = 0,
            triggerY            = 7990,
            triggerRange        = 400,
            actorX              = 19990,
            actorZ              = 1500,
            actorY              = 7950,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18440,
            triggerZ            = 0,
            triggerY            = 12120,
            triggerRange        = 1000,
            actorX              = 18440,
            actorZ              = 1000,
            actorY              = 12120,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2B6
@scena.Code('PreInit')
def PreInit():
    StopEffect(0x80, 0x00)
    SetScenaFlags(ScenaFlag(0x006D, 3, 0x36B))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_2F7',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    SetChrPos(0x000A, 20390, 0, 10700, 180)
    SetChrPos(0x000E, 79990, 0, 13380, 0)

    Jump('loc_3C8')

    def _loc_2F7(): pass

    label('loc_2F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_321',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    SetChrPos(0x000A, 20390, 0, 10700, 180)

    Jump('loc_3C8')

    def _loc_321(): pass

    label('loc_321')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_34B',
    )

    SetChrPos(0x000A, 20390, 0, 10700, 180)
    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)

    Jump('loc_3C8')

    def _loc_34B(): pass

    label('loc_34B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Return,
        ),
        'loc_364',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x000C, 0x0080)

    Jump('loc_3C8')

    def _loc_364(): pass

    label('loc_364')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_378',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)

    Jump('loc_3C8')

    def _loc_378(): pass

    label('loc_378')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_391',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x000C, 0x0080)

    Jump('loc_3C8')

    def _loc_391(): pass

    label('loc_391')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_3AA',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0008)

    Jump('loc_3C8')

    def _loc_3AA(): pass

    label('loc_3AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_3BE',
    )

    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0008)

    Jump('loc_3C8')

    def _loc_3BE(): pass

    label('loc_3BE')

    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0008)

    def _loc_3C8(): pass

    label('loc_3C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3D6',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000D)

    def _loc_3D6(): pass

    label('loc_3D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_3F6',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_B1('t1310_n')
    Event(0, 0x000E)

    def _loc_3F6(): pass

    label('loc_3F6')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_402'),
        (-1, 'loc_415'),
    )

    def _loc_402(): pass

    label('loc_402')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 5, 0x405)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 4, 0x404)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_412',
    )

    Event(0, 0x000C)

    def _loc_412(): pass

    label('loc_412')

    Jump('loc_415')

    def _loc_415(): pass

    label('loc_415')

    Return()

# id: 0x0001 offset: 0x416
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 2, 0x402)),
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_42E',
    )

    OP_B1('t1310_y')

    Jump('loc_437')

    def _loc_42E(): pass

    label('loc_42E')

    OP_B1('t1310_n')

    def _loc_437(): pass

    label('loc_437')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Return,
        ),
        'loc_44F',
    )

    OP_1B(0x00, 0x00, 0x000F)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 99)

    def _loc_44F(): pass

    label('loc_44F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_45D',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_483')

    def _loc_45D(): pass

    label('loc_45D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Return,
        ),
        'loc_467',
    )

    Jump('loc_483')

    def _loc_467(): pass

    label('loc_467')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_475',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_483')

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_47F',
    )

    Jump('loc_483')

    def _loc_47F(): pass

    label('loc_47F')

    OP_64(0x01, 0x0001)

    def _loc_483(): pass

    label('loc_483')

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x4CD
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4E2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_4E2(): pass

    label('loc_4E2')

    Return()

# id: 0x0003 offset: 0x4E3
@scena.Code('func_03_4E3')
def func_03_4E3():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x4E8
@scena.Code('func_04_4E8')
def func_04_4E8():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_526',
    )

    ChrTalk(
        0x0008,
        (
            '嗯，今天用野菜作为原料，\n',
            '来挑战新的菜式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1215')

    def _loc_526(): pass

    label('loc_526')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_58A',
    )

    ChrTalk(
        0x0008,
        (
            '哦……\n',
            '从卢安订购的鱼好像运过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今晚就稍微奢侈一下，\n',
            '给大家振奋一下士气吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1215')

    def _loc_58A(): pass

    label('loc_58A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_5E8',
    )

    ChrTalk(
        0x0008,
        (
            '自那以后，\n',
            '袭击这里的魔兽再也没有出现过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果然，\n',
            '不是住在这一带的魔兽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1215')

    def _loc_5E8(): pass

    label('loc_5E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_633',
    )

    ChrTalk(
        0x0008,
        (
            '哦，你们不就是游击士的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么了，\n',
            '来这里有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1215')

    def _loc_633(): pass

    label('loc_633')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_EAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE2',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_69(0x0008, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 6, 0x446)),
            Expr.Return,
        ),
        'loc_683',
    )

    ChrTalk(
        0x0008,
        (
            '啊呀，怎么了。\n',
            '现在办理通行手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A14')

    def _loc_683(): pass

    label('loc_683')

    ChrTalk(
        0x0101,
        (
            '#0010040332V#001F士兵先生，早上好～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040333V#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040334V哦，早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040335V昨天真的是\n',
            '辛苦你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040336V#008F嘿嘿，没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040337V士兵先生你们呢？\n',
            '后来巡逻的时候\n',
            '没有发生什么事情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040338V啊啊。\n',
            '之后一切正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040339V不过……有一点比较奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040340V#501F奇怪……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040341V街道和关所附近的照明设施\n',
            '有驱赶魔兽的防御效果，\n',
            '这点你们应该很清楚的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040342V就算魔兽真的靠近了关所，\n',
            '充其量也只有两三只。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040343V但是昨天却来了一大群，\n',
            '这种情况我们还是第一次遇到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040344V#012F这样说来的确是有点奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040345V呵呵，不过比起那些帝国军，\n',
            '这些魔兽还算挺可爱的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040346V就把这次骚动\n',
            '当成防卫关所的演习好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040347V#004F这、这样没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040348V对于我们来说，\n',
            '帝国那边的动静才是最令人担心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040349V至于魔兽之类的，\n',
            '还是交给你们游击士处理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040350V那么……\n',
            '你们也该出发了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040351V现在办理通行手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A14(): pass

    label('loc_A14')

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
        0,
        (
            TXT(0x00, '【办理通行手续】\n'),
            TXT(0x01, '【还是算了】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_A83'),
        (0x00000000, 'loc_AB3'),
        (-1, 'loc_DDF'),
    )

    def _loc_A83(): pass

    label('loc_A83')

    ChrTalk(
        0x0008,
        (
            '#1440040352V准备好了的话\n',
            '随时都可以来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0088, 6, 0x446))
    EventEnd(0x01)

    Jump('loc_DDF')

    def _loc_AB3(): pass

    label('loc_AB3')

    ChrTalk(
        0x0102,
        (
            '#0020040353V#010F是的，麻烦您了。',
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
            '通往卢安地区的通行手续已经办理完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#1440040354V……这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040355V然后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 90, 400)
    Sleep(300)

    @scena.Lambda('lambda_0B63')
    def lambda_0B63():
        CameraMove(23120, 0, 24400, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B63)

    WaitForThreadExit(0x0101, 0x0003)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '副长操作开关装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_70(0x0002, 100)
    ChrTurnDirectionByPos(0x0000, 23120, 24400, 400)
    ChrTurnDirectionByPos(0x0001, 23120, 24400, 400)
    OP_73(0x0002)

    @scena.Lambda('lambda_0BDC')
    def lambda_0BDC():
        ChrTurnDirection(0x0008, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BDC)

    OP_69(0x0008, 1500)

    ChrTalk(
        0x0008,
        (
            '#1440040356V碧海白花环抱的卢安\n',
            '欢迎你们的到来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040357V对了对了，\n',
            '小姑娘你们是不是打算去卢安市？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C57')
    def lambda_0C57():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0C57)

    ChrTurnDirection(0x0001, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040358V#000F嗯，我们正想去那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040359V那就麻烦你们把昨天的情况\n',
            '向卢安的支部报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040360V军队也会支付相应的酬金的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040361V#004F啊，这样可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040362V呵呵，\n',
            '这些酬金你们就和阿加特平分吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040363V那么后会有期，\n',
            '期待你们早日成为正游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040364V#001F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040365V#010F承蒙你们多方关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0080, 7, 0x407))
    OP_28(0x003A, 0x04, 0x10)
    OP_28(0x003A, 0x01, 0x0004)
    OP_28(0x0011, 0x04, 0x40)
    OP_28(0x0013, 0x04, 0x40)
    OP_1B(0x00, 0x00, 0x000F)
    NewScene('ED6_DT01/T1300._SN', 101, 0, 0)
    IdleLoop()

    def _loc_DDF(): pass

    label('loc_DDF')

    Jump('loc_EA8')

    def _loc_DE2(): pass

    label('loc_DE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E57',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '啊，是你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那就麻烦你们把昨天的情况\n',
            '向卢安的支部报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '去卢安的路上要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA8')

    def _loc_E57(): pass

    label('loc_E57')

    ChrTalk(
        0x0008,
        (
            '那就麻烦你们把昨天的情况\n',
            '向卢安的支部报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '去卢安的路上要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EA8(): pass

    label('loc_EA8')

    Jump('loc_1215')

    def _loc_EAB(): pass

    label('loc_EAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_EEE',
    )

    ChrTalk(
        0x0008,
        (
            '啊，\n',
            '这种时间还到这里来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '外面已经很冷了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1215')

    def _loc_EEE(): pass

    label('loc_EEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_101D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FBF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '不管多么习惯旅行在外，\n',
            '晚上在这一带行走还是非常危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '山路崎岖，而且魔兽也多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说起来很奇怪的是，\n',
            '最近经常会看到有首领带领的魔兽群体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那可是至今为止都没有见过的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101A')

    def _loc_FBF(): pass

    label('loc_FBF')

    ChrTalk(
        0x0008,
        (
            '最近很奇怪的是，\n',
            '经常会看到有首领带领的魔兽群体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那可是至今为止都没有见过的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_101A(): pass

    label('loc_101A')

    Jump('loc_1215')

    def _loc_101D(): pass

    label('loc_101D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1090',
    )

    ChrTalk(
        0x0008,
        (
            '我有义务\n',
            '让士兵们平时保持\n',
            '六个小时以上的睡眠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '睡眠不足的话，\n',
            '就无法将自己的实力好好发挥出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1215')

    def _loc_1090(): pass

    label('loc_1090')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_119A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_113D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '别看我这个样子，\n',
            '我可以非常喜欢烹饪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会经常请求队长，\n',
            '让我在这里烧菜做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '顺带一提，\n',
            '那边有供旅行者专用的房间，\n',
            '你们可以随时使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1197')

    def _loc_113D(): pass

    label('loc_113D')

    ChrTalk(
        0x0008,
        (
            '别看我这个样子，\n',
            '我可以非常喜欢烹饪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会经常请求队长，\n',
            '让我在这里炒菜做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1197(): pass

    label('loc_1197')

    Jump('loc_1215')

    def _loc_119A(): pass

    label('loc_119A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1215',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11FB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '啊，\n',
            '小姑娘你们要去卢安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要去卢安的话，\n',
            '必须要有通行许可证……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1215')

    def _loc_11FB(): pass

    label('loc_11FB')

    ChrTalk(
        0x0008,
        (
            '啊，你们要去卢安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1215(): pass

    label('loc_1215')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x1219
@scena.Code('func_05_1219')
def func_05_1219():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1253',
    )

    ChrTalk(
        0x00FE,
        (
            '堡垒的人最近\n',
            '总是谈论市长被捕这个话题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1725')

    def _loc_1253(): pass

    label('loc_1253')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_1322',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12D7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '今天本该轮到\n',
            '我来炒菜做饭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过刚才副长来，\n',
            '说要代替我做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人，\n',
            '真的非常喜欢烹饪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131F')

    def _loc_12D7(): pass

    label('loc_12D7')

    ChrTalk(
        0x00FE,
        (
            '刚才副长来了，\n',
            '说要代替我做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人，\n',
            '真的非常喜欢烹饪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_131F(): pass

    label('loc_131F')

    Jump('loc_1725')

    def _loc_1322(): pass

    label('loc_1322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_13C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1397',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '自从空贼被逮捕以来，\n',
            '柏斯地区就非常和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，要是接连不断发生事件\n',
            '那真是很难办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C6')

    def _loc_1397(): pass

    label('loc_1397')

    ChrTalk(
        0x00FE,
        (
            '自从空贼被逮捕以来，\n',
            '柏斯地区就非常和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C6(): pass

    label('loc_13C6')

    Jump('loc_1725')

    def _loc_13C9(): pass

    label('loc_13C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_141B',
    )

    ChrTalk(
        0x00FE,
        (
            '之前来的魔兽\n',
            '比想象中的要厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也必须\n',
            '加紧训练才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1725')

    def _loc_141B(): pass

    label('loc_141B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_1469',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天的袭击\n',
            '真是个很好的教训。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来平时\n',
            '就要做好充分准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1725')

    def _loc_1469(): pass

    label('loc_1469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_14CA',
    )

    ChrTalk(
        0x00FE,
        (
            '搜索这样持续下去，\n',
            '国境师团的家伙们也相当累吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么新的进展就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1725')

    def _loc_14CA(): pass

    label('loc_14CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_153A',
    )

    ChrTalk(
        0x00FE,
        (
            '这一带\n',
            '越往山中走魔兽越多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且被通缉的魔兽\n',
            '也越来越多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天的训练是必不可少的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1725')

    def _loc_153A(): pass

    label('loc_153A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1638',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15E0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这座古罗尼连峰的地形\n',
            '也是起伏频繁的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定\n',
            '空贼团那些家伙们\n',
            '就藏在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '国境守备队的搜索队\n',
            '已经来这里调查了很多次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1635')

    def _loc_15E0(): pass

    label('loc_15E0')

    ChrTalk(
        0x00FE,
        (
            '这座古罗尼连峰\n',
            '地形也是起伏频繁的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定\n',
            '空贼团那些家伙们\n',
            '就藏在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1635(): pass

    label('loc_1635')

    Jump('loc_1725')

    def _loc_1638(): pass

    label('loc_1638')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1725',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16CB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这么险峻的山道，\n',
            '一般来说旅行的人\n',
            '是根本不会走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为现在飞艇还在停航，\n',
            '急着去卢安和柏斯的人们\n',
            '不得不从这里通过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1725')

    def _loc_16CB(): pass

    label('loc_16CB')

    ChrTalk(
        0x00FE,
        (
            '但是不管怎么说，\n',
            '还是应该尽量避免\n',
            '在晚上翻越这座山峰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对一般人来说太危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1725(): pass

    label('loc_1725')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x1729
@scena.Code('func_06_1729')
def func_06_1729():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_178A',
    )

    ChrTalk(
        0x00FE,
        (
            '市长的所作所为\n',
            '真的非常令人感到遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么想，\n',
            '也觉得这件事不可原谅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E17')

    def _loc_178A(): pass

    label('loc_178A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_1897',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1829',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '利贝尔各地的关所\n',
            '在十年前分裂帝国军时\n',
            '起到了很大的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且如今也\n',
            '作为军事要地被广泛利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些地方的守备\n',
            '绝对不能放松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1894')

    def _loc_1829(): pass

    label('loc_1829')

    ChrTalk(
        0x00FE,
        (
            '利贝尔各地的关所\n',
            '在十年前分裂帝国军时\n',
            '起到了很大的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以说，这些地方的守备\n',
            '绝对不可以放松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1894(): pass

    label('loc_1894')

    Jump('loc_1E17')

    def _loc_1897(): pass

    label('loc_1897')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1994',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1937',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '虽然我们士兵是为了\n',
            '镇守关所才驻守在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过偶尔也会向\n',
            '一些登山者实行救助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为来古罗尼连峰登山\n',
            '而遇难的人也有不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1991')

    def _loc_1937(): pass

    label('loc_1937')

    ChrTalk(
        0x00FE,
        (
            '虽然我们士兵是为了\n',
            '镇守关所才驻守在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过偶尔也会向\n',
            '一些登山者实行救助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1991(): pass

    label('loc_1991')

    Jump('loc_1E17')

    def _loc_1994(): pass

    label('loc_1994')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_19F1',
    )

    ChrTalk(
        0x00FE,
        (
            '如果敌人从两个方向发动进攻，\n',
            '该如何防守呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天训练的议题就是这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E17')

    def _loc_19F1(): pass

    label('loc_19F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Return,
        ),
        'loc_1A23',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，要出发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '路上小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E17')

    def _loc_1A23(): pass

    label('loc_1A23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_1A6A',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，睡得还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天你们出手\n',
            '真是帮了我们大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E17')

    def _loc_1A6A(): pass

    label('loc_1A6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 0, 0x400)),
            Expr.Return,
        ),
        'loc_1BF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 4, 0x404)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BB6',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0080, 4, 0x404))
    OP_69(0x00FE, 1000)

    ChrTalk(
        0x00FE,
        (
            '#1430040138V啊，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040139V#010F您好，不好意思打扰一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040140V其实我们……',
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
            '两人向队长说明情况，\n',
            '并且请求在关所留宿一晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#1430040141V哦，没问题。\n',
            '游击士的身份就是一种保证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1430040142V隔壁的休息室就请随便使用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040143V#000F谢谢，队长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_1BF1')

    def _loc_1BB6(): pass

    label('loc_1BB6')

    ChrTalk(
        0x00FE,
        (
            '这里隔壁的休息室\n',
            '就请随便使用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '先取个暖如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BF1(): pass

    label('loc_1BF1')

    Jump('loc_1E17')

    def _loc_1BF4(): pass

    label('loc_1BF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1C48',
    )

    ChrTalk(
        0x00FE,
        (
            '国境守备队好像\n',
            '向本部要求增员了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来将军\n',
            '准备在这几天动手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E17')

    def _loc_1C48(): pass

    label('loc_1C48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1CB4',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，摩尔根将军已经将搜索范围\n',
            '缩小到北部山区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼们果然藏在\n',
            '国境附近的某个地方啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E17')

    def _loc_1CB4(): pass

    label('loc_1CB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1DD2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D79',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '摩尔根将军\n',
            '发布命令要求强化这一带的警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼们藏在哪里，\n',
            '还不是很清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤其是山林，\n',
            '那里是他们最好的藏身之处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要赶快通知队里的人，\n',
            '让他们提高警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DCF')

    def _loc_1D79(): pass

    label('loc_1D79')

    ChrTalk(
        0x00FE,
        (
            '摩尔根将军\n',
            '发布命令要求强化这一带的警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼们藏在哪里，\n',
            '还不是很清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DCF(): pass

    label('loc_1DCF')

    Jump('loc_1E17')

    def _loc_1DD2(): pass

    label('loc_1DD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1E17',
    )

    ChrTalk(
        0x00FE,
        (
            '需要通行许可证的话，我就发给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '随时来找我好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E17(): pass

    label('loc_1E17')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x1E1B
@scena.Code('func_07_1E1B')
def func_07_1E1B():
    TalkBegin(0x000B)
    ChrTurnDirection(0x00FE, 0x0103, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2054',
    )

    SetScenaFlags(ScenaFlag(0x006C, 0, 0x360))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0120030585V#814F啊，难道……\n',
            '这不是雪拉扎德前辈吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030586V#850F很久不见了啊。\n',
            '自从您去修行之后就再没见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030587V#020F这不是亚妮拉丝吗。\n',
            '你在这里做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030588V#810F嗯～\n',
            '协会委托我来这边消灭通缉魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030589V#020F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030590V对了，\n',
            '你已经找到所谓的剑之道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030591V#819F呵呵，请别问了。\n',
            '我还处在修行阶段呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030592V说起来，\n',
            '前辈您也是在执行协会的任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030593V#020F是啊，不过我和你的任务性质不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030594V#810F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030595V这个地方\n',
            '最近发生很多事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030596V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_214F')

    def _loc_2054(): pass

    label('loc_2054')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20F7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0103,
        (
            '#0030030597V#020F啊，这不是亚妮拉丝吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030598V#850F雪拉扎德前辈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030599V#810F怎么样？\n',
            '调查进行得顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030600V#020F嗯，有一点进展了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_214F')

    def _loc_20F7(): pass

    label('loc_20F7')

    ChrTalk(
        0x00FE,
        (
            '#0120030601V#810F雪拉扎德前辈，\n',
            '这个地方最近处于多事之秋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030602V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_214F(): pass

    label('loc_214F')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x2153
@scena.Code('func_08_2153')
def func_08_2153():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x2158
@scena.Code('func_09_2158')
def func_09_2158():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Return,
        ),
        'loc_21BA',
    )

    ChrTalk(
        0x000C,
        (
            '啊呀，你们要去卢安吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这里可是去柏斯的出口。\n',
            '要去卢安的话，请从对面出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F4')

    def _loc_21BA(): pass

    label('loc_21BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_21F4',
    )

    ChrTalk(
        0x000C,
        (
            '这里的海拔比较高，\n',
            '太阳一落山果然就会很冷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21F4(): pass

    label('loc_21F4')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x21F8
@scena.Code('func_0A_21F8')
def func_0A_21F8():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_223A',
    )

    ChrTalk(
        0x00FE,
        (
            '听说卢安的市长\n',
            '被逮捕了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然有这种事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C6')

    def _loc_223A(): pass

    label('loc_223A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_229C',
    )

    ChrTalk(
        0x00FE,
        (
            '被魔兽打伤的地方\n',
            '终于痊愈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要尽量避免以后再发生这类事情，\n',
            '所以要加紧训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C6')

    def _loc_229C(): pass

    label('loc_229C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_22F3',
    )

    ChrTalk(
        0x00FE,
        (
            '副长还真是喜欢烹饪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时候明明不是他当班，\n',
            '但是他却在厨房做饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C6')

    def _loc_22F3(): pass

    label('loc_22F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_2346',
    )

    ChrTalk(
        0x00FE,
        (
            '柴火差不多要用完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '训练结束后去报告一下，\n',
            '然后就去砍些柴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C6')

    def _loc_2346(): pass

    label('loc_2346')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_238B',
    )

    ChrTalk(
        0x00FE,
        (
            '痛痛痛痛痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是失策。\n',
            '被魔兽打伤的地方好痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C6')

    def _loc_238B(): pass

    label('loc_238B')

    ChrTalk(
        0x00FE,
        (
            '一会儿就轮到我值班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '趁现在赶快吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23C6(): pass

    label('loc_23C6')

    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x23CA
@scena.Code('func_0B_23CA')
def func_0B_23CA():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_240C',
    )

    ChrTalk(
        0x00FE,
        (
            '呜呜～虽说已经是这个季节，\n',
            '山上却还是这么冷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_294E')

    def _loc_240C(): pass

    label('loc_240C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_2451',
    )

    ChrTalk(
        0x00FE,
        (
            '离值勤还有段时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是先\n',
            '稍微小睡一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_294E')

    def _loc_2451(): pass

    label('loc_2451')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2544',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_250E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '这里是深山老林，\n',
            '食物的供应非常不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也有很多东西\n',
            '从柏斯和卢安那里运送过来，\n',
            '不过毕竟是山路啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经常需要去迎接送货的人，\n',
            '并且给他们顺便但当护卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2541')

    def _loc_250E(): pass

    label('loc_250E')

    ChrTalk(
        0x00FE,
        (
            '这里一到冬天，\n',
            '大雪就会堆积起来，特别不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2541(): pass

    label('loc_2541')

    Jump('loc_294E')

    def _loc_2544(): pass

    label('loc_2544')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_259B',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多到训练的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为发生过魔兽袭击事件，\n',
            '大家要提高警惕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_294E')

    def _loc_259B(): pass

    label('loc_259B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_264F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_260B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '早上好，昨天谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然看上去挺年轻，\n',
            '但真不愧是游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干得真棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_264C')

    def _loc_260B(): pass

    label('loc_260B')

    ChrTalk(
        0x00FE,
        (
            '虽然看上去挺年轻，\n',
            '但真不愧是游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天干得真棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_264C(): pass

    label('loc_264C')

    Jump('loc_294E')

    def _loc_264F(): pass

    label('loc_264F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_26F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26BC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '有什么事吗？\n',
            '你们可以随便进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要使用休息室的话，\n',
            '和我们队长打声招呼就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26F1')

    def _loc_26BC(): pass

    label('loc_26BC')

    ChrTalk(
        0x00FE,
        (
            '想使用里面的屋子时，\n',
            '和我们队长打声招呼就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26F1(): pass

    label('loc_26F1')

    Jump('loc_294E')

    def _loc_26F4(): pass

    label('loc_26F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_280B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27B8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '好像还是找不到\n',
            '空贼团的所在之处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国境守备队的那伙人\n',
            '最近也经常到这里\n',
            '来进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯这个地方\n',
            '就是山岳比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '犯人要是隐藏在这里，\n',
            '可是最难发现的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2808')

    def _loc_27B8(): pass

    label('loc_27B8')

    ChrTalk(
        0x00FE,
        (
            '柏斯这个地方\n',
            '就是山岳比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '犯人要是隐藏在这里，\n',
            '可是最难发现的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2808(): pass

    label('loc_2808')

    Jump('loc_294E')

    def _loc_280B(): pass

    label('loc_280B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2874',
    )

    ChrTalk(
        0x00FE,
        (
            '消失的定期船\n',
            '好像被找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为犯人还没有被抓住，\n',
            '所以关所还要继续\n',
            '维持盘查的制度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_294E')

    def _loc_2874(): pass

    label('loc_2874')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_28FC',
    )

    ChrTalk(
        0x00FE,
        (
            '是空贼团吗……\n',
            '真是一群不容易对付的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，这次是由那位\n',
            '摩尔根将军亲临指挥呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定马上就会抓到他们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_294E')

    def _loc_28FC(): pass

    label('loc_28FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_294E',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正处在戒严状态中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们想通行的话，\n',
            '必须先在里面办手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_294E(): pass

    label('loc_294E')

    TalkEnd(0x000E)

    Return()

# id: 0x000C offset: 0x2952
@scena.Code('func_0C_2952')
def func_0C_2952():
    EventBegin(0x00)
    FormationAddMember(0x05, 0xFF)
    EventBegin(0x00)
    CameraMove(80631, 0, 54990, 0)
    SetChrPos(0x0101, 75900, 0, 53900, 90)
    SetChrPos(0x0102, 74500, 0, 53000, 90)
    SetChrPos(0x0106, 73600, 0, 52570, 90)
    SetChrPos(0x0008, 73600, 0, 52570, 90)
    SetChrFlags(0x0106, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0106, 0x0004)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_29D6')
    def lambda_29D6():
        ChrWalkTo(0x00FE, 80100, 0, 53900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_29D6)

    @scena.Lambda('lambda_29F1')
    def lambda_29F1():
        ChrWalkTo(0x00FE, 79200, 0, 53000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_29F1)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010980001V#000F这里就是旅行者专用的休息室啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020980002V#010F嗯。\n',
            '我先把暖炉点着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A6F')
    def lambda_2A6F():
        CameraMove(82761, 0, 52570, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2A6F)

    ChrWalkTo(0x0102, 80800, 0, 53000, 2000, 0x00)

    @scena.Lambda('lambda_2A9B')
    def lambda_2A9B():
        ChrWalkTo(0x00FE, 83135, 0, 51740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2A9B)

    Sleep(500)

    @scena.Lambda('lambda_2ABB')
    def lambda_2ABB():
        ChrWalkTo(0x00FE, 82756, 0, 52574, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2ABB)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 90, 400)
    Sleep(1000)

    PlaySE(134, 0x00, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrWalkTo(0x0102, 82756, 0, 51260, 2000, 0x00)
    SetChrDirection(0x0102, 52, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010980003V#001F#1P呼～好暖和……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010980004V还是烧柴火的暖炉\n',
            '更让人感到自然和舒服啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020980005V#010F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020980006V虽然导力炉已经广泛使用了，\n',
            '不过温暖程度始终比不上暖炉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010980007V#501F#1P嗯，各有各的优点吧。\n',
            '导力炉用起来比较方便嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlaySE(113, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1440980008V#2P两位～打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_2CB0')
    def lambda_2CB0():
        CameraMove(81370, 0, 53270, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2CB0)

    @scena.Lambda('lambda_2CC8')
    def lambda_2CC8():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2CC8')

    DispatchAsync2(0x0102, 0x0001, lambda_2CC8)

    Sleep(100)

    @scena.Lambda('lambda_2CDE')
    def lambda_2CDE():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2CDE')

    DispatchAsync2(0x0101, 0x0001, lambda_2CDE)

    OP_4A(0x0008, 255)
    ClearChrFlags(0x0008, 0x0080)
    ChrWalkTo(0x0008, 78000, 0, 53320, 3000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1440980009V我从队长那里听说了，\n',
            '你们今晚要住在这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440980010V晚饭就和我们\n',
            '吃一样的饭菜如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010980011V#004F#1P哎，这样好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020980012V#010F不好意思，还让你们这样款待我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440980013V哪里，自从定期船通航之后，\n',
            '从这里通行的人寥寥无几。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440980014V这里大部分时间都很冷清，\n',
            '所以我们是十分欢迎有客人来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010980015V#001F#1P嘿嘿，既然您这样说，\n',
            '那我们就不客气啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440980016V好的。\n',
            '那就请你们稍微等会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440980017V对了，因为是军队的伙食，\n',
            '你们可别对味道过于期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 270, 400)
    ChrWalkTo(0x0008, 74570, 0, 52910, 3000, 0x00)

    @scena.Lambda('lambda_2F14')
    def lambda_2F14():
        ChrWalkTo(0x00FE, 72320, 0, 52990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2F14)

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 500)
    PlaySE(7, 0x00, 0x64)
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010980018V#000F#1P虽然在空贼团作乱的时候\n',
            '和王国军有过争执……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010980019V不过在王国军里\n',
            '还是有很多亲切的军人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101139V#010F确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020980021V#015F不过，亲切的军人，\n',
            '我想也只有利贝尔才会有吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3015')
    def lambda_3015():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3015)

    ChrTalk(
        0x0101,
        (
            '#0010980022V#501F#1P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020980023V#010F没什么……\n',
            '总之先把行李放好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    SetMapFlags(0x02000000)
    NewScene('ED6_DT01/T1311._SN', 2, 0, 0)
    IdleLoop()
    CameraMove(80990, 200, 53320, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0101, 81090, 200, 51050, 270)
    SetChrPos(0x0102, 78250, 200, 51000, 90)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 4)
    SetChrPos(0x000F, 79980, 750, 50430, 0)
    SetChrPos(0x0010, 79200, 750, 51110, 0)
    SetChrPos(0x0011, 80060, 700, 51150, 0)
    SetChrPos(0x0012, 79240, 700, 50480, 0)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    Sleep(1000)

    PlayBGM(84)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    OP_62(0x0101, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040144V#001F#2P哈～～吃饱啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040145V还说不要太期待什么的，\n',
            '没想到原来是这么好吃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040146V#010F是啊。\n',
            '想不到军队里也有如此好吃的饭菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(16, 0x00, 0x64)
    Sleep(1000)

    SetChrFlags(0x0008, 0x0040)
    SetChrPos(0x0008, 72320, 0, 52990, 90)

    ChrTalk(
        0x0008,
        (
            '#1440040147V#2P打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    PlaySE(15, 0x00, 0x64)
    Sleep(500)

    SetChrFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_3270')
    def lambda_3270():
        CameraMove(79690, 0, 53470, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3270)

    SetChrSubChip(0x0102, 1)
    SetChrDirection(0x0008, 90, 0)
    ClearChrFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_3299')
    def lambda_3299():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_3299)

    ChrWalkTo(0x0008, 79660, 0, 52870, 3000, 0x00)
    SetChrDirection(0x0008, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040148V#001F#2P啊，副长先生。\n',
            '饭菜真的很好吃哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F谢谢你们的款待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040150V#1P只是些粗茶淡饭，\n',
            '能合你们的口味就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040151V#1P啊，对了……\n',
            '又有一位客人来了，\n',
            '你们不介意和他住一个房间吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F客人……\n',
            '这么晚了还有人来这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040153V#000F#2P这位客人胆子还挺大的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040154V我们倒无所谓，\n',
            '说到底自己也同样是客人罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040155V#1P你们能这么说真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040156V#1P说起来，他和小姑娘你们是同行，\n',
            '因此也没必要太过顾虑哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040157V#004F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F同行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0106, 72320, 0, 52990, 90)

    NpcTalk(
        0x0106,
        '青年的声音',
        (
            '#0050040159V#2P哼……\n',
            '没想到你们也来了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0106, 7)
    ClearChrFlags(0x0106, 0x0080)
    ChrSetRGBAMask(0x0106, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_351C')
    def lambda_351C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_351C)

    @scena.Lambda('lambda_352E')
    def lambda_352E():
        ChrWalkTo(0x00FE, 78640, 0, 53600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_352E)

    Sleep(500)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0106, 0x0001)
    SetChrDirection(0x0106, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040160V#004F#2P啊，是你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F『重剑阿加特』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040162V#1P什么，原来你们认识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#1440040163V#2P对了阿加特，\n',
            '你吃过晚饭没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040164V#050F谢了，不用了。\n',
            '刚刚已经吃过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040165V让我在这里睡一晚就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040166V#2P没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#1P好了。\n',
            '你们就自己分配床位吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040168V#1P晚安了，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 270, 400)
    TerminateThread(0x0106, 0xFF)
    ChrWalkTo(0x0008, 78400, 0, 52230, 3000, 0x00)

    @scena.Lambda('lambda_36F9')
    def lambda_36F9():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_36F9')

    DispatchAsync2(0x0106, 0x0003, lambda_36F9)

    ChrWalkTo(0x0008, 74570, 0, 52910, 3000, 0x00)

    @scena.Lambda('lambda_371E')
    def lambda_371E():
        ChrWalkTo(0x00FE, 72320, 0, 52990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_371E)

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 500)
    SetChrFlags(0x0008, 0x0080)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_3753')
    def lambda_3753():
        CameraMove(80990, 200, 53320, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3753)

    TerminateThread(0x0106, 0xFF)
    SetChrDirection(0x0106, 135, 400)
    ChrWalkTo(0x0106, 79660, 0, 52870, 2000, 0x00)
    SetChrDirection(0x0106, 180, 400)

    ChrTalk(
        0x0106,
        (
            '#050F#1P对了……\n',
            '你们两个是大叔的孩子吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040170V为什么你们\n',
            '会在这种地方过夜？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040171V雪拉扎德没和你们在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040172V#010F雪拉姐姐她\n',
            '已经回洛连特去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040173V现在只有我们两个一起旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040174V#006F#2P嗯，我们以成为正游击士为目标，\n',
            '打算环游整个王国一周。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040175V同时为了修行，选择了徒步旅行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#052F#1P正游击士？\n',
            '徒步环游整个王国一周？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040177V真是两个无忧无虑的小鬼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040178V#009F#2P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F#1P像你们这种小鬼可以\n',
            '那么简单就成为正游击士吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040180V用常识想想，常识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040181V#005F#2P别、别小看我们！\n',
            '之前我们还抓住了那些空贼呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040182V而且我们也获得了推荐信，\n',
            '你别把我们当作三岁小孩子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F#1P捉空贼那件事吗？\n',
            '我从卢格兰老爷子那听说过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040184V#050F我倒要问问你们……\n',
            '假如只有你们两个的话，\n',
            '事件真的会那么容易就解决吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040185V假如没有雪拉扎德在身边，\n',
            '你们自己可以对付得了空贼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040186V#003F#2P这、这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F……我想会很难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F#1P那是当然的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040189V你们只是初出茅庐的新人，还是小鬼而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040190V能力不够、经验不足，\n',
            '遇到突发事件又不能做出敏锐的判断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040191V而且还这么不知天高地厚，\n',
            '你们迟早有一天会摔跟头的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040192V#009F#2P什、什么不知天高地厚啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040193V你才是呢！\n',
            '这个时候还上山来，\n',
            '你究竟知不知道有多危险啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040194V还有资格说别人吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F#1P蠢材！我和你们可不一样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040196V而且我有任务在身，\n',
            '不像你们那样在到处游山玩水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F任务？\n',
            '是游击士协会的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F#1P啊啊，就是你们那个老爸，\n',
            '出差前把自己的任务强推给我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040199V#004F#2P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040200V#014F父亲强推给你的任务？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F#1P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0106, 315, 400)

    ChrTalk(
        0x0106,
        (
            '#0050040202V#053F不说了，明天还要早起。\n',
            '赶快睡觉要紧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040203V你们也别再啰嗦了，上床睡觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3E11')
    def lambda_3E11():
        CameraMove(79640, 0, 54740, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3E11)

    ChrWalkTo(0x0106, 77650, 0, 56480, 2500, 0x00)
    SetChrDirection(0x0106, 180, 400)
    SetChrFlags(0x0106, 0x0004)
    ChrJumpTo(0x0106, 75900, 0, 56780, 1000, 5000)

    ChrTalk(
        0x0101,
        (
            '#0010040204V#005F#2P啊～这样就想糊弄过去吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F说得那么明显，\n',
            '分明就是要让我们在意嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#054F够啦！别再烦我啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040207V我是为了你们两个小鬼好，\n',
            '多管闲事只会惹来一身麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#053F明天一早就给我快点去卢安，\n',
            '看看协会的公告板上有什么活干！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那种才是……呼啊……\n',
            '你们应该去过的生活……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040210V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 1700, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(2000)

    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040211V#004F#2P等、等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好像已经睡着了。\n',
            '和艾丝蒂尔你一样能睡呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040213V#005F#2P别把我和他混为一谈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040214V#007F真是的～这家伙究竟怎么想的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040215V难道除了吵架，\n',
            '他就不会做点别的事情吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040216V#010F算了算了。\n',
            '毕竟我们还是新人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040217V也许他只是担心我们，\n',
            '才会特意说那么严厉的话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040218V#009F#2P………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040219V我说约修亚，\n',
            '难道你真的这样想吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#005F这个嘛，我也不太肯定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040221V#010F不过，正如他所说的，\n',
            '我们最好也早点休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040222V明天还要下山呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040223V#007F#2P唔～虽然感到很不爽，\n',
            '不过没办法啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040224V#006F嘿嘿，我们干脆在他脸上涂鸦，\n',
            '给他一点教训吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040225V我看他睡得挺熟的，应该没问题☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040226V#018F还是不要这么做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    SetMapFlags(0x02000000)
    NewScene('ED6_DT01/T1301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x42CB
@scena.Code('func_0D_42CB')
def func_0D_42CB():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(80978, 0, 152763, 0)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0106, 0x0004)
    SetChrPos(0x0101, 84150, 0, 151987, 45)
    SetChrPos(0x0102, 80770, 0, 151987, 45)
    SetChrPos(0x0106, 76070, 0, 151787, 315)
    OP_62(0x0101, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    SetChrDirection(0x0101, 225, 400)
    OP_63(0x0101)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    SetChrDirection(0x0102, 225, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    OP_63(0x0102)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    SetChrDirection(0x0106, 135, 400)
    OP_62(0x0106, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    OP_63(0x0106)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#000F刚、刚才你有没有听到什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好像发生了什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我到外面看看情况，\n',
            '你们两个乖乖留在这里睡觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpTo(0x0106, 77869, 0, 151633, 1000, 6000)
    ChrWalkTo(0x0106, 77353, 0, 148213, 5000, 0x00)
    ChrWalkTo(0x0106, 73337, 0, 147693, 5000, 0x00)
    SetChrFlags(0x0106, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#000F啊……\n',
            '等、等一下嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F为了谨慎起见，\n',
            '我们也出去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，那当然啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0101, 82130, 0, 148000, 270)
    FormationDelMember(0x05, 0xFF)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x4540
@scena.Code('func_0E_4540')
def func_0E_4540():
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 10)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    FormationDelMember(0x05, 0xFF)
    EventBegin(0x00)
    CameraMove(84500, 0, 57320, 0)
    SetChrPos(0x0102, 82610, 0, 56640, 90)
    SetChrPos(0x0101, 84250, 650, 56940, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 7)
    FadeOut(0, 0, -1)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020040300V#010F艾丝蒂尔。\n',
            '……天亮了，该起床了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040301V#455F#2P呼啊～～……\n',
            '讨厌……做什么嘛～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 16)
    PlayBGM(16)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010040302V#457F#2P咦，约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040303V这么早就要去协会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040304V#017F你在说什么呀？\n',
            '我们还在古罗尼关所呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_46DF')
    def lambda_46DF():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_46DF)

    Sleep(50)

    OP_6F(0x0003, 10)
    OP_70(0x0003, 20)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010040305V#456F#2P啊，对了……\n',
            '昨天晚上发生了魔兽骚动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x11, 0x15, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010040306V#453F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(82170, 0, 55040, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010040307V#451F#4P那个红头发的刀子嘴呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040308V#010F#3P他好像一大早就出发了，\n',
            '应该是有紧要任务要去执行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040309V#452F#4P是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040310V#455F#4P难得昨天晚上\n',
            '还同心协力把魔兽击退了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040311V连个招呼也不打就走了，\n',
            '真是个没礼貌的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040312V#010F#3P算了算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040313V我们也该准备动身出发了，\n',
            '最好在中午之前翻过这座山峰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040314V#454F#4P嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040315V终于要到卢安了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_72(0x0003, 0x0008)
    OP_72(0x0003, 0x0020)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0101, 0x0002)
    SetChrPos(0x0101, 77640, 0, 53190, 270)
    SetChrPos(0x0102, 77640, 0, 53190, 270)
    CameraMove(77640, 0, 53190, 0)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    Sleep(500)

    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x0080, 6, 0x406))
    OP_28(0x003A, 0x04, 0x02)
    OP_28(0x003A, 0x04, 0x04)
    OP_28(0x003A, 0x01, 0x0001)
    OP_28(0x003A, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x499C
@scena.Code('func_0F_499C')
def func_0F_499C():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A02',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061983V#010F这边是柏斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061984V没有拿到许可证\n',
            '是不能从这边出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A57')

    def _loc_4A02(): pass

    label('loc_4A02')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061985V#010F这边是柏斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061986V没有拿到许可证\n',
            '是不能从这边出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A57(): pass

    label('loc_4A57')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0010 offset: 0x4A73
@scena.Code('func_10_4A73')
def func_10_4A73():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
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
        1,
        (
            TXT(0x00, '在此休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C8C',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x02, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 50)
    OP_73(0x0033)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    SetChrPos(0x0000, 19740, 0, 13090, 217)
    SetChrPos(0x0001, 19740, 0, 13090, 217)
    SetChrPos(0x0002, 19740, 0, 13090, 217)
    SetChrPos(0x0003, 19740, 0, 13090, 217)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0005, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_4C8C(): pass

    label('loc_4C8C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4CA6',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_4CA6(): pass

    label('loc_4CA6')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
