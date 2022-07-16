import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '吉米'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '照相机'),
    TXT(0x06, ''),
    TXT(0x07, '玛诺利亚村方向'),
    TXT(0x08, '卢安方向'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2201.x'
    header.mapIndex       = 101
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/R2201._SN', 'ED6_DT01/R2201_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x942
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
            word_3A         = 101,
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT09/CH10230._CH', 'ED6_DT09/CH10230P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT09/CH10460._CH', 'ED6_DT09/CH10460P._CP'),
        ('ED6_DT09/CH10461._CH', 'ED6_DT09/CH10461P._CP'),
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
        ('ED6_DT09/CH10480._CH', 'ED6_DT09/CH10480P._CP'),
        ('ED6_DT09/CH10481._CH', 'ED6_DT09/CH10481P._CP'),
        ('ED6_DT09/CH10470._CH', 'ED6_DT09/CH10470P._CP'),
        ('ED6_DT09/CH10471._CH', 'ED6_DT09/CH10471P._CP'),
    ]

# id: 0x10002 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 72800,
            z                   = -6000,
            y                   = 3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 76800,
            z                   = -6000,
            y                   = -2800,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 72800,
            z                   = -6000,
            y                   = -3800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 67200,
            z                   = -6000,
            y                   = -2000,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 67200,
            z                   = -6000,
            y                   = -2000,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
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
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -5600,
            z                   = -2000,
            y                   = 30080,
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
        ScenaNpcData(
            x                   = 117910,
            z                   = -2020,
            y                   = -87790,
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

# id: 0x10003 offset: 0x23A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 36840,
            z           = -2000,
            y           = 16600,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0183,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 41480,
            z           = -6090,
            y           = 11430,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0189,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 83840,
            z           = -2000,
            y           = -19430,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0182,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 103150,
            z           = -6030,
            y           = -53480,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 73280,
            z           = -5940,
            y           = -40040,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 36840,
            z           = -2000,
            y           = 16600,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0327,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 41480,
            z           = -6090,
            y           = 11430,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x032D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 83840,
            z           = -2000,
            y           = -19430,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0326,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 103150,
            z           = -6030,
            y           = -53480,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0331,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 73280,
            z           = -5940,
            y           = -40040,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x032E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x352
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 72000,
            y           = -6000,
            z           = -12900,
            range       = 2000,
            dword_10    = 0x00000578,
            dword_14    = 0x00000000,
            dword_18    = 0x00010040,
            dword_1C    = 0x00000000,
        ),
    )

# id: 0x10005 offset: 0x372
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 79840,
            triggerZ            = -6030,
            triggerY            = -14200,
            triggerRange        = 1000,
            actorX              = 80360,
            actorZ              = -6040,
            actorY              = -13800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 112050,
            triggerZ            = -6010,
            triggerY            = -68270,
            triggerRange        = 1000,
            actorX              = 112550,
            actorZ              = -5940,
            actorY              = -68770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 66590,
            triggerZ            = -6050,
            triggerY            = -4800,
            triggerRange        = 1000,
            actorX              = 65960,
            actorZ              = -5100,
            actorY              = -4960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3DE
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x3DF
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -67000, -155000, 196647)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_409',
    )

    OP_B1('R2201_y')

    Jump('loc_412')

    def _loc_409(): pass

    label('loc_409')

    OP_B1('R2201_n')

    def _loc_412(): pass

    label('loc_412')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_43A',
    )

    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)

    Jump('loc_453')

    def _loc_43A(): pass

    label('loc_43A')

    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)

    def _loc_453(): pass

    label('loc_453')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 3, 0x4BB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_465',
    )

    OP_6F(0x0000, 0)

    Jump('loc_46C')

    def _loc_465(): pass

    label('loc_465')

    OP_6F(0x0000, 60)

    def _loc_46C(): pass

    label('loc_46C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 4, 0x4BC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47E',
    )

    OP_6F(0x0001, 0)

    Jump('loc_485')

    def _loc_47E(): pass

    label('loc_47E')

    OP_6F(0x0001, 60)

    def _loc_485(): pass

    label('loc_485')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 5, 0x4BD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_497',
    )

    OP_6F(0x0002, 0)

    Jump('loc_49E')

    def _loc_497(): pass

    label('loc_497')

    OP_6F(0x0002, 60)

    def _loc_49E(): pass

    label('loc_49E')

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x186A),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(456, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x4AE
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4C3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_4C3(): pass

    label('loc_4C3')

    Return()

# id: 0x0003 offset: 0x4C4
@scena.Code('func_03_4C4')
def func_03_4C4():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 3, 0x4BB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_53A',
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
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0097, 3, 0x4BB))

    Jump('loc_5B1')

    def _loc_53A(): pass

    label('loc_53A')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_5B1(): pass

    label('loc_5B1')

    Jump('loc_5EA')

    def _loc_5B4(): pass

    label('loc_5B4')

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
    WaitEffect(0x0F, 0x85)
    def _loc_5EA(): pass

    label('loc_5EA')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5F8
@scena.Code('func_04_5F8')
def func_04_5F8():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 4, 0x4BC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_66C',
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
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0097, 4, 0x4BC))

    Jump('loc_6DF')

    def _loc_66C(): pass

    label('loc_66C')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_6DF(): pass

    label('loc_6DF')

    Jump('loc_718')

    def _loc_6E2(): pass

    label('loc_6E2')

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
    WaitEffect(0x0F, 0x86)
    def _loc_718(): pass

    label('loc_718')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x726
@scena.Code('func_05_726')
def func_05_726():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 5, 0x4BD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 6, 0x4BE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_81E',
    )

    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 0)
    SetChrPos(0x000D, 65960, -3500, -4960, 320)
    ChrTurnDirection(0x000D, 0x0000, 0)

    @scena.Lambda('lambda_0775')
    def lambda_0775():
        ChrMoveTo(0x00FE, 65960, -5000, -4960, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0775)

    @scena.Lambda('lambda_0790')
    def lambda_0790():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0790)

    ClearChrFlags(0x000D, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7D3',
    )

    Battle(0x0000032C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_7E0')

    def _loc_7D3(): pass

    label('loc_7D3')

    Battle(0x00000188, 0x00000000, 0x00, 0x0000, 0xFF)

    def _loc_7E0(): pass

    label('loc_7E0')

    SetChrFlags(0x000D, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_7F9'),
        (0x00000002, 'loc_80B'),
        (0x00000001, 'loc_81B'),
        (-1, 'loc_81E'),
    )

    def _loc_7F9(): pass

    label('loc_7F9')

    SetScenaFlags(ScenaFlag(0x0097, 6, 0x4BE))
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_81E')

    def _loc_80B(): pass

    label('loc_80B')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_81B(): pass

    label('loc_81B')

    OP_B4(0x00)

    Return()

    def _loc_81E(): pass

    label('loc_81E')

    If(
        (
            (Expr.Eval, "AddItem(0x0143, 1)"),
            Expr.Return,
        ),
        'loc_876',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石护符',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0097, 5, 0x4BD))

    Jump('loc_8EF')

    def _loc_876(): pass

    label('loc_876')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '红耀石护符',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '红耀石护符',
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

    def _loc_8EF(): pass

    label('loc_8EF')

    Jump('loc_928')

    def _loc_8F2(): pass

    label('loc_8F2')

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
    WaitEffect(0x0F, 0x87)
    def _loc_928(): pass

    label('loc_928')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
