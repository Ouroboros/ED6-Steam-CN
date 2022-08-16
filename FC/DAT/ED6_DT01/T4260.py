import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4260_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4260   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4260.x'
    header.mapIndex       = 1
    header.bgm            = 17
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯少尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '摩尔根将军',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '艾莉茜雅女王',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x312
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x312
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x312
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x312
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_329',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_06_7E7)

    def _loc_329(): pass

    label('loc_329')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_353',
    )

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_35D',
    )

    Jump('loc_3CE')

    def _loc_35D(): pass

    label('loc_35D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3A9',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, 60, 500, 154950, 168)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0016, 60, 0, 150270, 7)
    ChrSetPos(0x0017, -800, 0, 149980, 356)

    Jump('loc_3CE')

    def _loc_3A9(): pass

    label('loc_3A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_3B3',
    )

    Jump('loc_3CE')

    def _loc_3B3(): pass

    label('loc_3B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_3BD',
    )

    Jump('loc_3CE')

    def _loc_3BD(): pass

    label('loc_3BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_3C7',
    )

    Jump('loc_3CE')

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_3CE',
    )

    def _loc_3CE(): pass

    label('loc_3CE')

    Return()

# id: 0x0001 offset: 0x3CF
@scena.Code('func_01_3CF')
def func_01_3CF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            (Expr.PushValueByIndex, 0x1),
            (Expr.PushLong, 0x51),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3E8(): pass

    label('loc_3E8')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x3F2
@scena.Code('func_02_3F2')
def func_02_3F2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_407',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3F2')

    def _loc_407(): pass

    label('loc_407')

    Return()

# id: 0x0003 offset: 0x408
@scena.Code('func_03_408')
def func_03_408():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0018,
        (
            '#0630140653V#090F让曾经辞退了军衔的\n',
            '卡西乌斯阁下恢复原职，\n',
            '我心里很是过意不去啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630140654V不过有他在的话，\n',
            '我也安心了不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630140655V虽然对你们深感抱歉，\n',
            '但请暂时让你们的父亲助我一臂之力吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x4E1
@scena.Code('func_04_4E1')
def func_04_4E1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_553',
    )

    ChrTalk(
        0x0016,
        (
            '#0160140635V#080F我很快就要\n',
            '参加预定的会议了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140634V你们两个在王都里面\n',
            '好好地玩一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DB')

    def _loc_553(): pass

    label('loc_553')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0016,
        (
            '#0160140632V#080F大街那边很热闹吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140633V我很快就要\n',
            '参加预定的会议了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140634V你们两个在王都里面\n',
            '好好地玩一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5DB(): pass

    label('loc_5DB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x5DF
@scena.Code('func_05_5DF')
def func_05_5DF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_618',
    )

    ChrTalk(
        0x0017,
        (
            '#160F理查德……\n',
            '……那个愚蠢的小子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E3')

    def _loc_618(): pass

    label('loc_618')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0017,
        (
            '#160F是你们俩啊……好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……摩尔根将军？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140639V#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#160F你们在艾尔贝离宫\n',
            '救了我的孙女吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F艾尔贝离宫……\n',
            '啊，是莉安妮小妹妹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那是我们理应要做的事情。\n',
            '作为游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0600140645V#160F哼，还是那么能说会道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，这回我真的要\n',
            '向你们表示感激。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F摩尔根将军……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#160F作为游击士，\n',
            '你们做得很不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F怎、怎么感觉\n',
            '这不是您的说话方式呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '算了，这样也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7E3(): pass

    label('loc_7E3')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x7E7
@scena.Code('func_06_7E7')
def func_06_7E7():
    EventBegin(0x00)
    CameraMove(-20, 0, 140000, 0)
    OP_67(0, 8189, -10000, 0)
    CameraSetDistance(2180, 0)
    OP_6C(45000, 0)
    OP_6E(473, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0008, 620, 500, 152930, 270)
    ChrSetPos(0x0009, -790, 500, 152790, 90)
    ChrSetPos(0x000A, -730, 0, 148500, 0)
    ChrSetPos(0x000B, 620, 0, 148500, 0)
    ChrSetPos(0x000C, -730, 0, 146900, 0)
    ChrSetPos(0x000D, 620, 0, 146900, 0)
    ChrSetPos(0x000E, -730, 0, 145500, 0)
    ChrSetPos(0x000F, 620, 0, 145500, 0)
    ChrSetPos(0x0010, -730, 0, 143900, 0)
    ChrSetPos(0x0011, 620, 0, 143900, 0)
    ChrSetPos(0x0012, -730, 0, 142300, 0)
    ChrSetPos(0x0013, 620, 0, 142300, 0)
    ChrSetPos(0x0014, -730, 0, 140700, 0)
    ChrSetPos(0x0015, 620, 0, 140700, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    FadeIn(2000, 0)
    CameraMove(-60, 500, 152860, 5000)
    Fade(1000)
    CameraMove(-60, 500, 152860, 0)
    OP_67(0, 8189, -10000, 0)
    CameraSetDistance(1500, 0)
    OP_6C(45000, 0)
    OP_6E(473, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0610130917V#187F这、这究竟是怎么回事！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610130918V与『艾尔贝离宫』的联络竟然中断了！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140130920V#281F亲卫队和游击士协会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140130921V很有可能被他们那伙人攻陷了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610130923V#186F厚、厚颜无耻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610130924V指挥那里的部队的……\n',
            '少尉，不就是你吗！　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140130926V#280F我真是颜面尽失啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140130927V不过，既然事已至此，\n',
            '怎么埋怨也都已经没用吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140130929V而且我们还必须坚守王城，\n',
            '不能让陛下被他们劫走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610130931V#187F不、不用你说，\n',
            '我也明白这一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BC2')
    def lambda_0BC2():
        CameraMove(-20, 500, 151500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BC2)

    ChrSetDirection(0x0008, 180, 400)
    ChrWalkTo(0x0008, 310, 500, 152070, 2000, 0x00)
    ChrSetDirection(0x0009, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0610130932V#185F彻底封锁城门！\n',
            '无论是谁都不许入内！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610130933V然后只要准备迎击\n',
            '从空中而来的突袭就可以了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2630130935V#5P了解！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610130936V#185F还有，联络各地的部队，\n',
            '让他们向艾尔贝离宫进发！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610130938V理由是——\n',
            '镇压假冒王族的恐怖集团！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    SetMessageWindowPos(350, 250, -1, -1)
    TalkSetChrName('特务兵们')

    Talk(
        (
            '#2620130939V',
            (TxtCtl.SetColor, 0x0),
            '#5SYes，Madam！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x000E, 0x01, 0x00, func_07_F0C)
    Sleep(50)

    CreateThread(0x000F, 0x01, 0x00, func_08_F28)
    Sleep(300)

    CreateThread(0x000C, 0x01, 0x00, func_07_F0C)
    Sleep(50)

    CreateThread(0x000D, 0x01, 0x00, func_08_F28)
    Sleep(300)

    CreateThread(0x000A, 0x01, 0x00, func_07_F0C)
    Sleep(50)

    CreateThread(0x000B, 0x01, 0x00, func_08_F28)
    Sleep(1000)

    @scena.Lambda('lambda_0D9A')
    def lambda_0D9A():
        CameraMove(-250, 500, 152390, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D9A)

    Sleep(500)

    @scena.Lambda('lambda_0DB7')
    def lambda_0DB7():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0DB7')

    DispatchAsync2(0x0009, 0x0001, lambda_0DB7)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0140130940V#280F呵呵，很有一手嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0610130941V#180F哼哼，那是当然。\n',
            '不要把我和你这个新来的相提并论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E45')
    def lambda_0E45():
        CameraMove(-1270, 2700, 154040, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E45)

    @scena.Lambda('lambda_0E5D')
    def lambda_0E5D():
        OP_67(0, 3190, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0E5D)

    @scena.Lambda('lambda_0E75')
    def lambda_0E75():
        OP_6C(38000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E75)

    @scena.Lambda('lambda_0E85')
    def lambda_0E85():
        CameraSetDistance(1600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0E85)

    ChrSetDirection(0x0008, 0, 400)
    ChrWalkTo(0x0008, 350, 500, 153030, 1000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0610130942V#183F#2P……上校不在，\n',
            '我们一定要把这里守住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4302._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0xF0C
@scena.Code('func_07_F0C')
def func_07_F0C():
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, -730, 0, 110220, 4000, 0x00)

    Return()

# id: 0x0008 offset: 0xF28
@scena.Code('func_08_F28')
def func_08_F28():
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 620, 0, 110220, 4000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
