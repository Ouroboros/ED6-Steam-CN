import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5801_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5801   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5801.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT29/CH12310._CH', 'ED6_DT29/CH12310P._CP'),
        ('ED6_DT29/CH12311._CH', 'ED6_DT29/CH12311P._CP'),
        ('ED6_DT29/CH12060._CH', 'ED6_DT29/CH12060P._CP'),
        ('ED6_DT29/CH12061._CH', 'ED6_DT29/CH12061P._CP'),
        ('ED6_DT29/CH12190._CH', 'ED6_DT29/CH12190P._CP'),
        ('ED6_DT29/CH12191._CH', 'ED6_DT29/CH12191P._CP'),
        ('ED6_DT29/CH12970._CH', 'ED6_DT29/CH12970P._CP'),
        ('ED6_DT29/CH12971._CH', 'ED6_DT29/CH12971P._CP'),
        ('ED6_DT27/CH03760._CH', 'ED6_DT27/CH03760P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '莱奥尔刚依吉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵红',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵红',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵蓝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵蓝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '多伦',
            x                   = -47010,
            z                   = 0,
            y                   = -69580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '空贼蒂诺',
            x                   = -48100,
            z                   = 0,
            y                   = -71060,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '空贼罗尔',
            x                   = -49550,
            z                   = 3400,
            y                   = -69030,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '目标角色',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '居住区域『克雷德尔』１',
            x                   = -137160,
            z                   = 0,
            y                   = -63670,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x23A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -99450,
            z           = 0,
            y           = -40530,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -95800,
            z           = 0,
            y           = -68900,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -69300,
            z           = 0,
            y           = -39890,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -57180,
            z           = 0,
            y           = -118140,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -112940,
            z           = 0,
            y           = -110020,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x2C6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -102000,
            y           = 2000,
            z           = -105000,
            range       = 2000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -47500,
            y           = 4000,
            z           = -65140,
            range       = -45500,
            dword_10    = 0x00001770,
            dword_14    = 0xFFFF0574,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000014,
        ),
    )

# id: 0x10004 offset: 0x306
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -100970,
            triggerZ            = -7920,
            triggerY            = -119660,
            triggerRange        = 800,
            actorX              = -100500,
            actorZ              = -6520,
            actorY              = -119000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x32A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_376',
    )

    ChrSetPos(0x000D, -48740, 3410, -69080, 90)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000E, -46920, 0, -70650, 90)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000F, -47070, 0, -68910, 90)
    ChrClearFlags(0x000F, 0x0080)

    Jump('loc_391')

    def _loc_376(): pass

    label('loc_376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_391',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0010)

    def _loc_391(): pass

    label('loc_391')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3A7',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_11_388D)

    Jump('loc_400')

    def _loc_3A7(): pass

    label('loc_3A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_3B8',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_13_3A83)

    Jump('loc_400')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_3CE',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_0E_36A6)

    Jump('loc_400')

    def _loc_3CE(): pass

    label('loc_3CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_3DF',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    Event(0, func_0D_2FD4)

    Jump('loc_400')

    def _loc_3DF(): pass

    label('loc_3DF')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3EB'),
        (-1, 'loc_400'),
    )

    def _loc_3EB(): pass

    label('loc_3EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_400',
    )

    MapSetFlags(0x10000000)
    Event(0, func_05_1426)

    def _loc_400(): pass

    label('loc_400')

    Return()

# id: 0x0001 offset: 0x401
@scena.Code('func_01_401')
def func_01_401():
    OP_16(0x02, 4000, -212000, -209000, 2293880)
    PlaySE(455, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_10(0x02, 0x00)
    OP_72(0x0004, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 4, 0x221C)),
            Expr.Return,
        ),
        'loc_446',
    )

    OP_71(0x0004, 0x0010)
    OP_64(0x00, 0x0001)
    OP_71(0x0008, 0x0004)

    def _loc_446(): pass

    label('loc_446')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x50E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57A',
    )

    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 18)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 19)
    LoadChip('ED6_DT07/CH00312._CH', 'ED6_DT07/CH00312P._CP', 20)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_495'),
        (0x00000005, 'loc_4A2'),
        (0x00000003, 'loc_4AF'),
        (0x00000004, 'loc_4BC'),
        (0x00000006, 'loc_4C9'),
        (0x00000007, 'loc_4D6'),
        (0x00000008, 'loc_4E3'),
        (-1, 'loc_4F0'),
    )

    def _loc_495(): pass

    label('loc_495')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 21)

    Jump('loc_4F0')

    def _loc_4A2(): pass

    label('loc_4A2')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 21)

    Jump('loc_4F0')

    def _loc_4AF(): pass

    label('loc_4AF')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 21)

    Jump('loc_4F0')

    def _loc_4BC(): pass

    label('loc_4BC')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 21)

    Jump('loc_4F0')

    def _loc_4C9(): pass

    label('loc_4C9')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 21)

    Jump('loc_4F0')

    def _loc_4D6(): pass

    label('loc_4D6')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 21)

    Jump('loc_4F0')

    def _loc_4E3(): pass

    label('loc_4E3')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 21)

    Jump('loc_4F0')

    def _loc_4F0(): pass

    label('loc_4F0')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_515'),
        (0x00000005, 'loc_522'),
        (0x00000003, 'loc_52F'),
        (0x00000004, 'loc_53C'),
        (0x00000006, 'loc_549'),
        (0x00000007, 'loc_556'),
        (0x00000008, 'loc_563'),
        (-1, 'loc_570'),
    )

    def _loc_515(): pass

    label('loc_515')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 22)

    Jump('loc_570')

    def _loc_522(): pass

    label('loc_522')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 22)

    Jump('loc_570')

    def _loc_52F(): pass

    label('loc_52F')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 22)

    Jump('loc_570')

    def _loc_53C(): pass

    label('loc_53C')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 22)

    Jump('loc_570')

    def _loc_549(): pass

    label('loc_549')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 22)

    Jump('loc_570')

    def _loc_556(): pass

    label('loc_556')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 22)

    Jump('loc_570')

    def _loc_563(): pass

    label('loc_563')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 22)

    Jump('loc_570')

    def _loc_570(): pass

    label('loc_570')

    LoadChip('ED6_DT26/CH20401._CH', 'ED6_DT26/CH20401P._CP', 23)

    def _loc_57A(): pass

    label('loc_57A')

    Return()

# id: 0x0002 offset: 0x57B
@scena.Code('func_02_57B')
def func_02_57B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_590',
    )

    ChrSetFlags(0x000D, 0x0010)

    def _loc_590(): pass

    label('loc_590')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_80B',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_755',
    )

    ChrTurnDirection(0x000D, 0x010B, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0459, 3, 0x22CB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EA',
    )

    ChrTalk(
        0x000D,
        (
            '#0300400673V#490F哦，是乔丝特啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400674V现在要开始\n',
            '修复翼端了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400675V我正在鼓舞这些\n',
            '小子们的士气哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400676V#210F修理工作看来很顺利呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400677V希望『山猫号』也能\n',
            '早点恢复正常状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300400678V#490F交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400679V等你回来的时候，\n',
            '它就像新的一样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0459, 3, 0x22CB))

    Jump('loc_74B')

    def _loc_6EA(): pass

    label('loc_6EA')

    ChrTalk(
        0x000D,
        (
            '#0300400680V#490F我们也会\n',
            '拚命进行修理的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400679V等你回来的时候，\n',
            '它就像新的一样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_74B(): pass

    label('loc_74B')

    ChrSetDirection(0x000D, 90, 0)

    Jump('loc_808')

    def _loc_755(): pass

    label('loc_755')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D5',
    )

    ChrTalk(
        0x000D,
        (
            '#0300400682V#196F喂，你们几个！\n',
            '再加把劲啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400683V老是这副模样的话，\n',
            '能举起的东西都抬不起来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_808')

    def _loc_7D5(): pass

    label('loc_7D5')

    ChrTalk(
        0x000D,
        (
            '#0300400684V#196F好，再来一次！\n',
            '加把劲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0010)

    def _loc_808(): pass

    label('loc_808')

    Jump('loc_D2F')

    def _loc_80B(): pass

    label('loc_80B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_D2F',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 7, 0x2297)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AB7',
    )

    ChrTurnDirection(0x000D, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '#0300400685V#490F哦，乔丝特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400686V怎么样？\n',
            '还顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400687V#210F我没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400688V不过，修理的情况如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300400689V#197F现在勉强让它飞的话\n',
            '还是能飞的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400690V但是因为内部结构受了损伤，\n',
            '完全无法进行长距离的飞行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400691V如果不解决这个问题，\n',
            '就算逃出去也无法支撑到降落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400692V#212F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400693V#210F要是有什么需要的东西\n',
            '就尽管跟我说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400694V我会从『埃尔赛尤』那边\n',
            '偷偷拿过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300400695V#191F哈哈，全靠你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400696V#490F那么回头见，乔丝特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400697V遇到麻烦的话\n',
            '一定要马上叫我们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400698V不管在什么地方，\n',
            '我们都会赶过去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0452, 7, 0x2297))

    Jump('loc_BED')

    def _loc_AB7(): pass

    label('loc_AB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_B35',
    )

    ChrTurnDirection(0x000D, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '#0300400699V#490F回头见，乔丝特。\n',
            '好好加油哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400700V遇到麻烦时记得叫我们。\n',
            '我们会马上赶过去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BED')

    def _loc_B35(): pass

    label('loc_B35')

    ChrTalk(
        0x000D,
        (
            '#0300400689V#197F现在勉强让它飞的话\n',
            '还是能飞的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400690V但是因为内部结构受了损伤，\n',
            '完全无法进行长距离的飞行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400703V在修好那个部分之前，\n',
            '根本不可能离开这个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BED(): pass

    label('loc_BED')

    Jump('loc_D2F')

    def _loc_BF0(): pass

    label('loc_BF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CB6',
    )

    ChrTalk(
        0x000D,
        (
            '#0300400689V#197F现在勉强让它飞的话\n',
            '还是能飞的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400690V但是因为内部结构受了损伤，\n',
            '完全无法进行长距离的飞行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400703V在修好那个部分之前，\n',
            '根本不可能离开这个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_D2F')

    def _loc_CB6(): pass

    label('loc_CB6')

    ChrTalk(
        0x000D,
        (
            '#0300400707V#190F我负责修理船体，\n',
            '结构方面都交给吉尔处理了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400708V那家伙的脑袋很灵光，\n',
            '适合做这种细部工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D2F(): pass

    label('loc_D2F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0xD33
@scena.Code('func_03_D33')
def func_03_D33():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_F34',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E4D',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DF8',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现、现在要开始\n',
            '修理这条脚架……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽、虽然我们两个人\n',
            '要把它抬起来\n',
            '好像非常困难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不、不过为了小姐，\n',
            '我们会努力完成的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_E4A')

    def _loc_DF8(): pass

    label('loc_DF8')

    ChrTalk(
        0x00FE,
        (
            '现、现在要开始\n',
            '修理这条脚架……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很困难，\n',
            '不过我们会为了小姐努力的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E4A(): pass

    label('loc_E4A')

    Jump('loc_F31')

    def _loc_E4D(): pass

    label('loc_E4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EDF',
    )

    ChrTalk(
        0x00FE,
        (
            '现、现在要开始\n',
            '修理这条脚架……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽、虽然我们两个人\n',
            '要把它抬起来\n',
            '好像非常困难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶，至少多伦老大\n',
            '也来帮忙一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_F31')

    def _loc_EDF(): pass

    label('loc_EDF')

    ChrTalk(
        0x00FE,
        (
            '现、现在要把\n',
            '这条脚架抬起来吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大、大哥他们至少\n',
            '能不能来帮忙一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F31(): pass

    label('loc_F31')

    Jump('loc_1180')

    def _loc_F34(): pass

    label('loc_F34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_1180',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10A5',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0459, 4, 0x22CC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1046',
    )

    ChrTalk(
        0x000E,
        (
            '啊，小姐……\n',
            '回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#210F我来看看情况的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '飞船的状态怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '脚架虽然断了，\n',
            '不过其它部分几乎没受到损伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '就看内部结构的状况如何了，\n',
            '但似乎很快就能修好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#210F是吗……\n',
            '嗯，好好加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '是、是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0459, 4, 0x22CC))

    Jump('loc_10A2')

    def _loc_1046(): pass

    label('loc_1046')

    ChrTalk(
        0x000E,
        (
            '就看内部结构的状况如何了，\n',
            '但似乎很快就能修好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '为了小姐，\n',
            '我们会拚命努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10A2(): pass

    label('loc_10A2')

    Jump('loc_1180')

    def _loc_10A5(): pass

    label('loc_10A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_112C',
    )

    ChrTalk(
        0x000E,
        (
            '哦，你们几个……\n',
            '谢谢你们救了我们大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '目前这里也正在\n',
            '卯足全力修理飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我们可不想\n',
            '孤零零地被抛在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1180')

    def _loc_112C(): pass

    label('loc_112C')

    ChrTalk(
        0x000E,
        (
            '目前这里也正在\n',
            '卯足全力修理飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过要如何修理内部结构\n',
            '还是一个大问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1180(): pass

    label('loc_1180')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x1184
@scena.Code('func_04_1184')
def func_04_1184():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_134C',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12AE',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_125F',
    )

    ChrTalk(
        0x000F,
        (
            '要把这个抬起来，\n',
            '根本就是不可能的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '小姐请你帮忙\n',
            '向老大求情吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#212F我可不想听\n',
            '这些丧气话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你们是男人吧？\n',
            '让我看看你们的毅力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '小、小姐……\n',
            '不会吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_12AB')

    def _loc_125F(): pass

    label('loc_125F')

    ChrTalk(
        0x000F,
        (
            '要把这个抬起来，\n',
            '根本就是不可能的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '小姐请你帮忙\n',
            '向老大求情吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12AB(): pass

    label('loc_12AB')

    Jump('loc_1349')

    def _loc_12AE(): pass

    label('loc_12AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_130A',
    )

    ChrTalk(
        0x000F,
        (
            '要把这种东西抬起来，\n',
            '根本就是不可能的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '唉，多伦老大\n',
            '也真是乱来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_1349')

    def _loc_130A(): pass

    label('loc_130A')

    ChrTalk(
        0x000F,
        (
            '要把这个抬起来，\n',
            '根本就不可能啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '大哥也真是乱来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1349(): pass

    label('loc_1349')

    Jump('loc_1422')

    def _loc_134C(): pass

    label('loc_134C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_1422',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13DC',
    )

    ChrTalk(
        0x000F,
        (
            '唉唉～真的\n',
            '硬生生断掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '一般情况下断得彻底些\n',
            '还比较容易修理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '不过这种程度的话，\n',
            '还真要想想该怎么修了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_1422')

    def _loc_13DC(): pass

    label('loc_13DC')

    ChrTalk(
        0x000F,
        (
            '唔～这个翼端\n',
            '要怎么修理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '得先和多伦老大\n',
            '商量一下才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1422(): pass

    label('loc_1422')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x1426
@scena.Code('func_05_1426')
def func_05_1426():
    Call(0, 0x0006)
    Call(0, 0x0007)

    Return()

# id: 0x0006 offset: 0x142F
@scena.Code('func_06_142F')
def func_06_142F():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1446',
    )

    Call(0, 0x0015)
    Call(0, 0x0016)

    def _loc_1446(): pass

    label('loc_1446')

    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 10)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 11)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 12)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 13)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1493'),
        (0x00000005, 'loc_14AA'),
        (0x00000003, 'loc_14C1'),
        (0x00000004, 'loc_14D8'),
        (0x00000006, 'loc_14EF'),
        (0x00000007, 'loc_1506'),
        (0x00000008, 'loc_151D'),
        (-1, 'loc_1534'),
    )

    def _loc_1493(): pass

    label('loc_1493')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 14)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 15)

    Jump('loc_1534')

    def _loc_14AA(): pass

    label('loc_14AA')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 14)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 15)

    Jump('loc_1534')

    def _loc_14C1(): pass

    label('loc_14C1')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 14)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 15)

    Jump('loc_1534')

    def _loc_14D8(): pass

    label('loc_14D8')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 14)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 15)

    Jump('loc_1534')

    def _loc_14EF(): pass

    label('loc_14EF')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 14)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 15)

    Jump('loc_1534')

    def _loc_1506(): pass

    label('loc_1506')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 14)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 15)

    Jump('loc_1534')

    def _loc_151D(): pass

    label('loc_151D')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 14)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 15)

    Jump('loc_1534')

    def _loc_1534(): pass

    label('loc_1534')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1559'),
        (0x00000005, 'loc_1570'),
        (0x00000003, 'loc_1587'),
        (0x00000004, 'loc_159E'),
        (0x00000006, 'loc_15B5'),
        (0x00000007, 'loc_15CC'),
        (0x00000008, 'loc_15E3'),
        (-1, 'loc_15FA'),
    )

    def _loc_1559(): pass

    label('loc_1559')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 16)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 17)

    Jump('loc_15FA')

    def _loc_1570(): pass

    label('loc_1570')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 16)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 17)

    Jump('loc_15FA')

    def _loc_1587(): pass

    label('loc_1587')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 16)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 17)

    Jump('loc_15FA')

    def _loc_159E(): pass

    label('loc_159E')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 16)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 17)

    Jump('loc_15FA')

    def _loc_15B5(): pass

    label('loc_15B5')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 16)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 17)

    Jump('loc_15FA')

    def _loc_15CC(): pass

    label('loc_15CC')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 16)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 17)

    Jump('loc_15FA')

    def _loc_15E3(): pass

    label('loc_15E3')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 16)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 17)

    Jump('loc_15FA')

    def _loc_15FA(): pass

    label('loc_15FA')

    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 18)
    LoadChip('ED6_DT07/CH00312._CH', 'ED6_DT07/CH00312P._CP', 19)
    LoadChip('ED6_DT07/CH00314._CH', 'ED6_DT07/CH00314P._CP', 20)
    LoadChip('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP', 21)
    LoadChip('ED6_DT07/CH00313._CH', 'ED6_DT07/CH00313P._CP', 22)
    LoadChip('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP', 23)
    LoadChip('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP', 24)
    LoadChip('ED6_DT29/CH12354._CH', 'ED6_DT29/CH12354P._CP', 25)
    LoadChip('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP', 26)
    LoadChip('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP', 27)
    LoadChip('ED6_DT29/CH12354._CH', 'ED6_DT29/CH12354P._CP', 28)
    LoadChip('ED6_DT29/CH12312._CH', 'ED6_DT29/CH12312P._CP', 29)
    FormationAddMember(ChrTable['乔丝特2'], 0xFA, 0xFF)
    CameraMove(-120860, 0, -62110, 0)
    OP_67(0, 4740, -10000, 0)
    CameraSetDistance(3190, 0)
    OP_6C(299000, 0)
    OP_6E(309, 0)
    ChrSetPos(0x0101, -119030, 0, -63460, 90)
    ChrSetPos(0x0102, -119050, 0, -62270, 90)
    ChrSetPos(0x00F8, -120560, 0, -63510, 90)
    ChrSetPos(0x00F9, -120770, 0, -62110, 90)
    ChrSetPos(0x0146, -59210, 0, -63960, 270)
    ChrSetPos(0x0010, -59210, 0, -63960, 270)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -72000, 1000, -62940, 90)
    ChrSetPos(0x0009, -66760, 0, -59620, 135)
    ChrSetPos(0x000A, -68280, 0, -62740, 90)
    ChrSetPos(0x000B, -68300, 0, -64590, 90)
    ChrSetPos(0x000C, -66590, 0, -67870, 45)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x0009, 23)
    ChrSetChipByIndex(0x000A, 23)
    ChrSetChipByIndex(0x000B, 26)
    ChrSetChipByIndex(0x000C, 26)

    @scena.Lambda('lambda_17A6')
    def lambda_17A6():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_17A6')

    DispatchAsync2(0x0008, 0x0003, lambda_17A6)

    @scena.Lambda('lambda_17B9')
    def lambda_17B9():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_17B9')

    DispatchAsync2(0x0009, 0x0003, lambda_17B9)

    @scena.Lambda('lambda_17CC')
    def lambda_17CC():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_17CC')

    DispatchAsync2(0x000A, 0x0003, lambda_17CC)

    @scena.Lambda('lambda_17DF')
    def lambda_17DF():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_17DF')

    DispatchAsync2(0x000B, 0x0003, lambda_17DF)

    @scena.Lambda('lambda_17F2')
    def lambda_17F2():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_17F2')

    DispatchAsync2(0x000C, 0x0003, lambda_17F2)

    ChrSetSubChip(0x0146, 0)
    ChrSetChipByIndex(0x0146, 19)
    OP_26(503)
    LoadEffect(0x00, 'map\\mp003_00.eff')
    LoadEffect(0x01, 'monster\\msc0331.eff')
    LoadEffect(0x02, 'battle\\btbomb00.eff')
    OP_20(0x000003E8)
    FadeIn(1000, 0)
    OP_E3(0x00, 0x09, 0x00, 0x00)
    OP_E3(0x00, 0x0A, 0x00, 0x00)
    OP_E3(0x00, 0x0B, 0x00, 0x00)
    OP_E3(0x00, 0x0C, 0x00, 0x00)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18CD',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_190B')

    def _loc_18CD(): pass

    label('loc_18CD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18F4',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_190B')

    def _loc_18F4(): pass

    label('loc_18F4')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_190B(): pass

    label('loc_190B')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1937',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1975')

    def _loc_1937(): pass

    label('loc_1937')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_195E',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1975')

    def _loc_195E(): pass

    label('loc_195E')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_1975(): pass

    label('loc_1975')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010391181V#1004F#5P约修亚，看那个……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391182V#1044F#5P……嗯。\n',
            '怎么会出现在这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391183V#1042F！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(41)
    Sleep(500)

    @scena.Lambda('lambda_1A0B')
    def lambda_1A0B():
        CameraMove(-64629, 0, -63910, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1A0B)

    @scena.Lambda('lambda_1A23')
    def lambda_1A23():
        OP_67(0, 6510, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A23)

    @scena.Lambda('lambda_1A3B')
    def lambda_1A3B():
        CameraSetDistance(4510, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1A3B)

    @scena.Lambda('lambda_1A4B')
    def lambda_1A4B():
        OP_6C(296000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1A4B)

    OP_6E(453, 7000)
    Sleep(500)

    Fade(500)
    CameraMove(-64629, 0, -62690, 0)
    OP_67(0, 4370, -10000, 0)
    CameraSetDistance(2990, 0)
    OP_6C(307000, 0)
    OP_6E(333, 0)
    OP_0D()

    @scena.Lambda('lambda_1AAC')
    def lambda_1AAC():
        ChrWalkTo(0x00FE, -62860, 0, -62430, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1AAC)

    Sleep(50)

    @scena.Lambda('lambda_1ACC')
    def lambda_1ACC():
        ChrWalkTo(0x00FE, -62990, 0, -65770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_1ACC)

    Sleep(50)

    @scena.Lambda('lambda_1AEC')
    def lambda_1AEC():
        ChrWalkTo(0x00FE, -63300, 0, -63670, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1AEC)

    Sleep(50)

    @scena.Lambda('lambda_1B0C')
    def lambda_1B0C():
        ChrWalkTo(0x00FE, -63030, 0, -64830, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_1B0C)

    Sleep(50)

    CreateThread(0x0146, 0x00, 0x00, func_08_2C5F)
    WaitForThreadExit(0x0146, 0x0000)
    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000B, 0x0000)
    WaitForThreadExit(0x000C, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0146,
        (
            '#0090391184V#214F别、别过来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391185V如果再继续伤害『山猫号』的话，\n',
            '我是绝对不会放过你们的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BB9')
    def lambda_1BB9():
        CameraMove(-70470, 0, -61640, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1BB9)

    @scena.Lambda('lambda_1BD1')
    def lambda_1BD1():
        OP_67(0, 4130, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1BD1)

    @scena.Lambda('lambda_1BE9')
    def lambda_1BE9():
        CameraSetDistance(2890, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1BE9)

    ChrMoveTo(0x0008, -69080, 1000, -63370, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(250)
    ChrSetChipByIndex(0x0008, 29)
    OP_0D()
    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    PlayEffect(0x01, 0x00, 0x0008, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x0010, -1000, 0, 0, 0)

    @scena.Lambda('lambda_1C65')
    def lambda_1C65():
        CameraMove(-70470, 1500, -61640, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1C65)

    Sleep(1000)

    @scena.Lambda('lambda_1C82')
    def lambda_1C82():
        CameraMove(-67470, 0, -61640, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1C82)

    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x02, 0x01, 0x00FF, -59210, 0, -63960, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetSubChip(0x0146, 0)
    ChrSetChipByIndex(0x0146, 22)

    @scena.Lambda('lambda_1CE7')
    def lambda_1CE7():
        ChrJumpTo(0x00FE, -55400, 0, -63530, 1300, 5000)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_1CE7)

    OP_7C(400, 400, 3000, 500)
    Fade(500)
    CameraMove(-54060, 0, -63310, 0)
    OP_67(0, 5630, -10000, 0)
    CameraSetDistance(2390, 0)
    OP_6C(67000, 0)
    OP_6E(401, 0)
    ChrSetChipByIndex(0x0008, 0)
    WaitForThreadExit(0x0146, 0x0001)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0146, 0)
    ChrSetChipByIndex(0x0146, 20)

    @scena.Lambda('lambda_1D75')
    def lambda_1D75():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_1D75)

    ChrTalk(
        0x0146,
        (
            '#0090391186V#216F#5P啊呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0146, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_1DB3')
    def lambda_1DB3():
        CameraMove(-58360, 0, -63110, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1DB3)

    @scena.Lambda('lambda_1DCB')
    def lambda_1DCB():
        ChrWalkTo(0x00FE, -59900, 0, -61220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1DCB)

    Sleep(100)

    @scena.Lambda('lambda_1DEB')
    def lambda_1DEB():
        ChrWalkTo(0x00FE, -60700, 0, -62840, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1DEB)

    Sleep(150)

    @scena.Lambda('lambda_1E0B')
    def lambda_1E0B():
        ChrWalkTo(0x00FE, -60730, 0, -64319, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1E0B)

    Sleep(140)

    @scena.Lambda('lambda_1E2B')
    def lambda_1E2B():
        ChrWalkTo(0x00FE, -59980, 0, -65760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1E2B)

    Sleep(800)

    @scena.Lambda('lambda_1E4B')
    def lambda_1E4B():
        ChrWalkTo(0x00FE, -64900, 1000, -63890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1E4B)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    MapSetFlags(0x00000010)

    ChrTalk(
        0x0146,
        (
            '#0090391187V#413F呜呜……\n',
            '吉尔哥……多伦哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391188V#215F………约修亚…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -77950, 0, -65650, 90)

    NpcTalk(
        0x0101,
        '女孩的声音',
        (
            '#0010391189V哼哼，看来你遇到麻烦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)
    ChrSetChipByIndex(0x00F8, 14)
    ChrSetChipByIndex(0x00F9, 16)
    ChrSetPos(0x0101, -72190, 0, -64099, 90)
    ChrSetPos(0x0102, -72080, 0, -62770, 90)
    ChrSetPos(0x00F8, -73710, 0, -64580, 90)
    ChrSetPos(0x00F9, -73670, 0, -62730, 90)
    OP_62(0x0146, 0xFFFFFF38, 1500, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x0146, 2)
    Sleep(500)

    @scena.Lambda('lambda_1F96')
    def lambda_1F96():
        CameraMove(-66700, 0, -62400, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F96)

    @scena.Lambda('lambda_1FAE')
    def lambda_1FAE():
        OP_67(0, 5450, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FAE)

    @scena.Lambda('lambda_1FC6')
    def lambda_1FC6():
        CameraSetDistance(2390, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1FC6)

    @scena.Lambda('lambda_1FD6')
    def lambda_1FD6():
        OP_6C(54000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1FD6)

    @scena.Lambda('lambda_1FE6')
    def lambda_1FE6():
        OP_6E(417, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1FE6)

    @scena.Lambda('lambda_1FF6')
    def lambda_1FF6():
        ChrSetDirection(0x00FE, 270, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FF6)

    Sleep(100)

    @scena.Lambda('lambda_2009')
    def lambda_2009():
        ChrSetDirection(0x00FE, 270, 300)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2009)

    @scena.Lambda('lambda_2017')
    def lambda_2017():
        ChrSetDirection(0x00FE, 270, 300)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2017)

    Sleep(100)

    @scena.Lambda('lambda_202A')
    def lambda_202A():
        ChrSetDirection(0x00FE, 270, 300)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_202A)

    @scena.Lambda('lambda_2038')
    def lambda_2038():
        ChrSetDirection(0x00FE, 270, 300)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2038)

    WaitForThreadExit(0x0102, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0146,
        (
            '#0090391190V#213F#6P是无脑女！？\n',
            '……还、还有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391191V#1019F#5P我～说～啊，\n',
            '你说谁是无脑女啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391192V#1046F#5P有话待会儿再说！\n',
            '先解决掉它们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391193V#414F#6P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391194V#1007F#5P真受不了……烦人的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0146, 0x02, 0x00, 1000)
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0146, 19)
    ChrSetSubChip(0x0146, 0)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_2175')
    def lambda_2175():
        CameraMove(-62330, 0, -62850, 450)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2175)

    @scena.Lambda('lambda_218D')
    def lambda_218D():
        OP_67(0, 6930, -10000, 450)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_218D)

    @scena.Lambda('lambda_21A5')
    def lambda_21A5():
        CameraSetDistance(2000, 450)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_21A5)

    @scena.Lambda('lambda_21B5')
    def lambda_21B5():
        ChrMoveToRelativeAsync(0x00FE, 6000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_21B5)

    Sleep(30)

    @scena.Lambda('lambda_21D5')
    def lambda_21D5():
        ChrMoveToRelativeAsync(0x00FE, 6000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_21D5)

    @scena.Lambda('lambda_21F0')
    def lambda_21F0():
        ChrMoveToRelativeAsync(0x00FE, 6000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_21F0)

    Sleep(30)

    @scena.Lambda('lambda_2210')
    def lambda_2210():
        ChrMoveToRelativeAsync(0x00FE, 6000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_2210)

    Sleep(80)

    ChrSetChipByIndex(0x0146, 18)
    ChrSetFlags(0x0146, 0x1000)

    @scena.Lambda('lambda_223A')
    def lambda_223A():
        ChrMoveToRelativeAsync(0x00FE, -4000, 0, 0, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0146, 0x0000, lambda_223A)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0146, 0xFF)
    OP_B6(0x0045, 0x01)
    Battle(0x0000050E, 0x00300019, 0x00, 0x0000, 0xFF)

    Return()

# id: 0x0007 offset: 0x227A
@scena.Code('func_07_227A')
def func_07_227A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    TerminateThread(0x0146, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    CameraMove(-63860, 0, -65590, 0)
    OP_67(0, 6400, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(225000, 0)
    OP_6E(382, 0)
    ChrSetChipByIndex(0x0101, 18)
    ChrSetChipByIndex(0x0102, 19)
    ChrSetChipByIndex(0x0146, 20)
    ChrSetChipByIndex(0x00F8, 21)
    ChrSetChipByIndex(0x00F9, 22)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0146, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetPos(0x0101, -66370, 0, -65450, 90)
    ChrSetPos(0x0102, -66310, 0, -64010, 90)
    ChrSetPos(0x00F8, -67990, 0, -65870, 90)
    ChrSetPos(0x00F9, -67870, 0, -64340, 90)
    ChrSetPos(0x0146, -58480, 0, -64450, 270)

    @scena.Lambda('lambda_237D')
    def lambda_237D():
        CameraSetDistance(2300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_237D)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    Sleep(100)

    ChrSetChipByIndex(0x0146, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010391195V#1007F#6P呼……\n',
            '总算摆平了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391196V#1002F那个大家伙\n',
            '还真难对付……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391197V#1035F#4P那是结社的重型人形兵器，\n',
            '『据点武装者』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391198V#1043F一般都是拿来\n',
            '防卫据点用的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_249B')
    def lambda_249B():
        CameraMove(-61840, 0, -65830, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_249B)

    @scena.Lambda('lambda_24B3')
    def lambda_24B3():
        ChrWalkTo(0x00FE, -61790, 0, -64099, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_24B3)

    Sleep(100)

    @scena.Lambda('lambda_24D3')
    def lambda_24D3():
        ChrWalkTo(0x00FE, -61940, 0, -65430, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_24D3)

    Sleep(80)

    @scena.Lambda('lambda_24F3')
    def lambda_24F3():
        ChrWalkTo(0x00FE, -63560, 0, -65870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_24F3)

    Sleep(120)

    @scena.Lambda('lambda_2513')
    def lambda_2513():
        ChrWalkTo(0x00FE, -63290, 0, -64360, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_2513)

    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020391199V#1040F#2P总之……\n',
            '你没事真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391200V不过，为什么你们\n',
            '会在这种地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391201V#215F#6P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391202V#413F自从我们和你分开后，\n',
            '就一直潜伏在国境附近……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391203V不过天空中突然出现了奇怪的东西，\n',
            '于是我们就飞过去看个究竟，\n',
            '然后山猫号的导力就停止了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391204V#1007F#5P所以就坠落下来了是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391205V#1004F对了，说到这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010391206V#1015F#5P……你那些\n',
            '哥哥们怎么样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391207V#1016F完全没看到他们，\n',
            '是不是出去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0146, 15, 0, 300, 3000)
    Sleep(500)

    ChrTalk(
        0x0146,
        (
            '#0090391208V#215F#6P…………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391209V#413F呜呜……呜呜………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010391210V#1020F#5P哇呀，你、你怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391211V#1035F#2P乔丝特……冷静一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391212V#1040F能不能慢慢地\n',
            '把事情说给我们听？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0146, 15, 0, 300, 3000)
    Sleep(500)

    ChrTalk(
        0x0146,
        (
            '#0090391213V#417F#6P呜呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391214V#418F约修亚……约修亚～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_28D0')
    def lambda_28D0():
        ChrTurnDirection(0x00FE, 0x0146, 400)
        Yield()

        Jump('lambda_28D0')

    DispatchAsync2(0x0101, 0x0002, lambda_28D0)

    @scena.Lambda('lambda_28E1')
    def lambda_28E1():
        ChrTurnDirection(0x00FE, 0x0146, 400)
        Yield()

        Jump('lambda_28E1')

    DispatchAsync2(0x0102, 0x0002, lambda_28E1)

    @scena.Lambda('lambda_28F2')
    def lambda_28F2():
        ChrTurnDirection(0x00FE, 0x0146, 400)
        Yield()

        Jump('lambda_28F2')

    DispatchAsync2(0x00F8, 0x0002, lambda_28F2)

    @scena.Lambda('lambda_2903')
    def lambda_2903():
        ChrTurnDirection(0x00FE, 0x0146, 0)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2903)

    @scena.Lambda('lambda_2911')
    def lambda_2911():
        CameraMove(-62450, 0, -65050, 1500)

        ExitThread()

    DispatchAsync(0x0146, 0x0003, lambda_2911)

    ChrSetFlags(0x0146, 0x0040)

    @scena.Lambda('lambda_292E')
    def lambda_292E():
        ChrWalkTo(0x0146, -61450, 0, -64099, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0146, 0x0000, lambda_292E)

    WaitForThreadExit(0x0146, 0x0000)

    @scena.Lambda('lambda_294E')
    def lambda_294E():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_294E')

    DispatchAsync2(0x0101, 0x0002, lambda_294E)

    ChrSetFlags(0x0146, 0x0002)
    ChrSetSubChip(0x0146, 0)
    ChrSetChipByIndex(0x0146, 23)

    @scena.Lambda('lambda_296E')
    def lambda_296E():
        ChrMoveTo(0x00FE, -62000, 0, -64099, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_296E)

    WaitForThreadExit(0x0102, 0x0000)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29CB',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2A09')

    def _loc_29CB(): pass

    label('loc_29CB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29F2',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2A09')

    def _loc_29F2(): pass

    label('loc_29F2')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_2A09(): pass

    label('loc_2A09')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A35',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2A73')

    def _loc_2A35(): pass

    label('loc_2A35')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A5C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2A73')

    def _loc_2A5C(): pass

    label('loc_2A5C')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_2A73(): pass

    label('loc_2A73')

    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AB4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391215V#1164F………啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AB4(): pass

    label('loc_2AB4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AE7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391216V#065F……啊啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AE7(): pass

    label('loc_2AE7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B18',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391217V#037F哎呀哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B18(): pass

    label('loc_2B18')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B47',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391218V#027F哎呀呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B47(): pass

    label('loc_2B47')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B75',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391219V#1064F哎哟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B75(): pass

    label('loc_2B75')

    ChrTalk(
        0x0101,
        (
            '#0010391220V#1020F#5P什、什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090391221V#418F#6P哥、哥哥他们\n',
            '被结社那些家伙抓走了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391222V大家为了掩护我逃走，\n',
            '特意去引诱敌人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391223V#417F约修亚……\n',
            '我该……怎么办才好！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2C5F
@scena.Code('func_08_2C5F')
def func_08_2C5F():
    ChrSetDirection(0x00FE, 315, 500)

    @scena.Lambda('lambda_2C6C')
    def lambda_2C6C():
        OP_99(0x00FE, 0x00, 0x07, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2C6C)

    Sleep(300)

    TerminateThread(0x0008, 0x00)
    CreateThread(0x0009, 0x00, 0x00, func_09_2D1A)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 225, 500)

    @scena.Lambda('lambda_2C98')
    def lambda_2C98():
        OP_99(0x00FE, 0x00, 0x07, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C98)

    Sleep(300)

    TerminateThread(0x000C, 0x00)
    CreateThread(0x000C, 0x00, 0x00, func_0C_2F29)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 270, 500)

    @scena.Lambda('lambda_2CC4')
    def lambda_2CC4():
        OP_99(0x00FE, 0x00, 0x04, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2CC4)

    Sleep(200)

    TerminateThread(0x000A, 0x00)
    CreateThread(0x000A, 0x00, 0x00, func_0A_2DC5)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 270, 500)
    Sleep(200)

    @scena.Lambda('lambda_2CF5')
    def lambda_2CF5():
        OP_99(0x00FE, 0x00, 0x06, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2CF5)

    TerminateThread(0x000B, 0x00)
    CreateThread(0x000B, 0x00, 0x00, func_0B_2E7E)
    WaitForThreadExit(0x00FE, 0x0001)
    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0009 offset: 0x2D1A
@scena.Code('func_09_2D1A')
def func_09_2D1A():
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x00FE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(50, 50, 3000, 100)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 25)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_2D7A')
    def lambda_2D7A():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2D7A)

    ChrMoveTo(0x00FE, -66760, 0, -59620, 16000, 0x00)
    WaitForThreadExit(0x00FE, 0x0003)
    ChrClearFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 23)

    @scena.Lambda('lambda_2DB7')
    def lambda_2DB7():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_2DB7')

    DispatchAsync2(0x00FE, 0x0003, lambda_2DB7)

    Return()

# id: 0x000A offset: 0x2DC5
@scena.Code('func_0A_2DC5')
def func_0A_2DC5():
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x00FE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(50, 50, 3000, 100)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 25)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_2E25')
    def lambda_2E25():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E25)

    @scena.Lambda('lambda_2E3F')
    def lambda_2E3F():
        ChrSetDirection(0x00FE, 135, 0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2E3F)

    ChrMoveTo(0x00FE, -67760, 0, -61410, 16000, 0x00)
    WaitForThreadExit(0x00FE, 0x0003)
    ChrClearFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 23)

    @scena.Lambda('lambda_2E70')
    def lambda_2E70():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_2E70')

    DispatchAsync2(0x00FE, 0x0003, lambda_2E70)

    Return()

# id: 0x000B offset: 0x2E7E
@scena.Code('func_0B_2E7E')
def func_0B_2E7E():
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0x02, 0x00FE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(50, 50, 3000, 100)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 28)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_2EDE')
    def lambda_2EDE():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2EDE)

    ChrMoveTo(0x00FE, -67530, 0, -65990, 16000, 0x00)
    WaitForThreadExit(0x00FE, 0x0003)
    ChrClearFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 26)

    @scena.Lambda('lambda_2F1B')
    def lambda_2F1B():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_2F1B')

    DispatchAsync2(0x00FE, 0x0003, lambda_2F1B)

    Return()

# id: 0x000C offset: 0x2F29
@scena.Code('func_0C_2F29')
def func_0C_2F29():
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0x03, 0x00FE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(50, 50, 3000, 100)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 28)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_2F89')
    def lambda_2F89():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F89)

    ChrMoveTo(0x00FE, -66590, 0, -67870, 16000, 0x00)
    WaitForThreadExit(0x00FE, 0x0003)
    ChrClearFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 26)

    @scena.Lambda('lambda_2FC6')
    def lambda_2FC6():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_2FC6')

    DispatchAsync2(0x00FE, 0x0003, lambda_2FC6)

    Return()

# id: 0x000D offset: 0x2FD4
@scena.Code('func_0D_2FD4')
def func_0D_2FD4():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FEB',
    )

    Call(0, 0x0015)
    Call(0, 0x000F)

    def _loc_2FEB(): pass

    label('loc_2FEB')

    CameraMove(-83690, 0, -60600, 0)
    OP_67(0, 6340, -10000, 0)
    CameraSetDistance(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -84410, 0, -62530, 0)
    ChrSetPos(0x0102, -83090, 0, -61240, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_307C',
    )

    ChrSetPos(0x00F9, -85770, 0, -61600, 90)
    ChrSetPos(0x010B, -84210, 0, -59930, 180)

    Jump('loc_30D0')

    def _loc_307C(): pass

    label('loc_307C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30AE',
    )

    ChrSetPos(0x00F8, -85770, 0, -61600, 90)
    ChrSetPos(0x010B, -84210, 0, -59930, 180)

    Jump('loc_30D0')

    def _loc_30AE(): pass

    label('loc_30AE')

    ChrSetPos(0x00F8, -84210, 0, -59930, 180)
    ChrSetPos(0x00F9, -85770, 0, -61600, 90)

    def _loc_30D0(): pass

    label('loc_30D0')

    ChrSetStatus(0x00FF, 0xFE, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_355C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010391306V#1006F那么……\n',
            '要继续探索吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391307V#1004F……对了，乔丝特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391308V在这附近有没有\n',
            '通往其它地方的出口？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090391309V#413F#5P嗯……\n',
            '我没有看到呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391310V#212F通向隔壁街区的桥梁\n',
            '也完全崩塌了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391311V#1007F唔……这可伤脑筋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391312V#1040F总之先调查一下\n',
            '街上的情况吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391313V或许会发现\n',
            '什么线索也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_326F')
    def lambda_326F():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_326F)

    Sleep(50)

    ChrTurnDirection(0x010B, 0x0102, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010391314V#1019F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090391315V#212F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391316V#1048F那个，我……',
            TxtCtl.Enter,
            '\n',
            '#1052F…………对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391317V#1001F#6P咦，为什么要道歉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090391318V#211F#5P没线索\n',
            '又不是你的错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33C6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391319V#067F#6P（真、真可怜……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3559')

    def _loc_33C6(): pass

    label('loc_33C6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_340B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391320V#551F#6P（看上去是如坐针毡啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3559')

    def _loc_340B(): pass

    label('loc_340B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3451',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391321V#1068F#6P（真挺得住啊，约修亚……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3559')

    def _loc_3451(): pass

    label('loc_3451')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3494',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391322V#070F#6P（真是的，还年轻啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3559')

    def _loc_3494(): pass

    label('loc_3494')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34DD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391323V#027F#6P（呵呵，这也是青春的一面吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3559')

    def _loc_34DD(): pass

    label('loc_34DD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_351D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391324V#1380F#6P（还真是可怜啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3559')

    def _loc_351D(): pass

    label('loc_351D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3559',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391325V#031F#6P（呵呵～很有意思。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3559(): pass

    label('loc_3559')

    Jump('loc_369A')

    def _loc_355C(): pass

    label('loc_355C')

    ChrTalk(
        0x0101,
        (
            '#0010391326V#1006F那么，接下来\n',
            '要继续探索这个区域吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391327V#1015F据乔丝特所说，\n',
            '好像还没有找到\n',
            '通往其它地方的出口……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391328V#1035F嗯，而且通往隔壁\n',
            '街区的桥梁也完全崩塌了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391312V#1040F总之先调查一下\n',
            '街上的情况吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391313V或许会发现\n',
            '什么线索也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391331V#1006F了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_369A(): pass

    label('loc_369A')

    SetScenaFlags(ScenaFlag(0x0443, 1, 0x2219))
    OP_28(0x009D, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x36A6
@scena.Code('func_0E_36A6')
def func_0E_36A6():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_12(0x0000D6D8, 0x00061A80, 0x00000000)
    CameraMove(-42870, 0, -61220, 0)
    OP_67(0, 8500, -10000, 0)
    CameraSetDistance(8000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x000E, -46920, 0, -70650, 90)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000F, -47070, 0, -68910, 90)
    ChrClearFlags(0x000F, 0x0080)
    FadeIn(1000, 0)
    OP_12(0x0000D6D8, 0x00030D40, 0x00001F40)

    @scena.Lambda('lambda_374E')
    def lambda_374E():
        CameraMove(-84570, 2000, -53000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_374E)

    @scena.Lambda('lambda_3766')
    def lambda_3766():
        OP_67(0, 6500, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3766)

    @scena.Lambda('lambda_377E')
    def lambda_377E():
        CameraSetDistance(6500, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_377E)

    @scena.Lambda('lambda_378E')
    def lambda_378E():
        OP_6C(327000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_378E)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5810._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x37C4
@scena.Code('func_0F_37C4')
def func_0F_37C4():
    FadeOut(0, 0, -1)
    CameraMove(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x0010 offset: 0x3857
@scena.Code('func_10_3857')
def func_10_3857():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地锁着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0011 offset: 0x388D
@scena.Code('func_11_388D')
def func_11_388D():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-101730, 2000, -104530, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    CameraMove(-103060, -8000, -116730, 7000)
    Fade(500)
    CameraMove(-103060, -8000, -116730, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    PlaySE(170, 0x00, 0x64)
    OP_71(0x0008, 0x0004)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C6001._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x3969
@scena.Code('func_12_3969')
def func_12_3969():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101850, 2000, -104940, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_89(0x0101, -101000, 2000, -105000, 90)
    OP_89(0x0102, -102000, 2000, -104000, 90)
    OP_89(0x00F8, -103000, 2000, -105000, 90)
    OP_89(0x00F9, -102000, 2000, -106000, 90)
    OP_0D()
    Sleep(100)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 1200)
    OP_12(0x0000D6D8, 0x0006DDD0, 0x00001F40)

    @scena.Lambda('lambda_3A22')
    def lambda_3A22():
        CameraMove(-101850, 50000, -104940, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3A22)

    @scena.Lambda('lambda_3A3A')
    def lambda_3A3A():
        OP_67(0, 10680, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3A3A)

    @scena.Lambda('lambda_3A52')
    def lambda_3A52():
        OP_6C(50000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3A52)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C6001._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x3A83
@scena.Code('func_13_3A83')
def func_13_3A83():
    EventBegin(0x00)
    CameraMove(-101850, 60000, -104940, 0)
    OP_67(0, 10680, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    OP_11(0xED, 0xFF, 0xEE, 55000, 450000, 0)
    OP_6F(0x0005, 600)
    Yield()
    OP_89(0x0101, -101000, 80000, -105000, 90)
    OP_89(0x0102, -102000, 80000, -104000, 90)
    OP_89(0x00F8, -103000, 80000, -105000, 90)
    OP_89(0x00F9, -102000, 80000, -106000, 90)
    PlaySE(235, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_12(0x0000D6D8, 0x000186A0, 0x00002328)

    @scena.Lambda('lambda_3B3F')
    def lambda_3B3F():
        CameraMove(-101850, 2000, -104940, 10500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B3F)

    @scena.Lambda('lambda_3B57')
    def lambda_3B57():
        OP_67(0, 6500, -10000, 10500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3B57)

    @scena.Lambda('lambda_3B6F')
    def lambda_3B6F():
        OP_6C(45000, 10500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3B6F)

    OP_70(0x0005, 0)
    OP_73(0x0005)
    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(200)

    Fade(500)
    CameraMove(-100250, 2009, -105250, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -100250, 2009, -105250, 90)
    ChrSetPos(0x0001, -100250, 2009, -105250, 90)
    ChrSetPos(0x0002, -100250, 2009, -105250, 90)
    ChrSetPos(0x0003, -100250, 2009, -105250, 90)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x3C1A
@scena.Code('func_14_3C1A')
def func_14_3C1A():
    EventBegin(0x02)
    FadeOut(1000, 0, -1)
    OP_0D()
    NewScene('ED6_DT21/E0111._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x3C31
@scena.Code('func_15_3C31')
def func_15_3C31():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_3CAB'),
        (0x00000001, 'loc_3CB1'),
        (-1, 'loc_3CB7'),
    )

    def _loc_3CAB(): pass

    label('loc_3CAB')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3CB7')

    def _loc_3CB1(): pass

    label('loc_3CB1')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3CB7')

    def _loc_3CB7(): pass

    label('loc_3CB7')

    Return()

# id: 0x0016 offset: 0x3CB8
@scena.Code('func_16_3CB8')
def func_16_3CB8():
    FadeOut(0, 0, -1)
    CameraMove(-182260, 0, -191970, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
