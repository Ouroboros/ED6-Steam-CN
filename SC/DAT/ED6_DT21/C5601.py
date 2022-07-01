import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5601_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5601   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '银发的青年'),
    TXT(0x02, '怀斯曼教授'),
    TXT(0x03, '歼灭天使玲'),
    TXT(0x04, '歼灭天使玲'),
    TXT(0x05, '艾丝蒂尔'),
    TXT(0x06, '小丑肯帕雷拉'),
    TXT(0x07, '结社艇'),
    TXT(0x08, '结社艇（影）'),
    TXT(0x09, '结社艇（光）'),
    TXT(0x0A, '帕蒂尔·玛蒂尔'),
    TXT(0x0B, '小船'),
    TXT(0x0C, '小船（诱饵）'),
    TXT(0x0D, '目标用照相机'),
    TXT(0x0E, '库拉茨'),
    TXT(0x0F, '卡露娜'),
    TXT(0x10, '亚妮拉丝'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5601.x'
    header.mapIndex       = 1
    header.bgm            = 125
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4523
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
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT27/CH03550._CH', 'ED6_DT27/CH03550P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT27/CH03004._CH', 'ED6_DT27/CH03004P._CP'),
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT26/CH20295._CH', 'ED6_DT26/CH20295P._CP'),
        ('ED6_DT26/CH20379._CH', 'ED6_DT26/CH20379P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT26/CH20288._CH', 'ED6_DT26/CH20288P._CP'),
    ]

# id: 0x10002 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
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
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
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
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
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
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
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
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
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
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C4,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C4,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0188,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E5,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0084,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -6510,
            z                   = -6050,
            y                   = -26680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = -6770,
            z                   = -5970,
            y                   = -27880,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -6380,
            z                   = -5900,
            y                   = -28820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x352
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x352
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x352
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9520,
            triggerZ            = 9000,
            triggerY            = 6150,
            triggerRange        = 1000,
            actorX              = 9960,
            actorZ              = 9000,
            actorY              = 6600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -15010,
            triggerZ            = 0,
            triggerY            = -3880,
            triggerRange        = 800,
            actorX              = -15010,
            actorZ              = 1000,
            actorY              = -3880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4500,
            triggerZ            = -6000,
            triggerY            = -27040,
            triggerRange        = 1000,
            actorX              = -4500,
            actorZ              = -5000,
            actorY              = -27040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3BE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 7, 0x1C0F)),
            Expr.Return,
        ),
        'loc_3C8',
    )

    Jump('loc_401')

    def _loc_3C8(): pass

    label('loc_3C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 5, 0x1C0D)),
            Expr.Return,
        ),
        'loc_3E1',
    )

    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)

    Jump('loc_401')

    def _loc_3E1(): pass

    label('loc_3E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 3, 0x1C0B)),
            Expr.Return,
        ),
        'loc_3F5',
    )

    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)

    Jump('loc_401')

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 0, 0x1C08)),
            Expr.Return,
        ),
        'loc_401',
    )

    ClearChrFlags(0x0015, 0x0080)

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 6, 0x1C06)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_409',
    )

    def _loc_409(): pass

    label('loc_409')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_438',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x7D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    SetMapFlags(0x00000010)
    OP_11(0x81, 0x99, 0xCF, 0x000186A0, 0x000493E0, 0x00000000)
    Event(0, 0x0006)

    Jump('loc_4AC')

    def _loc_438(): pass

    label('loc_438')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_456',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x3D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F1)
    OP_64(0x00, 0x0001)
    Event(0, 0x000C)

    Jump('loc_4AC')

    def _loc_456(): pass

    label('loc_456')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_474',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x3D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F2)
    OP_64(0x00, 0x0001)
    Event(0, 0x000D)

    Jump('loc_4AC')

    def _loc_474(): pass

    label('loc_474')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_493',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 0x0018)

    Jump('loc_4AC')

    def _loc_493(): pass

    label('loc_493')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x000E)

    def _loc_4AC(): pass

    label('loc_4AC')

    Return()

# id: 0x0001 offset: 0x4AD
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFDDD20, 0xFFFE3AE0, 0x00230073)
    OP_22(0x01C5, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A5, 0, 0x1D28)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_4DD')

    def _loc_4D6(): pass

    label('loc_4D6')

    OP_6F(0x0001, 60)

    def _loc_4DD(): pass

    label('loc_4DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 7, 0x1C07)),
            Expr.Return,
        ),
        'loc_4FF',
    )

    OP_10(0x00, 0x01)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0010)
    OP_6F(0x0004, 30)
    OP_64(0x01, 0x0001)

    Jump('loc_502')

    def _loc_4FF(): pass

    label('loc_4FF')

    OP_10(0x00, 0x00)

    def _loc_502(): pass

    label('loc_502')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 4, 0x1C04)),
            Expr.Return,
        ),
        'loc_51F',
    )

    OP_A1(0x0012, 0x0003)
    SetChrPos(0x0012, -8590, -8500, -33600, 90)

    def _loc_51F(): pass

    label('loc_51F')

    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_1C(0x05, 0x00, 0x001C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_586',
    )

    LoadEffect(0x06, 'map\\\\mp027_00.eff')
    PlayEffect(0x06, 0x06, 0x00FF, -4500, -5000, -27040, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Jump('loc_58F')

    def _loc_586(): pass

    label('loc_586')

    OP_71(0x001D, 0x0004)
    OP_64(0x02, 0x0001)

    def _loc_58F(): pass

    label('loc_58F')

    Return()

# id: 0x0002 offset: 0x590
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 5, 0x1C0D)),
            Expr.Return,
        ),
        'loc_5F1',
    )

    ChrTalk(
        0x0015,
        (
            '#0310321154V#822F协会和军方应该\n',
            '马上就会派出支援……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321155V别太勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CD')

    def _loc_5F1(): pass

    label('loc_5F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 3, 0x1C0B)),
            Expr.Return,
        ),
        'loc_64F',
    )

    ChrTalk(
        0x0015,
        (
            '#0310321156V#824F只剩下亚妮拉丝了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321157V#822F抱歉，拜托你们了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CD')

    def _loc_64F(): pass

    label('loc_64F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 0, 0x1C08)),
            Expr.Return,
        ),
        'loc_6CD',
    )

    ChrTalk(
        0x0015,
        (
            '#0310321158V#826F呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321159V#824F不用管我，\n',
            '继续探索吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321160V卡露娜和亚妮拉丝就拜托你们了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CD(): pass

    label('loc_6CD')

    TalkEnd(0x0015)

    Return()

# id: 0x0003 offset: 0x6D1
@scena.Code('func_03_6D1')
def func_03_6D1():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 5, 0x1C0D)),
            Expr.Return,
        ),
        'loc_73F',
    )

    ChrTalk(
        0x0016,
        (
            '#0320321267V#833F没想到那个黑发小伙子\n',
            '也潜入了这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320321268V#834F希望他平安无事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AE')

    def _loc_73F(): pass

    label('loc_73F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 3, 0x1C0B)),
            Expr.Return,
        ),
        'loc_7AE',
    )

    ChrTalk(
        0x0016,
        (
            '#0320321269V#836F呜……\n',
            '不用管我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320321270V#835F就算这种状态之下，\n',
            '我们还是可以照顾自己的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7AE(): pass

    label('loc_7AE')

    TalkEnd(0x0016)

    Return()

# id: 0x0004 offset: 0x7B2
@scena.Code('func_04_7B2')
def func_04_7B2():
    TalkBegin(0x0017)
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0017,
        (
            '#0120321373V#813F我想约修亚\n',
            '可能去了屋顶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321374V#812F艾丝蒂尔……\n',
            '你要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00FE, 270, 0)
    TalkEnd(0x0017)

    Return()

# id: 0x0005 offset: 0x829
@scena.Code('func_05_829')
def func_05_829():
    UnlockAchievement(0x02, 0x9E, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A5, 0, 0x1D28)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_906',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['催眠曲奇'], 1)"),
            Expr.Return,
        ),
        'loc_89D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D28)

    Jump('loc_903')

    def _loc_89D(): pass

    label('loc_89D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_903(): pass

    label('loc_903')

    Jump('loc_937')

    def _loc_906(): pass

    label('loc_906')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_937(): pass

    label('loc_937')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_98F',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0043)"),
            Expr.Return,
        ),
        'loc_956',
    )

    Jump('loc_98F')

    def _loc_956(): pass

    label('loc_956')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_98F(): pass

    label('loc_98F')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x998
@scena.Code('func_06_998')
def func_06_998():
    EventBegin(0x00)
    OP_DB()
    OP_E8(0x88, 0x13, 0x00, 0x00)
    ClearMapFlags(0x00100000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9C4',
    )

    ClearMapFlags(0x00000010)
    Call(0, 0x0019)
    Call(0, 0x001A)
    SetMapFlags(0x00000010)

    def _loc_9C4(): pass

    label('loc_9C4')

    OP_6D(31040, -6770, 3020, 0)
    OP_67(0, 11880, -10000, 0)
    OP_6B(13600, 0)
    OP_6C(351000, 0)
    OP_6E(410, 0)
    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0002)
    OP_71(0x0003, 0x0040)
    OP_A1(0x0012, 0x0003)
    SetChrPos(0x0012, 70630, -7500, 40480, 45)
    SetChrFlags(0x0012, 0x0040)
    Yield()
    SetChrBattleFlags(0x0101, 0x0020)
    SetChrBattleFlags(0x0109, 0x0020)
    SetChrBattleFlags(0x00F8, 0x0020)
    SetChrBattleFlags(0x00F9, 0x0020)
    OP_89(0x0101, 70320, -7500, 39620, 225)
    OP_89(0x0109, 69800, -7500, 40000, 225)
    OP_89(0x00F8, 71200, -7500, 40440, 225)
    OP_89(0x00F9, 70680, -7500, 40990, 225)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0109, 0x0040)
    SetChrFlags(0x00F8, 0x0040)
    SetChrFlags(0x00F9, 0x0040)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0109, 0x0004)
    SetChrFlags(0x00F8, 0x0004)
    SetChrFlags(0x00F9, 0x0004)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0109, 0)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0109, 7)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD8',
    )

    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0103, 1)

    def _loc_AD8(): pass

    label('loc_AD8')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF0',
    )

    SetChrSubChip(0x0106, 0)
    SetChrChipByIndex(0x0106, 2)

    def _loc_AF0(): pass

    label('loc_AF0')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B08',
    )

    SetChrSubChip(0x0104, 0)
    SetChrChipByIndex(0x0104, 3)

    def _loc_B08(): pass

    label('loc_B08')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B20',
    )

    SetChrSubChip(0x0105, 0)
    SetChrChipByIndex(0x0105, 4)

    def _loc_B20(): pass

    label('loc_B20')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B38',
    )

    SetChrSubChip(0x0107, 0)
    SetChrChipByIndex(0x0107, 5)

    def _loc_B38(): pass

    label('loc_B38')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B50',
    )

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 6)

    def _loc_B50(): pass

    label('loc_B50')

    LoadEffect(0x00, 'map\\\\mp013_02.eff')
    LoadEffect(0x01, 'map\\\\mp013_00.eff')
    LoadEffect(0x02, 'map\\\\mp013_01.eff')
    PlayEffect(0x01, 0x01, 0x0012, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x02, 0x0012, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_72(0x001B, 0x0004)
    OP_71(0x0003, 0x0020)
    OP_B0(0x0003, 0x1E)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x000000F0)
    OP_22(0x00DA, 0x01, 0x28)
    OP_12(0x000088B8, 0x000927C0, 0x00000000)
    OP_C8(0x0200, 0x0046, 'C_PLAC18._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0C48')
    def lambda_0C48():
        OP_6D(11950, -8800, -2530, 6000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_0C48)

    @scena.Lambda('lambda_0C60')
    def lambda_0C60():
        OP_6C(3000, 6000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_0C60)

    @scena.Lambda('lambda_0C70')
    def lambda_0C70():
        OP_8F(0x0012, 10280, -8500, -33550, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_0C70)

    Sleep(6000)

    OP_C4(0x00, 0x00000040)
    FadeOut(500, 0, -1)
    OP_0D()
    TerminateThread(0x0012, 0x00)
    OP_12(0x000088B8, 0x0001D4C0, 0x00000000)
    OP_67(0, 8029, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(3000, 0)
    OP_6E(597, 0)
    OP_69(0x0012, 0x00000000)
    OP_6A(0x0012)

    @scena.Lambda('lambda_0CE8')
    def lambda_0CE8():
        OP_8F(0x0012, 10280, -8500, -33550, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_0CE8)

    FadeIn(500, 0)
    OP_24(0x00DA, 0x4B)
    OP_0D()
    Sleep(500)

    OP_E8(0xE8, 0x03, 0x00, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010321035V#1004F#6P#20A啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_56(0x00)
    OP_59()
    Sleep(300)

    ChrTalk(
        0x0109,
        (
            '#0180321036V#1063F#5P#30A看来突破了……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_56(0x00)
    OP_59()
    Sleep(500)

    OP_6A(0x00FF)
    OP_C4(0x01, 0x00000040)
    Fade(500)
    OP_6D(-9850, -6060, -34780, 0)
    OP_67(0, 10860, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_C4(0x01, 0x00000040)
    WaitForThreadExit(0x0012, 0x0000)

    @scena.Lambda('lambda_0DD6')
    def lambda_0DD6():
        OP_8C(0x00FE, 90, 0)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_0DD6)

    @scena.Lambda('lambda_0DE4')
    def lambda_0DE4():
        OP_8C(0x00FE, 270, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DE4)

    @scena.Lambda('lambda_0DF2')
    def lambda_0DF2():
        OP_8C(0x00FE, 270, 0)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_0DF2)

    @scena.Lambda('lambda_0E00')
    def lambda_0E00():
        OP_8C(0x00FE, 270, 0)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_0E00)

    @scena.Lambda('lambda_0E0E')
    def lambda_0E0E():
        OP_8C(0x00FE, 270, 0)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_0E0E)

    @scena.Lambda('lambda_0E1C')
    def lambda_0E1C():
        OP_8F(0x00FE, -8590, -8500, -33600, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0E1C)

    Sleep(400)

    OP_23(0x00DA)
    OP_22(0x00D4, 0x00, 0x64)
    Sleep(2600)

    @scena.Lambda('lambda_0E49')
    def lambda_0E49():
        OP_8F(0x00FE, -8590, -8500, -33600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0E49)

    Sleep(1500)

    @scena.Lambda('lambda_0E69')
    def lambda_0E69():
        OP_8F(0x00FE, -8590, -8500, -33600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0E69)

    Sleep(1000)

    @scena.Lambda('lambda_0E89')
    def lambda_0E89():
        OP_8F(0x00FE, -8590, -8500, -33600, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0E89)

    Sleep(1000)

    @scena.Lambda('lambda_0EA9')
    def lambda_0EA9():
        OP_8F(0x00FE, -8590, -8500, -33600, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0EA9)

    WaitForThreadExit(0x0012, 0x0001)
    OP_82(0x01, 0x00)
    OP_82(0x02, 0x00)
    PlayEffect(0x00, 0x00, 0x0012, 0, -180, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010321037V#1006F#6P好……抵达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F33')
    def lambda_0F33():
        OP_6D(-8500, -5850, -29870, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F33)

    @scena.Lambda('lambda_0F4B')
    def lambda_0F4B():
        OP_67(0, 7820, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F4B)

    @scena.Lambda('lambda_0F63')
    def lambda_0F63():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_0F63)

    @scena.Lambda('lambda_0F73')
    def lambda_0F73():
        OP_6B(3310, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_0F73)

    CreateThread(0x0109, 0x01, 0x00, 0x0008)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x000A)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, 0x0007)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0009)
    Sleep(500)

    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    OP_82(0x00, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010321038V#1002F#6P这附近看起来\n',
            '好像没有人的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321039V#1063F#5P不可掉以轻心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321040V总之只能慎重调查一下\n',
            '上面的建筑物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10CC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321041V#074F#5P何况，对手是他们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080321042V#072F要是觉得危险的话，\n',
            '就果断地撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1296')

    def _loc_10CC(): pass

    label('loc_10CC')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1141',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321043V#025F#5P何况，对手是他们哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030321044V#022F要是觉得危险的话，\n',
            '就果断地撤退哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1296')

    def _loc_1141(): pass

    label('loc_1141')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11B6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321045V#053F#5P何况，对手是他们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050321046V#050F要是觉得危险的话，\n',
            '就果断地撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1296')

    def _loc_11B6(): pass

    label('loc_11B6')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1226',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321047V#032F#5P何况，对手是他们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040321048V要是觉得危险的话，\n',
            '就果断地撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1296')

    def _loc_1226(): pass

    label('loc_1226')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1296',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321049V#047F#5P何况，对手是他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060321050V#042F要是觉得危险的话，\n',
            '就果断地撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1296(): pass

    label('loc_1296')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_131F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010321051V#1010F#6P嗯……说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321052V#1006F提妲。\n',
            '要努力跟上来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070321053V#062F#5P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1346')

    def _loc_131F(): pass

    label('loc_131F')

    ChrTalk(
        0x0101,
        (
            '#0010321054V#1006F#6P嗯……也对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1346(): pass

    label('loc_1346')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-9590, -5860, -29950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -9590, -5860, -29950, 270)
    SetChrPos(0x0001, -9590, -5860, -29950, 270)
    SetChrPos(0x0002, -9590, -5860, -29950, 270)
    SetChrPos(0x0003, -9590, -5860, -29950, 270)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x1C04)
    OP_28(0x0097, 0x04, 0x10)
    OP_28(0x0097, 0x04, 0x20)
    OP_28(0x0098, 0x04, 0x02)
    OP_28(0x0098, 0x04, 0x08)
    OP_28(0x0098, 0x01, 0x0001)
    OP_28(0x0098, 0x01, 0x0002)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1408
@scena.Code('func_07_1408')
def func_07_1408():
    ClearChrBattleFlags(0x00FE, 0x0020)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 65535)
    OP_8C(0x00FE, 0, 400)
    Sleep(200)

    OP_8E(0x00FE, -9230, -8500, -33230, 3000, 0x00)
    OP_96(0x00FE, 0xFFFFD97C, 0xFFFFE890, 0xFFFF8616, 0x000009C4, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    ClearChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrFlags(0x00FE, 0x0001)
    OP_8E(0x00FE, -10100, -6010, -30690, 2000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x0008 offset: 0x147E
@scena.Code('func_08_147E')
def func_08_147E():
    ClearChrBattleFlags(0x00FE, 0x0020)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 65535)
    OP_8C(0x00FE, 0, 400)
    Sleep(200)

    OP_96(0x00FE, 0xFFFFD97C, 0xFFFFE890, 0xFFFF8616, 0x000009C4, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    ClearChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrFlags(0x00FE, 0x0001)
    OP_8E(0x00FE, -9950, -5920, -29000, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0009 offset: 0x14E0
@scena.Code('func_09_14E0')
def func_09_14E0():
    ClearChrBattleFlags(0x00FE, 0x0020)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 65535)
    OP_8C(0x00FE, 0, 400)
    Sleep(200)

    OP_8E(0x00FE, -8360, -8500, -33160, 3000, 0x00)
    OP_96(0x00FE, 0xFFFFDEFE, 0xFFFFE890, 0xFFFF8648, 0x000009C4, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    ClearChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrFlags(0x00FE, 0x0001)
    OP_8E(0x00FE, -8100, -5970, -30530, 3000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x000A offset: 0x1556
@scena.Code('func_0A_1556')
def func_0A_1556():
    ClearChrBattleFlags(0x00FE, 0x0020)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 65535)
    OP_8C(0x00FE, 0, 400)
    Sleep(200)

    OP_96(0x00FE, 0xFFFFDEFE, 0xFFFFE890, 0xFFFF8648, 0x000009C4, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    ClearChrFlags(0x00FE, 0x0040)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrFlags(0x00FE, 0x0001)
    OP_8E(0x00FE, -8400, -5910, -28960, 2000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x000B offset: 0x15B8
@scena.Code('func_0B_15B8')
def func_0B_15B8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 5, 0x1C05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_174A',
    )

    EventBegin(0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Fade(1000)
    OP_6D(-14880, 0, -4710, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(26000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -14410, 0, -7130, 0)
    SetChrPos(0x0109, -15440, 0, -7210, 0)
    SetChrPos(0x00F8, -13390, 0, -6670, 0)
    SetChrPos(0x00F9, -16400, 0, -6540, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 2, 0x1C1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16E1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010321055V#1007F#4P打不开吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321056V#1067F#6P看来只好寻找\n',
            '别的入口了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1742')

    def _loc_16E1(): pass

    label('loc_16E1')

    ChrTalk(
        0x0101,
        (
            '#0010321057V#1002F#4P打不开吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321058V#1068F#6P果然只能从刚才\n',
            '那个入口潜入了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1742(): pass

    label('loc_1742')

    OP_A2(0x1C05)
    EventEnd(0x00)

    Jump('loc_178A')

    def _loc_174A(): pass

    label('loc_174A')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_178A(): pass

    label('loc_178A')

    Return()

# id: 0x000C offset: 0x178B
@scena.Code('func_0C_178B')
def func_0C_178B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-14460, 0, -2390, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(17000, 0)
    OP_6E(262, 0)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0010)
    OP_6F(0x0004, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x0000001E)
    OP_22(0x006D, 0x00, 0x64)
    OP_73(0x0004)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5610._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x1842
@scena.Code('func_0D_1842')
def func_0D_1842():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-14460, 0, -2390, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(17000, 0)
    OP_6E(262, 0)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0010)
    OP_6F(0x0004, 30)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0010)
    OP_6F(0x0004, 30)
    OP_70(0x0004, 0x00000000)
    OP_22(0x006D, 0x00, 0x64)
    OP_73(0x0004)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5610._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x1903
@scena.Code('func_0E_1903')
def func_0E_1903():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1928',
    )

    Call(0, 0x0019)
    Call(0, 0x001A)
    FormationDelMember(0x00, 0xFF)

    def _loc_1928(): pass

    label('loc_1928')

    OP_6D(-7800, 15000, 15500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(47000, 0)
    OP_6E(262, 0)
    OP_6D(-7430, 15000, 16250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(47000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0109, -6230, 15000, 20660, 0)
    SetChrPos(0x00F8, -6230, 15000, 20660, 0)
    SetChrPos(0x00F9, -6230, 15000, 20660, 0)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 1200)
    OP_A1(0x000E, 0x0000)
    SetChrPos(0x000E, -25800, 15150, 11920, 0)
    OP_72(0x001B, 0x0004)
    OP_A1(0x000F, 0x001B)
    SetChrPos(0x000F, -25800, 15250, 11920, 0)
    OP_72(0x001C, 0x0004)
    OP_72(0x001C, 0x0020)
    OP_6F(0x001C, 1200)
    OP_A1(0x0010, 0x001C)
    SetChrPos(0x0010, -25800, 15150, 11920, 0)
    Yield()
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0001)
    ClearChrFlags(0x000A, 0x0001)
    SetChrBattleFlags(0x0008, 0x0020)
    SetChrBattleFlags(0x0009, 0x0020)
    SetChrBattleFlags(0x000A, 0x0020)
    OP_89(0x0008, -25470, 18450, 9290, 90)
    OP_89(0x0009, -23100, 18450, 9890, 90)
    OP_89(0x000A, -23140, 18450, 8530, 90)
    SetChrChipByIndex(0x0008, 16)
    SetChrSubChip(0x0008, 0)
    OP_22(0x0075, 0x01, 0x46)
    OP_79(0x0C, 0x0002)
    OP_7B()
    FadeIn(1000, 0)
    OP_0D()
    OP_72(0x0006, 0x0010)
    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 0)
    OP_70(0x0006, 0x0000001E)
    OP_22(0x006D, 0x00, 0x64)
    OP_73(0x0006)
    Sleep(200)

    CreateThread(0x0109, 0x01, 0x00, 0x0011)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0012)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x0013)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180321453V#1069F#5P糟糕……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000006, 'loc_1B4C'),
        (0x00000004, 'loc_1B71'),
        (0x00000002, 'loc_1B96'),
        (0x00000005, 'loc_1BBD'),
        (0x00000003, 'loc_1BE2'),
        (0x00000007, 'loc_1C07'),
        (-1, 'loc_1C2A'),
    )

    def _loc_1B4C(): pass

    label('loc_1B4C')

    ChrTalk(
        0x0107,
        (
            '#0070321454V#065F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2A')

    def _loc_1B71(): pass

    label('loc_1B71')

    ChrTalk(
        0x0105,
        (
            '#0060321455V#043F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2A')

    def _loc_1B96(): pass

    label('loc_1B96')

    ChrTalk(
        0x0103,
        (
            '#0030321456V#523F#5P什…什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2A')

    def _loc_1BBD(): pass

    label('loc_1BBD')

    ChrTalk(
        0x0106,
        (
            '#0050321457V#057F#5P唔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2A')

    def _loc_1BE2(): pass

    label('loc_1BE2')

    ChrTalk(
        0x0104,
        (
            '#0040321458V#039F#5P唔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2A')

    def _loc_1C07(): pass

    label('loc_1C07')

    ChrTalk(
        0x0108,
        (
            '#0080321459V#077F#5P……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2A')

    def _loc_1C2A(): pass

    label('loc_1C2A')

    OP_DB()

    @scena.Lambda('lambda_1C31')
    def lambda_1C31():
        OP_6D(-18050, 24180, 6110, 3500)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_1C31)

    @scena.Lambda('lambda_1C49')
    def lambda_1C49():
        OP_67(0, 5750, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_1C49)

    @scena.Lambda('lambda_1C61')
    def lambda_1C61():
        OP_6C(315000, 3500)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1C61)

    @scena.Lambda('lambda_1C71')
    def lambda_1C71():
        OP_6E(341, 3500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1C71)

    @scena.Lambda('lambda_1C81')
    def lambda_1C81():
        OP_6B(1850, 3500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_1C81)

    Sleep(3000)

    SetChrPos(0x0014, -18050, 24180, 6110, 0)

    @scena.Lambda('lambda_1CA7')
    def lambda_1CA7():
        OP_69(0x0014, 0x00000000)
        Yield()

        Jump('lambda_1CA7')

    DispatchAsync2(0x0014, 0x0002, lambda_1CA7)

    OP_B0(0x0000, 0x3C)
    OP_6F(0x0000, 361)
    OP_70(0x0000, 0x00000230)
    Sleep(500)

    OP_22(0x0076, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_73(0x0000)
    Sleep(500)

    CreateThread(0x0109, 0x02, 0x00, 0x0014)
    OP_E8(0xDC, 0x05, 0x00, 0x00)
    LoadEffect(0x00, 'map\\mp021_00.eff')
    PlayEffect(0x00, 0x00, 0x000F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_23(0x0075)
    OP_22(0x0079, 0x01, 0x64)
    OP_22(0x00CC, 0x00, 0x64)
    OP_B0(0x0000, 0x1E)
    OP_6F(0x0000, 561)
    OP_70(0x0000, 0x0000028A)
    OP_B0(0x001C, 0x1E)
    OP_6F(0x001C, 561)
    OP_70(0x001C, 0x0000028A)

    @scena.Lambda('lambda_1D6F')
    def lambda_1D6F():
        OP_91(0x00FE, 0, 500, 0, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_1D6F)

    @scena.Lambda('lambda_1D8A')
    def lambda_1D8A():
        OP_91(0x00FE, 0, 1000, 0, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D8A)

    @scena.Lambda('lambda_1DA5')
    def lambda_1DA5():
        OP_91(0x00FE, 0, 1000, 0, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1DA5)

    @scena.Lambda('lambda_1DC0')
    def lambda_1DC0():
        OP_91(0x00FE, 0, 3000, 0, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1DC0)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_1DE0')
    def lambda_1DE0():
        OP_91(0x00FE, 0, 1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_1DE0)

    @scena.Lambda('lambda_1DFB')
    def lambda_1DFB():
        OP_91(0x00FE, 0, 1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DFB)

    @scena.Lambda('lambda_1E16')
    def lambda_1E16():
        OP_91(0x00FE, 0, 1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1E16)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_1E36')
    def lambda_1E36():
        OP_91(0x00FE, 0, 2000, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_1E36)

    @scena.Lambda('lambda_1E51')
    def lambda_1E51():
        OP_91(0x00FE, 0, 2000, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E51)

    @scena.Lambda('lambda_1E6C')
    def lambda_1E6C():
        OP_91(0x00FE, 0, 2000, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1E6C)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_1E8C')
    def lambda_1E8C():
        OP_91(0x00FE, 0, 2000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_1E8C)

    @scena.Lambda('lambda_1EA7')
    def lambda_1EA7():
        OP_91(0x00FE, 0, 2000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1EA7)

    @scena.Lambda('lambda_1EC2')
    def lambda_1EC2():
        OP_91(0x00FE, 0, 2000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1EC2)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_1EE2')
    def lambda_1EE2():
        OP_91(0x00FE, 0, 2000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_1EE2)

    @scena.Lambda('lambda_1EFD')
    def lambda_1EFD():
        OP_91(0x00FE, 0, 2000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1EFD)

    @scena.Lambda('lambda_1F18')
    def lambda_1F18():
        OP_91(0x00FE, 0, 2000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1F18)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_1F38')
    def lambda_1F38():
        OP_91(0x00FE, 0, 1000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_1F38)

    @scena.Lambda('lambda_1F53')
    def lambda_1F53():
        OP_91(0x00FE, 0, 1000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1F53)

    @scena.Lambda('lambda_1F6E')
    def lambda_1F6E():
        OP_91(0x00FE, 0, 1000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1F6E)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_1F8E')
    def lambda_1F8E():
        OP_91(0x00FE, 0, 1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_1F8E)

    @scena.Lambda('lambda_1FA9')
    def lambda_1FA9():
        OP_91(0x00FE, 0, 1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1FA9)

    @scena.Lambda('lambda_1FC4')
    def lambda_1FC4():
        OP_91(0x00FE, 0, 1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1FC4)

    WaitForThreadExit(0x000E, 0x0001)
    OP_82(0x00, 0x02)
    TerminateThread(0x0014, 0x02)
    CreateThread(0x000E, 0x03, 0x00, 0x0010)
    CreateThread(0x000E, 0x02, 0x00, 0x0016)

    @scena.Lambda('lambda_1FF9')
    def lambda_1FF9():
        OP_6D(-5580, 30000, 22960, 7000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_1FF9)

    @scena.Lambda('lambda_2011')
    def lambda_2011():
        OP_6C(95000, 7000)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_2011)

    @scena.Lambda('lambda_2021')
    def lambda_2021():
        OP_97(0x00FE, 0xFFFFD83C, 0x00002E90, 0x00020F58, 0x00001F40, 0x0001)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2021)

    @scena.Lambda('lambda_203D')
    def lambda_203D():
        OP_97(0x00FE, 0xFFFFD83C, 0x00002E90, 0x00020F58, 0x00001F40, 0x0001)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_203D)

    @scena.Lambda('lambda_2059')
    def lambda_2059():
        OP_97(0x00FE, 0xFFFFD83C, 0x00002E90, 0x00020F58, 0x00001F40, 0x0001)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2059)

    CreateThread(0x0009, 0x00, 0x00, 0x000F)
    Sleep(3000)

    OP_CA(0x1B, 0x01, 0x0000012C)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x000F, 0x0001)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_20A0')
    def lambda_20A0():
        OP_6D(16140, 40000, 5000, 5000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_20A0)

    @scena.Lambda('lambda_20B8')
    def lambda_20B8():
        OP_6B(3000, 5000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_20B8)

    @scena.Lambda('lambda_20C8')
    def lambda_20C8():
        OP_67(0, 6750, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_20C8)

    @scena.Lambda('lambda_20E0')
    def lambda_20E0():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_20E0)

    @scena.Lambda('lambda_20F6')
    def lambda_20F6():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_20F6)

    @scena.Lambda('lambda_210C')
    def lambda_210C():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_210C)

    Sleep(500)

    @scena.Lambda('lambda_2127')
    def lambda_2127():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00004650, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2127)

    @scena.Lambda('lambda_213D')
    def lambda_213D():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00004650, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_213D)

    @scena.Lambda('lambda_2153')
    def lambda_2153():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00004650, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2153)

    Sleep(500)

    @scena.Lambda('lambda_216E')
    def lambda_216E():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00005208, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_216E)

    @scena.Lambda('lambda_2184')
    def lambda_2184():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00005208, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2184)

    @scena.Lambda('lambda_219A')
    def lambda_219A():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00005208, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_219A)

    Sleep(500)

    @scena.Lambda('lambda_21B5')
    def lambda_21B5():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x000061A8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_21B5)

    @scena.Lambda('lambda_21CB')
    def lambda_21CB():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x000061A8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_21CB)

    @scena.Lambda('lambda_21E1')
    def lambda_21E1():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x000061A8, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_21E1)

    CreateThread(0x000E, 0x03, 0x00, 0x0017)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F7)
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x2221
@scena.Code('func_0F_2221')
def func_0F_2221():
    Sleep(1000)

    SetChrFlags(0x000A, 0x0002)
    SetChrSubChip(0x000A, 4)
    Sleep(50)

    SetChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 4)
    Sleep(50)

    SetChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 4)
    Sleep(1000)

    SetChrFlags(0x000A, 0x0002)
    SetChrSubChip(0x000A, 3)
    Sleep(50)

    SetChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 3)
    Sleep(50)

    SetChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 3)

    Return()

# id: 0x0010 offset: 0x227C
@scena.Code('func_10_227C')
def func_10_227C():
    OP_73(0x0000)
    OP_73(0x001C)
    OP_6F(0x0000, 651)
    OP_70(0x0000, 0x000002A8)
    OP_6F(0x001C, 651)
    OP_70(0x001C, 0x000002A8)
    OP_73(0x0000)
    OP_73(0x001C)
    OP_71(0x0000, 0x0020)
    OP_71(0x001C, 0x0020)
    OP_6F(0x0000, 680)
    OP_70(0x0000, 0x0000030C)
    OP_6F(0x001C, 680)
    OP_70(0x001C, 0x0000030C)

    Return()

# id: 0x0011 offset: 0x22CB
@scena.Code('func_11_22CB')
def func_11_22CB():
    OP_8E(0x00FE, -6160, 15000, 16940, 5000, 0x00)
    OP_8E(0x00FE, -8830, 15000, 15120, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Return()

# id: 0x0012 offset: 0x2312
@scena.Code('func_12_2312')
def func_12_2312():
    OP_8E(0x00FE, -6160, 15000, 16940, 5000, 0x00)
    OP_8E(0x00FE, -8020, 15000, 13910, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2368',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_23A6')

    def _loc_2368(): pass

    label('loc_2368')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_238F',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_23A6')

    def _loc_238F(): pass

    label('loc_238F')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_23A6(): pass

    label('loc_23A6')

    Return()

# id: 0x0013 offset: 0x23A7
@scena.Code('func_13_23A7')
def func_13_23A7():
    OP_8E(0x00FE, -6160, 15000, 16940, 5000, 0x00)
    OP_8E(0x00FE, -8060, 15000, 16260, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2402',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2440')

    def _loc_2402(): pass

    label('loc_2402')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2429',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2440')

    def _loc_2429(): pass

    label('loc_2429')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2440(): pass

    label('loc_2440')

    Return()

# id: 0x0014 offset: 0x2441
@scena.Code('func_14_2441')
def func_14_2441():
    Sleep(500)

    @scena.Lambda('lambda_244C')
    def lambda_244C():
        OP_91(0x00FE, -15000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_244C)

    Sleep(100)

    @scena.Lambda('lambda_246C')
    def lambda_246C():
        OP_91(0x00FE, -15000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_246C)

    Sleep(100)

    @scena.Lambda('lambda_248C')
    def lambda_248C():
        OP_91(0x00FE, -15000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_248C)

    Return()

# id: 0x0015 offset: 0x24A2
@scena.Code('func_15_24A2')
def func_15_24A2():
    Sleep(2000)

    @scena.Lambda('lambda_24AD')
    def lambda_24AD():
        OP_8E(0x00FE, 7500, 15000, 14770, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_24AD)

    Sleep(200)

    @scena.Lambda('lambda_24CD')
    def lambda_24CD():
        OP_8E(0x00FE, 6770, 15000, 13820, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_24CD)

    Sleep(200)

    @scena.Lambda('lambda_24ED')
    def lambda_24ED():
        OP_8E(0x00FE, 5670, 15000, 13020, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_24ED)

    WaitForThreadExit(0x0109, 0x0001)

    @scena.Lambda('lambda_250D')
    def lambda_250D():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_250D')

    DispatchAsync2(0x0109, 0x0001, lambda_250D)

    WaitForThreadExit(0x00F8, 0x0001)

    @scena.Lambda('lambda_2523')
    def lambda_2523():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_2523')

    DispatchAsync2(0x00F8, 0x0001, lambda_2523)

    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_2539')
    def lambda_2539():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_2539')

    DispatchAsync2(0x00F9, 0x0001, lambda_2539)

    Return()

# id: 0x0016 offset: 0x2545
@scena.Code('func_16_2545')
def func_16_2545():
    OP_73(0x0000)
    OP_73(0x001C)
    OP_22(0x0079, 0x00, 0x64)
    OP_6F(0x0000, 651)
    OP_70(0x0000, 0x000002A8)
    OP_6F(0x001C, 651)
    OP_70(0x001C, 0x000002A8)
    OP_73(0x0000)
    OP_73(0x001C)
    OP_71(0x0000, 0x0020)
    OP_71(0x001C, 0x0020)
    OP_6F(0x0000, 680)
    OP_70(0x0000, 0x0000030C)
    OP_6F(0x001C, 680)
    OP_70(0x001C, 0x0000030C)

    Return()

# id: 0x0017 offset: 0x2599
@scena.Code('func_17_2599')
def func_17_2599():
    OP_24(0x0079, 0x5A)
    Sleep(200)

    OP_24(0x0079, 0x50)
    Sleep(200)

    OP_24(0x0079, 0x46)
    Sleep(200)

    OP_24(0x0079, 0x3C)
    Sleep(200)

    OP_24(0x0079, 0x32)
    Sleep(200)

    OP_24(0x0079, 0x28)
    Sleep(200)

    OP_24(0x0079, 0x1E)
    Sleep(200)

    OP_23(0x0079)

    Return()

# id: 0x0018 offset: 0x25DC
@scena.Code('func_18_25DC')
def func_18_25DC():
    EventBegin(0x00)
    OP_C4(0x00, 0x00000002)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_25F6',
    )

    Call(0, 0x001B)

    def _loc_25F6(): pass

    label('loc_25F6')

    LoadEffect(0x01, 'map\\\\mp064_01.eff')
    LoadEffect(0x02, 'map\\\\mp065_01.eff')
    LoadEffect(0x03, 'map\\\\mp064_00.eff')
    LoadEffect(0x04, 'map\\\\mp065_00.eff')
    LoadEffect(0x05, 'map\\\\mp021_00.eff')
    OP_71(0x001B, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_6D(-13460, 15200, -850, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(6010, 0)
    OP_6C(0, 0)
    OP_6E(598, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000A, 0x0001)
    SetChrPos(0x000D, -26000, 18450, 11200, 180)
    OP_A1(0x0011, 0x0002)
    OP_71(0x0002, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x0F)
    OP_6F(0x0002, 501)
    OP_70(0x0002, 0x00000208)
    SetChrFlags(0x000A, 0x0020)
    SetChrFlags(0x000A, 0x0002)
    OP_CF(0x000A, 0x02, 'Frame85__ren')
    SetChrSubChip(0x000A, 1)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x0011, 0x0040)
    SetChrPos(0x0011, 21380, 20000, -38500, 0)
    OP_97(0x0011, 0x00004B6E, 0x000004A6, 0x000003E8, 0x00002710, 0x0001)
    PlayEffect(0x01, 0x00, 0x0011, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x01, 0x0011, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x02, 0x0011, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x03, 0x0011, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x04, 0x0011, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x05, 0x0011, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2880')
    def lambda_2880():
        OP_6D(-23510, 15200, 14990, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2880)

    @scena.Lambda('lambda_2898')
    def lambda_2898():
        OP_67(0, 7830, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2898)

    @scena.Lambda('lambda_28B0')
    def lambda_28B0():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28B0)

    @scena.Lambda('lambda_28C0')
    def lambda_28C0():
        OP_6B(4200, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_28C0)

    OP_22(0x0113, 0x01, 0x32)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(200)

    OP_24(0x0113, 0x3C)
    Sleep(200)

    OP_24(0x0113, 0x46)
    Sleep(200)

    OP_24(0x0113, 0x50)
    Sleep(200)

    OP_24(0x0113, 0x5A)
    Sleep(200)

    OP_24(0x0113, 0x64)
    OP_97(0x0011, 0x00004B6E, 0x000004A6, 0x000057E4, 0x00003E80, 0x0001)
    OP_97(0x0011, 0x00004B6E, 0x000004A6, 0x000057E4, 0x00003A98, 0x0001)
    OP_97(0x0011, 0x00004B6E, 0x000004A6, 0x000057E4, 0x000036B0, 0x0001)
    OP_97(0x0011, 0x00004B6E, 0x000004A6, 0x00004E20, 0x000032C8, 0x0001)
    PlayEffect(0x03, 0x06, 0x0011, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x07, 0x0011, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_8C(0x0011, 0, 400)
    OP_22(0x0114, 0x00, 0x64)
    PlayEffect(0x01, 0x06, 0x0011, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x07, 0x0011, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0002, 0x0020)
    OP_B0(0x0002, 0x0A)
    OP_6F(0x0002, 500)
    OP_70(0x0002, 0x000001E1)

    @scena.Lambda('lambda_2A57')
    def lambda_2A57():
        OP_8F(0x00FE, -25800, 20000, 11920, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2A57)

    Sleep(500)

    OP_82(0x00, 0x02)
    OP_82(0x01, 0x02)
    OP_82(0x02, 0x02)
    OP_82(0x03, 0x02)
    OP_82(0x04, 0x02)
    OP_82(0x05, 0x02)
    Sleep(500)

    OP_22(0x0116, 0x00, 0x64)
    Sleep(500)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_2A9D')
    def lambda_2A9D():
        OP_8C(0x00FE, 180, 50)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2A9D)

    Sleep(500)

    SetChrSubChip(0x000A, 2)
    Sleep(500)

    SetChrSubChip(0x000A, 3)
    Sleep(500)

    SetChrSubChip(0x000A, 4)
    Sleep(500)

    SetChrSubChip(0x000A, 5)
    WaitForThreadExit(0x0011, 0x0001)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    Fade(1000)
    OP_6D(-27510, 15200, 10990, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000A, 0x0001)
    SetChrPos(0x0011, -24960, 18450, 7270, 90)
    SetChrFlags(0x0011, 0x0001)
    ClearChrFlags(0x0011, 0x0080)

    ExecExpressionWithValue(
        0x0011,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000040)

    @scena.Lambda('lambda_2B7C')
    def lambda_2B7C():
        OP_8F(0x00FE, -24800, 15300, 7220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2B7C)

    PlayEffect(0x05, 0x00, 0x0011, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00CC, 0x00, 0x64)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 421)
    OP_70(0x0002, 0x000001CC)
    OP_0D()
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0011, 0x0001)
    OP_82(0x00, 0x02)
    OP_82(0x06, 0x02)
    OP_82(0x07, 0x02)
    OP_23(0x0113)
    OP_22(0x0088, 0x00, 0x64)
    OP_22(0x00F5, 0x00, 0x64)
    OP_7C(0x00000000, 0x0000012C, 0x00000FA0, 0x000001F4)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 421)
    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    Sleep(2000)

    OP_DB()

    ChrTalk(
        0x000A,
        (
            '#0220271102V#263F哈哈哈，把那些野猪一样的\n',
            '飞艇全部甩开了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000A, 0x0020)
    ClearChrFlags(0x000A, 0x0002)
    OP_8C(0x000A, 180, 0)
    OP_8C(0x000A, 270, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0220271103V#1306F谢谢你，『帕蒂尔·玛蒂尔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x03D4, 0x00, 0x64)
    Sleep(2000)

    SetChrPos(0x0008, -12840, 14800, 9830, 270)
    ClearChrFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#0140271104V#1P终于回来了，玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2D36')
    def lambda_2D36():
        OP_6D(-20330, 15000, 9930, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D36)

    ClearChrFlags(0x000A, 0x0020)
    ClearChrFlags(0x000A, 0x0002)
    OP_8C(0x000A, 180, 400)

    @scena.Lambda('lambda_2D5F')
    def lambda_2D5F():
        OP_8E(0x00FE, -15790, 15000, 9170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2D5F)

    WaitForThreadExit(0x0008, 0x0000)
    OP_8C(0x0008, 270, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000A,
        (
            '#0220271105V#265F#6P莱维！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000A, 0x0020)
    ClearChrFlags(0x000A, 0x0002)
    OP_CF(0x000A, 0x02, 'Frame86__ren')
    OP_8C(0x000A, 90, 0)
    SetChrChipByIndex(0x000A, 20)
    SetChrSubChip(0x000A, 0)
    SetChrFlags(0x000A, 0x0002)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(250)

    OP_22(0x00A3, 0x00, 0x64)
    SetChrFlags(0x000A, 0x0001)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_2E07')
    def lambda_2E07():
        OP_99(0x00FE, 0x02, 0x05, 0x0000028A)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_2E07)

    OP_96(0x000A, 0xFFFFAFC4, 0x00003A98, 0x0000240E, 0x00000258, 0x000009C4)
    SetChrFlags(0x000A, 0x0001)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x000A, 0x0000)

    @scena.Lambda('lambda_2E4E')
    def lambda_2E4E():
        OP_99(0x00FE, 0x06, 0x07, 0x000005DC)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_2E4E)

    WaitForThreadExit(0x000A, 0x0000)
    ClearChrFlags(0x000A, 0x0002)
    SetChrChipByIndex(0x000A, 10)
    SetChrSubChip(0x000A, 0)

    @scena.Lambda('lambda_2E72')
    def lambda_2E72():
        OP_8E(0x00FE, -17230, 15000, 9040, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2E72)

    @scena.Lambda('lambda_2E8D')
    def lambda_2E8D():
        OP_6D(-17430, 15000, 9790, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E8D)

    @scena.Lambda('lambda_2EA5')
    def lambda_2EA5():
        OP_67(0, 5290, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2EA5)

    @scena.Lambda('lambda_2EBD')
    def lambda_2EBD():
        OP_6B(3420, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2EBD)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0220271106V#261F#5P嘿嘿，我回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271107V玲可是按照你的吩咐，\n',
            '成功做完了实验哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271108V#123F呵呵，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271109V不过你把事情搞得\n',
            '还真是大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271110V#266F#5P因为这次说是\n',
            '不能杀人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271111V#1306F这么无聊\n',
            '至少要热闹热闹嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271112V托你的福\n',
            '开了个很开心的茶会哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271113V#124F呵呵……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271114V#120F实验的结果怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271115V#263F#5P这个嘛。\n',
            '还不坏吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271116V#260F虽然被教会的哥哥\n',
            '给搅了一下局……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271117V但运作很稳定，\n',
            '我想足够用于实战了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271118V#124F嗯，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271119V#267F#5P不过『福音』\n',
            '现在还不能量产吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271120V能否作为兵器使用，\n',
            '现在还无法确定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271121V#120F没有量产的必要啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271122V此次的实验也是\n',
            '单纯以测试新型\n',
            '『福音』的潜在能力为目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271123V并不是以制作兵器\n',
            '为目的的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271124V#264F#5P咦，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271125V#263F算了。\n',
            '我也没什么兴趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271126V#265F对了，话说回来……\n',
            '约修亚还没找到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271127V#124F啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271128V#120F我们为了扰乱军队而放出的\n',
            '人形兵器被破坏了好几架。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271129V恐怕就是他干的好事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271130V#262F#5P嗯～真有一手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271131V虽然玲也很擅长捉迷藏\n',
            '但还是敌不过约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271132V#268F啊～啊，不好玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271133V为什么不干脆\n',
            '返回结社呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271134V#124F谁知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271135V#267F#5P这么说来，教授倒是\n',
            '说过由于艾丝蒂尔的原因，\n',
            '约修亚才不会回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271136V艾丝蒂尔好像也在\n',
            '寻找约修亚呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271137V到底怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271138V#120F玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271139V教授说的话\n',
            '还是不要盲目相信的好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271140V#264F#5P为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271141V#124F所谓真相\n',
            '每个人的看法都不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271142V譬如月亮的脸\n',
            '被大家比喻成各种各样的形态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271143V#265F#5P比如小兔子啦，或者螃蟹之类的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271144V#120F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271145V教授所讲出来的“真实”\n',
            '和玲自己感悟到的“真实”是不同的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271146V你一定要自己去看，自己去感受，\n',
            '只有这样才能体会到属于玲自己的“真实”。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271147V#265F#5P嗯～听起来好深奥哦，\n',
            '玲不是很明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271148V#261F不过玲好像确实\n',
            '挺喜欢艾丝蒂尔她们…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271149V就算下次再见面，\n',
            '大概也不会马上就杀死她们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271150V#124F那就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0040)
    OP_8E(0x0008, -16500, 15000, 9000, 1500, 0x00)
    Sleep(500)

    Fade(250)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0008, 0x0002)
    ClearChrFlags(0x0008, 0x0001)
    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    OP_99(0x0008, 0x00, 0x02, 0x000003E8)
    OP_99(0x0008, 0x03, 0x06, 0x000003E8)
    OP_99(0x0008, 0x03, 0x06, 0x000003E8)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140271151V#123F#4P很了不起哦，玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271152V#261F#5P嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, -7420, 15000, 13980, 270)
    SetChrPos(0x000D, -7990, 15000, 14810, 270)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000D, 0x0080)

    NpcTalk(
        0x0009,
        '男性的声音',
        (
            '#0150271153V#1P呵呵，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000A, 0x00000000, 1500, 0x26, 0x27, 0x00000064, 0x00)
    Sleep(500)

    OP_63(0x000A)
    Sleep(500)

    Fade(250)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0008, 0x0002)
    SetChrFlags(0x0008, 0x0001)
    SetChrChipByIndex(0x0008, 8)
    SetChrSubChip(0x0008, 0)
    OP_0D()

    @scena.Lambda('lambda_3880')
    def lambda_3880():
        OP_8E(0x00FE, -17250, 15000, 7900, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3880)

    @scena.Lambda('lambda_389B')
    def lambda_389B():
        OP_8E(0x00FE, -15420, 15000, 8540, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_389B)

    Sleep(500)

    @scena.Lambda('lambda_38BB')
    def lambda_38BB():
        OP_8E(0x00FE, -15300, 15000, 9860, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_38BB)

    @scena.Lambda('lambda_38D6')
    def lambda_38D6():
        OP_6D(-16030, 15000, 9710, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_38D6)

    @scena.Lambda('lambda_38EE')
    def lambda_38EE():
        OP_6C(32000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38EE)

    @scena.Lambda('lambda_38FE')
    def lambda_38FE():
        OP_6B(3290, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_38FE)

    WaitForThreadExit(0x0008, 0x0001)
    OP_8C(0x0008, 90, 400)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000A,
        (
            '#0220271154V#265F#6P教授……\n',
            '还有肯帕雷拉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0190271155V#853F贵安，玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271156V#850F你在王都似乎\n',
            '过得相当愉快啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271157V#261F#6P嘿嘿嘿，还好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271158V#265F要是事先知道你要来的话，\n',
            '绝对会招待你一起参加的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271159V当时的场面可是非常热闹的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3AD7',
    )

    ChrTalk(
        0x000D,
        (
            '#0190271160V#851F呵呵，那可真是遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271161V我也请游击士大姐姐她们\n',
            '看了场人偶剧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271162V但比起你的茶会来，\n',
            '实在是不值一提啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B6C')

    def _loc_3AD7(): pass

    label('loc_3AD7')

    ChrTalk(
        0x000D,
        (
            '#0190271160V#851F呵呵，那可真是遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271164V我也请游击士大哥哥他们\n',
            '看了场人偶剧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271162V但比起你的茶会来，\n',
            '实在是不值一提啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B6C(): pass

    label('loc_3B6C')

    ChrTalk(
        0x0009,
        (
            '#0150271166V#1154F#2P哈哈，下次有机会\n',
            '再请我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271167V#1151F不过玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271168V你好像和艾丝蒂尔\n',
            '相当投缘吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271169V#263F#6P嘿嘿，还好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271170V#260F并不像教授说的那么讨厌，\n',
            '是个还挺不错的大姐姐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150271171V#1150F#2P哈哈，我也没\n',
            '说过她是个讨厌的人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271172V实话说，倒真是一个性格善良，\n',
            '魅力十足的小姑娘呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271173V#1154F只是，约修亚之所以不愿意回来，\n',
            '原因确实是因为她。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271174V对吧，莱维？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271175V#124F确实……\n',
            '我不否认这是原因之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150271176V#1151F#2P如何，玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271177V如果艾丝蒂尔成为我们的同伴，\n',
            '你会不会很高兴？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271178V#126F同……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220271179V#264F#6P让艾丝蒂尔成为同伴？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271180V#263F……嘻嘻。\n',
            '那当然好啊！很好玩的样子！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271181V#265F虽然实力还差得很远，\n',
            '但只要经过锻炼，应该也会很快变强吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271182V而且，如果艾丝蒂尔加入的话，\n',
            '约修亚也会回来对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150271183V#1151F#2P呵呵，这是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0190271184V#851F#5P啊哈哈，不愧是教授。\n',
            '你还真是有兴致呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271185V#124F教授，玩笑开过头了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271186V#121F即使是你，\n',
            '也不能无视本人的意志，\n',
            '强行将她拉入结社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271187V这可是『盟主』制定的`\n',
            '『噬身之蛇』规约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150271188V#1151F#2P哼哼，这自然不用你说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271189V你以为身为『蛇之使徒』的我\n',
            '会做出那种事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271190V包括你和约修亚在内，\n',
            '我也没有强迫过任何人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140271191V#120F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150271192V#1154F#2P要是那么做的话，\n',
            '难得的乐趣就都被破坏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271193V必须让她完全自愿地\n',
            '加入我们才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(500)

    OP_C4(0x01, 0x00000002)
    ClearMapFlags(0x02000000)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x4160
@scena.Code('func_19_4160')
def func_19_4160():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_41DD'),
        (0x00000001, 'loc_41E3'),
        (-1, 'loc_41E9'),
    )

    def _loc_41DD(): pass

    label('loc_41DD')

    OP_A2(0x1200)

    Jump('loc_41E9')

    def _loc_41E3(): pass

    label('loc_41E3')

    OP_A2(0x1201)

    Jump('loc_41E9')

    def _loc_41E9(): pass

    label('loc_41E9')

    Return()

# id: 0x001A offset: 0x41EA
@scena.Code('func_1A_41EA')
def func_1A_41EA():
    ClearMapFlags(0x00000001)
    OP_6D(-136530, -6000, 47970, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0008,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x001B offset: 0x4247
@scena.Code('func_1B_4247')
def func_1B_4247():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_42C1'),
        (0x00000001, 'loc_42C7'),
        (-1, 'loc_42CD'),
    )

    def _loc_42C1(): pass

    label('loc_42C1')

    OP_A2(0x1200)

    Jump('loc_42CD')

    def _loc_42C7(): pass

    label('loc_42C7')

    OP_A2(0x1201)

    Jump('loc_42CD')

    def _loc_42CD(): pass

    label('loc_42CD')

    Return()

# id: 0x001C offset: 0x42CE
@scena.Code('func_1C_42CE')
def func_1C_42CE():
    TalkBegin(0x00FF)
    OP_22(0x006D, 0x00, 0x64)
    TalkEnd(0x00FF)

    Return()

# id: 0x001D offset: 0x42DA
@scena.Code('func_1D_42DA')
def func_1D_42DA():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_432B',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_44E6')

    def _loc_432B(): pass

    label('loc_432B')

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
            TXT(0x00, '在这里休息\n'),
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
        'loc_44CB',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_82(0x06, 0x02)
    PlayEffect(0x06, 0x06, 0x00FF, -4500, -5000, -27040, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x001D, 0)
    OP_70(0x001D, 0x00000032)
    OP_73(0x001D)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x06, 0x02)
    LoadEffect(0x07, 'map\\\\mp027_01.eff')
    PlayEffect(0x07, 0x07, 0x00FF, -4500, -5000, -27040, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x07, 0x02)
    PlayEffect(0x06, 0x06, 0x00FF, -4500, -5000, -27040, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x001D, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_44CB(): pass

    label('loc_44CB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_44E5',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_44E5(): pass

    label('loc_44E5')

    Return()

    def _loc_44E6(): pass

    label('loc_44E6')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
