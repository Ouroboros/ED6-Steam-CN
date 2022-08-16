import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5612_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5612   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5612.x'
    header.mapIndex       = 1
    header.bgm            = 61
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
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT29/CH12330._CH', 'ED6_DT29/CH12330P._CP'),
        ('ED6_DT29/CH12331._CH', 'ED6_DT29/CH12331P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12201._CH', 'ED6_DT29/CH12201P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 55620,
            z                   = 9000,
            y                   = 35600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 60070,
            z                   = 0,
            y                   = 33920,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x014D,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -22330,
            z           = 0,
            y           = 127860,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -13930,
            z           = 0,
            y           = -4390,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -840,
            z           = 0,
            y           = 6830,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -68950,
            z           = 0,
            y           = 155090,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 97120,
            z           = 0,
            y           = 86150,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1C6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 48040,
            y           = -1000,
            z           = 131420,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 36070,
            y           = -1000,
            z           = 131620,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000017,
        ),
    )

# id: 0x10004 offset: 0x206
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -69010,
            triggerZ            = 0,
            triggerY            = 148300,
            triggerRange        = 1000,
            actorX              = -69010,
            actorZ              = 0,
            actorY              = 148960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 55620,
            triggerZ            = 8000,
            triggerY            = 34900,
            triggerRange        = 1000,
            actorX              = 55620,
            actorZ              = 8000,
            actorY              = 35600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1700,
            triggerZ            = 0,
            triggerY            = -4650,
            triggerRange        = 1000,
            actorX              = -1040,
            actorZ              = 0,
            actorY              = -4650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -27290,
            triggerZ            = 0,
            triggerY            = 9990,
            triggerRange        = 1000,
            actorX              = -27990,
            actorZ              = 0,
            actorY              = 9990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -27290,
            triggerZ            = 0,
            triggerY            = 7570,
            triggerRange        = 1000,
            actorX              = -27950,
            actorZ              = 0,
            actorY              = 7570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -70540,
            triggerZ            = 0,
            triggerY            = 100850,
            triggerRange        = 800,
            actorX              = -70540,
            actorZ              = 1100,
            actorY              = 100850,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 37890,
            triggerZ            = 0,
            triggerY            = 131750,
            triggerRange        = 800,
            actorX              = 37890,
            actorZ              = 1100,
            actorY              = 131750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -8010,
            triggerZ            = 720,
            triggerY            = -2040,
            triggerRange        = 800,
            actorX              = -8010,
            actorZ              = 720,
            actorY              = -2040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -21970,
            triggerZ            = 20,
            triggerY            = -1650,
            triggerRange        = 800,
            actorX              = -21970,
            actorZ              = 20,
            actorY              = -1650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x34A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 2, 0x1C0A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37B',
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000007A, 'loc_366'),
        (0x0000007B, 'loc_36D'),
        (0x0000007C, 'loc_374'),
        (-1, 'loc_37B'),
    )

    def _loc_366(): pass

    label('loc_366')

    Event(0, func_0B_DD5)

    Jump('loc_37B')

    def _loc_36D(): pass

    label('loc_36D')

    Event(0, func_10_1624)

    Jump('loc_37B')

    def _loc_374(): pass

    label('loc_374')

    Event(0, func_11_1E36)

    Jump('loc_37B')

    def _loc_37B(): pass

    label('loc_37B')

    Return()

# id: 0x0001 offset: 0x37C
@scena.Code('func_01_37C')
def func_01_37C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 0, 0x1D20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38E',
    )

    OP_6F(0x0000, 0)

    Jump('loc_395')

    def _loc_38E(): pass

    label('loc_38E')

    OP_6F(0x0000, 60)

    def _loc_395(): pass

    label('loc_395')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 2, 0x1D22)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A7',
    )

    OP_6F(0x0001, 0)

    Jump('loc_3AE')

    def _loc_3A7(): pass

    label('loc_3A7')

    OP_6F(0x0001, 60)

    def _loc_3AE(): pass

    label('loc_3AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 4, 0x1D24)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C0',
    )

    OP_6F(0x0002, 0)

    Jump('loc_3C7')

    def _loc_3C0(): pass

    label('loc_3C0')

    OP_6F(0x0002, 60)

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 6, 0x1D26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D9',
    )

    OP_6F(0x0003, 0)

    Jump('loc_3E0')

    def _loc_3D9(): pass

    label('loc_3D9')

    OP_6F(0x0003, 60)

    def _loc_3E0(): pass

    label('loc_3E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 7, 0x1D27)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F2',
    )

    OP_6F(0x0004, 0)

    Jump('loc_3F9')

    def _loc_3F2(): pass

    label('loc_3F2')

    OP_6F(0x0004, 60)

    def _loc_3F9(): pass

    label('loc_3F9')

    OP_A1(0x0009, 0x0012)
    ChrSetFlags(0x0009, 0x0001)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x34,
        (
            (Expr.PushLong, 0xC350),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 0, 0x1C18)),
            Expr.Return,
        ),
        'loc_446',
    )

    OP_64(0x05, 0x0001)
    OP_10(0x0E, 0x01)
    OP_71(0x0008, 0x0010)

    Jump('loc_44E')

    def _loc_446(): pass

    label('loc_446')

    OP_10(0x08, 0x00)
    OP_72(0x0008, 0x0010)

    def _loc_44E(): pass

    label('loc_44E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 1, 0x1C19)),
            Expr.Return,
        ),
        'loc_464',
    )

    OP_64(0x06, 0x0001)
    OP_10(0x01, 0x01)
    OP_71(0x0010, 0x0010)

    Jump('loc_46C')

    def _loc_464(): pass

    label('loc_464')

    OP_10(0x01, 0x00)
    OP_72(0x0010, 0x0010)

    def _loc_46C(): pass

    label('loc_46C')

    Return()

# id: 0x0002 offset: 0x46D
@scena.Code('func_02_46D')
def func_02_46D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_482',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_46D')

    def _loc_482(): pass

    label('loc_482')

    Return()

# id: 0x0003 offset: 0x483
@scena.Code('func_03_483')
def func_03_483():
    UnlockAchievement(0x02, 0x01AB, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 0, 0x1D20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_535',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    OP_6F(0x0000, 30)
    AddSepith(0x04, 50)
    AddSepith(0x05, 50)
    AddSepith(0x06, 50)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x03A4, 0, 0x1D20))

    Jump('loc_54F')

    def _loc_535(): pass

    label('loc_535')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_54F(): pass

    label('loc_54F')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x561
@scena.Code('func_04_561')
def func_04_561():
    UnlockAchievement(0x02, 0x0208, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 2, 0x1D22)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 3, 0x1D23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_645',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_05B8')
    def lambda_05B8():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05B8)

    @scena.Lambda('lambda_05D3')
    def lambda_05D3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05D3)

    ChrClearFlags(0x0008, 0x0080)

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
    Battle(0x00000423, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_620'),
        (0x00000002, 'loc_632'),
        (0x00000001, 'loc_642'),
        (-1, 'loc_645'),
    )

    def _loc_620(): pass

    label('loc_620')

    SetScenaFlags(ScenaFlag(0x03A4, 3, 0x1D23))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_645')

    def _loc_632(): pass

    label('loc_632')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_642(): pass

    label('loc_642')

    OP_B4(0x00)

    Return()

    def _loc_645(): pass

    label('loc_645')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['攻击４'], 1)"),
            Expr.Return,
        ),
        'loc_694',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['攻击４']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A4, 2, 0x1D22))

    Jump('loc_6F6')

    def _loc_694(): pass

    label('loc_694')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['攻击４']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['攻击４']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_6F6(): pass

    label('loc_6F6')

    Jump('loc_728')

    def _loc_6F9(): pass

    label('loc_6F9')

    FadeOut(300, 0, 100)

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
    def _loc_728(): pass

    label('loc_728')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x736
@scena.Code('func_05_736')
def func_05_736():
    UnlockAchievement(0x02, 0x01AC, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 4, 0x1D24)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_813',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['导力服'], 1)"),
            Expr.Return,
        ),
        'loc_7AA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A4, 4, 0x1D24))

    Jump('loc_810')

    def _loc_7AA(): pass

    label('loc_7AA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['导力服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['导力服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_810(): pass

    label('loc_810')

    Jump('loc_844')

    def _loc_813(): pass

    label('loc_813')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_844(): pass

    label('loc_844')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x852
@scena.Code('func_06_852')
def func_06_852():
    UnlockAchievement(0x02, 0x01AD, 0x00)
    UnlockAchievement(0x02, 0x020D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 6, 0x1D26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_934',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_8CB',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A4, 6, 0x1D26))

    Jump('loc_931')

    def _loc_8CB(): pass

    label('loc_8CB')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_931(): pass

    label('loc_931')

    Jump('loc_965')

    def _loc_934(): pass

    label('loc_934')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_965(): pass

    label('loc_965')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x973
@scena.Code('func_07_973')
def func_07_973():
    UnlockAchievement(0x02, 0x01AE, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A4, 7, 0x1D27)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A50',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_9E7',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A4, 7, 0x1D27))

    Jump('loc_A4D')

    def _loc_9E7(): pass

    label('loc_9E7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_A4D(): pass

    label('loc_A4D')

    Jump('loc_A81')

    def _loc_A50(): pass

    label('loc_A50')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_A81(): pass

    label('loc_A81')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xA8F
@scena.Code('func_08_A8F')
def func_08_A8F():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Call(0, 0x000A)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B03',
    )

    PlaySE(157, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0008, 0)
    OP_70(0x0008, 30)
    OP_73(0x0011)
    OP_64(0x05, 0x0001)
    OP_10(0x0E, 0x01)
    SetScenaFlags(ScenaFlag(0x0383, 0, 0x1C18))

    Jump('loc_B27')

    def _loc_B03(): pass

    label('loc_B03')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_B27',
    )

    PlaySE(171, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_B27')

    def _loc_B27(): pass

    label('loc_B27')

    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xB2B
@scena.Code('func_09_B2B')
def func_09_B2B():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Call(0, 0x000A)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B9F',
    )

    PlaySE(157, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0010, 0)
    OP_70(0x0010, 30)
    OP_73(0x0010)
    OP_64(0x06, 0x0001)
    OP_10(0x01, 0x01)
    SetScenaFlags(ScenaFlag(0x0383, 1, 0x1C19))

    Jump('loc_BC3')

    def _loc_B9F(): pass

    label('loc_B9F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_BC3',
    )

    PlaySE(171, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_BC3')

    def _loc_BC3(): pass

    label('loc_BC3')

    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0xBC7
@scena.Code('func_0A_BC7')
def func_0A_BC7():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 1, 0x1C09)),
            Expr.Return,
        ),
        'loc_BE2',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_BE2(): pass

    label('loc_BE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 4, 0x1C0C)),
            Expr.Return,
        ),
        'loc_BF3',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_BF3(): pass

    label('loc_BF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 6, 0x1C0E)),
            Expr.Return,
        ),
        'loc_C04',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_C04(): pass

    label('loc_C04')

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_C30'),
        (0x00000001, 'loc_C3D'),
        (0x00000003, 'loc_C99'),
        (0x00000007, 'loc_D19'),
        (-1, 'loc_DBD'),
    )

    def _loc_C30(): pass

    label('loc_C30')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DBD')

    def _loc_C3D(): pass

    label('loc_C3D')

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【使用红色密码卡】\n'),
            TXT(0x01, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C7C'),
        (0x00000001, 'loc_C89'),
        (-1, 'loc_C96'),
    )

    def _loc_C7C(): pass

    label('loc_C7C')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C96')

    def _loc_C89(): pass

    label('loc_C89')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C96')

    def _loc_C96(): pass

    label('loc_C96')

    Jump('loc_DBD')

    def _loc_C99(): pass

    label('loc_C99')

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【使用红色密码卡】\n'),
            TXT(0x01, '【使用绿色密码卡】\n'),
            TXT(0x02, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_CEF'),
        (0x00000001, 'loc_CFC'),
        (0x00000002, 'loc_D09'),
        (-1, 'loc_D16'),
    )

    def _loc_CEF(): pass

    label('loc_CEF')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D16')

    def _loc_CFC(): pass

    label('loc_CFC')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D16')

    def _loc_D09(): pass

    label('loc_D09')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D16')

    def _loc_D16(): pass

    label('loc_D16')

    Jump('loc_DBD')

    def _loc_D19(): pass

    label('loc_D19')

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【使用红色密码卡】\n'),
            TXT(0x01, '【使用绿色密码卡】\n'),
            TXT(0x02, '【使用蓝色密码卡】\n'),
            TXT(0x03, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D86'),
        (0x00000001, 'loc_D93'),
        (0x00000002, 'loc_DA0'),
        (0x00000003, 'loc_DAD'),
        (-1, 'loc_DBA'),
    )

    def _loc_D86(): pass

    label('loc_D86')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DBA')

    def _loc_D93(): pass

    label('loc_D93')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DBA')

    def _loc_DA0(): pass

    label('loc_DA0')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DBA')

    def _loc_DAD(): pass

    label('loc_DAD')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DBA')

    def _loc_DBA(): pass

    label('loc_DBA')

    Jump('loc_DBD')

    def _loc_DBD(): pass

    label('loc_DBD')

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

    Return()

# id: 0x000B offset: 0xDD5
@scena.Code('func_0B_DD5')
def func_0B_DD5():
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
        'loc_DEC',
    )

    Call(0, 0x0012)
    Call(0, 0x0013)

    def _loc_DEC(): pass

    label('loc_DEC')

    ChrSetPos(0x0101, 67270, 0, 29420, 270)
    ChrSetPos(0x0109, 67270, 0, 28510, 270)
    ChrSetPos(0x00F8, 68260, 0, 28510, 270)
    ChrSetPos(0x00F9, 68260, 0, 29420, 270)
    CameraMove(67730, 0, 29250, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(80)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ED1',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_F0F')

    def _loc_ED1(): pass

    label('loc_ED1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EF8',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_F0F')

    def _loc_EF8(): pass

    label('loc_EF8')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_F0F(): pass

    label('loc_F0F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F36',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_F74')

    def _loc_F36(): pass

    label('loc_F36')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F5D',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_F74')

    def _loc_F5D(): pass

    label('loc_F5D')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_F74(): pass

    label('loc_F74')

    Sleep(1000)

    ChrSetDirection(0x0101, 315, 400)
    ChrSetDirection(0x0109, 315, 400)
    ChrSetDirection(0x00F8, 315, 400)
    ChrSetDirection(0x00F9, 315, 400)

    @scena.Lambda('lambda_0F9B')
    def lambda_0F9B():
        CameraMove(59860, 0, 35220, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F9B)

    @scena.Lambda('lambda_0FB3')
    def lambda_0FB3():
        OP_6C(333000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FB3)

    OP_6E(238, 4000)
    Sleep(1000)

    Fade(500)
    CameraMove(67730, 0, 29250, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321161V#1020F#6P那、那个时候的机械兽！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_104C')
    def lambda_104C():
        CameraMove(59730, 0, 33680, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_104C)

    @scena.Lambda('lambda_1064')
    def lambda_1064():
        OP_67(0, 8070, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1064)

    @scena.Lambda('lambda_107C')
    def lambda_107C():
        CameraSetDistance(2800, 4000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_107C)

    @scena.Lambda('lambda_108C')
    def lambda_108C():
        OP_6C(350000, 4000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_108C)

    @scena.Lambda('lambda_109C')
    def lambda_109C():
        OP_6E(302, 4000)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_109C)

    CreateThread(0x0109, 0x01, 0x00, func_0D_15D0)
    Sleep(100)

    CreateThread(0x00F8, 0x01, 0x00, func_0E_15EC)
    Sleep(400)

    CreateThread(0x0101, 0x01, 0x00, func_0C_15B4)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x00, func_0F_1608)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x0109, 0x0002)

    ChrTalk(
        0x0109,
        (
            '#0180321162V#1064F#6P啊～确实和王城地下\n',
            '是同样的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321163V#1026F#6P为、为什么\n',
            '这里会有那种东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321164V#1019F我是说，那种怪物\n',
            '怎么会有两台这么多！？',
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
        'loc_13F0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321165V#065F#6P不、不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070321166V不过这里好像是研究设施，\n',
            '可能进行了不少调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321167V#1015F#6P调查？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070321168V#561F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070321169V作为开发独创的人形兵器时\n',
            '参考之用等等的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12BA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321170V#057F#6P原来如此……有可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AF')

    def _loc_12BA(): pass

    label('loc_12BA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12FB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321171V#022F#6P原来如此……有可能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AF')

    def _loc_12FB(): pass

    label('loc_12FB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_133E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321172V#042F#6P这个可能性似乎很高呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AF')

    def _loc_133E(): pass

    label('loc_133E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1377',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321173V#072F#6P这很有可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AF')

    def _loc_1377(): pass

    label('loc_1377')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13AF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321174V#032F#6P唔……有可能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13AF(): pass

    label('loc_13AF')

    ChrTalk(
        0x0109,
        (
            '#0180321175V#1068F#6P看来这是超乎预料之外\n',
            '的危险设施啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A9')

    def _loc_13F0(): pass

    label('loc_13F0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_145F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321176V#035F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040321177V#032F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A9')

    def _loc_145F(): pass

    label('loc_145F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14CE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321178V#074F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080321179V#072F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A9')

    def _loc_14CE(): pass

    label('loc_14CE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_153D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321180V#047F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060321181V#042F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A9')

    def _loc_153D(): pass

    label('loc_153D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15A9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321182V#026F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030321183V#022F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A9(): pass

    label('loc_15A9')

    Sleep(200)

    SetScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x15B4
@scena.Code('func_0C_15B4')
def func_0C_15B4():
    ChrWalkTo(0x00FE, 61140, 20, 31110, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000D offset: 0x15D0
@scena.Code('func_0D_15D0')
def func_0D_15D0():
    ChrWalkTo(0x00FE, 59760, 20, 30970, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000E offset: 0x15EC
@scena.Code('func_0E_15EC')
def func_0E_15EC():
    ChrWalkTo(0x00FE, 59620, 20, 29780, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x1608
@scena.Code('func_0F_1608')
def func_0F_1608():
    ChrWalkTo(0x00FE, 61070, 20, 29810, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0010 offset: 0x1624
@scena.Code('func_10_1624')
def func_10_1624():
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
        'loc_163B',
    )

    Call(0, 0x0012)
    Call(0, 0x0013)

    def _loc_163B(): pass

    label('loc_163B')

    ChrSetPos(0x0101, 60570, 4000, 21850, 0)
    ChrSetPos(0x0109, 59450, 4000, 21810, 0)
    ChrSetPos(0x00F8, 59430, 4000, 20670, 0)
    ChrSetPos(0x00F9, 60900, 4000, 20660, 0)
    CameraMove(59880, 4000, 21450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(80)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1720',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_175E')

    def _loc_1720(): pass

    label('loc_1720')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1747',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_175E')

    def _loc_1747(): pass

    label('loc_1747')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_175E(): pass

    label('loc_175E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1785',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_17C3')

    def _loc_1785(): pass

    label('loc_1785')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17AC',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_17C3')

    def _loc_17AC(): pass

    label('loc_17AC')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_17C3(): pass

    label('loc_17C3')

    Sleep(1000)

    @scena.Lambda('lambda_17CE')
    def lambda_17CE():
        CameraMove(59860, 0, 35220, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_17CE)

    @scena.Lambda('lambda_17E6')
    def lambda_17E6():
        OP_6C(333000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_17E6)

    OP_6E(238, 4000)
    Sleep(1000)

    Fade(500)
    CameraMove(59880, 4000, 21450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010321161V#1020F#6P那、那个时候的机械兽！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_187F')
    def lambda_187F():
        CameraMove(59950, 4000, 27700, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_187F)

    @scena.Lambda('lambda_1897')
    def lambda_1897():
        OP_6C(327000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1897)

    @scena.Lambda('lambda_18A7')
    def lambda_18A7():
        OP_6E(283, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_18A7)

    @scena.Lambda('lambda_18B7')
    def lambda_18B7():
        OP_67(0, 7140, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_18B7)

    @scena.Lambda('lambda_18CF')
    def lambda_18CF():
        ChrWalkTo(0x00FE, 60430, 4000, 23410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18CF)

    Sleep(50)

    @scena.Lambda('lambda_18EF')
    def lambda_18EF():
        ChrWalkTo(0x00FE, 59610, 4000, 23410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_18EF)

    Sleep(100)

    @scena.Lambda('lambda_190F')
    def lambda_190F():
        ChrWalkTo(0x00FE, 58800, 4000, 22590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_190F)

    Sleep(60)

    @scena.Lambda('lambda_192F')
    def lambda_192F():
        ChrWalkTo(0x00FE, 61660, 4000, 22410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_192F)

    WaitForThreadExit(0x00F8, 0x0001)
    ChrSetDirection(0x00F8, 0, 400)
    WaitForThreadExit(0x00F9, 0x0001)
    ChrSetDirection(0x00F9, 0, 400)
    WaitForThreadExit(0x0109, 0x0002)

    ChrTalk(
        0x0109,
        (
            '#0180321162V#1064F#6P啊～确实和王城地下\n',
            '是同样的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321163V#1026F#6P为、为什么\n',
            '这里会有那种东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321164V#1019F我是说，那种怪物\n',
            '怎么会有两台这么多！？',
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
        'loc_1C72',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321165V#065F#6P不、不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070321166V不过这里好像是研究设施，\n',
            '可能进行了不少调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321167V#1015F#6P调查？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070321168V#561F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070321169V作为开发独创的人形兵器时\n',
            '参考之用等等的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B40',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321170V#057F#6P原来如此……有可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C35')

    def _loc_1B40(): pass

    label('loc_1B40')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B81',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321171V#022F#6P原来如此……有可能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C35')

    def _loc_1B81(): pass

    label('loc_1B81')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BC4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321172V#042F#6P这个可能性似乎很高呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C35')

    def _loc_1BC4(): pass

    label('loc_1BC4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BFD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321173V#072F#6P这很有可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C35')

    def _loc_1BFD(): pass

    label('loc_1BFD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C35',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321174V#032F#6P唔……有可能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C35(): pass

    label('loc_1C35')

    ChrTalk(
        0x0109,
        (
            '#0180321175V#1068F#6P看来这是超乎预想\n',
            '的危险设施啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E2B')

    def _loc_1C72(): pass

    label('loc_1C72')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CE1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321176V#035F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040321177V#032F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E2B')

    def _loc_1CE1(): pass

    label('loc_1CE1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D50',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321178V#074F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080321179V#072F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E2B')

    def _loc_1D50(): pass

    label('loc_1D50')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DBF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321180V#047F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060321181V#042F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E2B')

    def _loc_1DBF(): pass

    label('loc_1DBF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E2B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321182V#026F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030321183V#022F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E2B(): pass

    label('loc_1E2B')

    Sleep(200)

    SetScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x1E36
@scena.Code('func_11_1E36')
def func_11_1E36():
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
        'loc_1E4D',
    )

    Call(0, 0x0012)
    Call(0, 0x0013)

    def _loc_1E4D(): pass

    label('loc_1E4D')

    ChrSetPos(0x0101, 52920, 8000, 28620, 90)
    ChrSetPos(0x0109, 52800, 8000, 29590, 90)
    ChrSetPos(0x00F8, 51980, 8000, 28450, 90)
    ChrSetPos(0x00F9, 51750, 8000, 29450, 90)
    CameraMove(52120, 8000, 28960, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010321207V#1004F#5P啊……\n',
            '这里是楼梯井？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0101, 54380, 8000, 29400, 2000, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_1F3E')
    def lambda_1F3E():
        CameraMove(59860, 0, 35220, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F3E)

    @scena.Lambda('lambda_1F56')
    def lambda_1F56():
        OP_6C(333000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F56)

    OP_6E(238, 4000)
    Sleep(1000)

    Fade(500)
    CameraMove(52850, 8000, 29240, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010321161V#1020F#5P那、那个时候的机械兽！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FEF')
    def lambda_1FEF():
        CameraMove(60080, 8000, 30590, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FEF)

    @scena.Lambda('lambda_2007')
    def lambda_2007():
        OP_67(0, 8189, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2007)

    @scena.Lambda('lambda_201F')
    def lambda_201F():
        OP_6C(297000, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_201F)

    @scena.Lambda('lambda_202F')
    def lambda_202F():
        OP_6E(363, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_202F)

    @scena.Lambda('lambda_203F')
    def lambda_203F():
        CameraSetDistance(2710, 3000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_203F)

    @scena.Lambda('lambda_204F')
    def lambda_204F():
        ChrWalkTo(0x00FE, 54340, 8000, 30200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_204F)

    Sleep(50)

    @scena.Lambda('lambda_206F')
    def lambda_206F():
        ChrWalkTo(0x00FE, 54310, 8000, 30990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_206F)

    Sleep(50)

    @scena.Lambda('lambda_208F')
    def lambda_208F():
        ChrWalkTo(0x00FE, 54380, 8000, 28550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_208F)

    WaitForThreadExit(0x0109, 0x0001)

    @scena.Lambda('lambda_20AF')
    def lambda_20AF():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_20AF)

    WaitForThreadExit(0x00F8, 0x0001)

    @scena.Lambda('lambda_20C2')
    def lambda_20C2():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_20C2)

    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_20D5')
    def lambda_20D5():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_20D5)

    WaitForThreadExit(0x0109, 0x0002)

    ChrTalk(
        0x0109,
        (
            '#0180321209V#1064F#6P从这里\n',
            '有点看不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321210V不过确实和王城地下\n',
            '是同样的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321211V#1026F#6P为、为什么\n',
            '这里会有那种东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321164V#1019F我是说，那种怪物\n',
            '怎么会有两台这么多！？',
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
        'loc_241C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321213V#065F#6P不、不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070321166V不过这里好像是研究设施，\n',
            '可能进行了不少调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321215V#1015F#6P调查？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070321216V#561F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070321169V作为开发独创的人形兵器时\n',
            '参考之用等等的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22E6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321218V#057F#6P原来如此……有可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DB')

    def _loc_22E6(): pass

    label('loc_22E6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2327',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321219V#022F#6P原来如此……有可能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DB')

    def _loc_2327(): pass

    label('loc_2327')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_236A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321220V#042F#6P这个可能性似乎很高呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DB')

    def _loc_236A(): pass

    label('loc_236A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23A3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321221V#072F#6P这很有可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DB')

    def _loc_23A3(): pass

    label('loc_23A3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23DB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321222V#032F#6P唔……有可能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23DB(): pass

    label('loc_23DB')

    ChrTalk(
        0x0109,
        (
            '#0180321223V#1068F#6P看来这是超乎预料之外\n',
            '的危险设施啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D5')

    def _loc_241C(): pass

    label('loc_241C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_248B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321224V#035F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040321177V#032F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D5')

    def _loc_248B(): pass

    label('loc_248B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24FA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321226V#074F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080321179V#072F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D5')

    def _loc_24FA(): pass

    label('loc_24FA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2569',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321228V#047F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060321181V#042F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D5')

    def _loc_2569(): pass

    label('loc_2569')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25D5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321230V#026F#6P这就不清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030321183V#022F看来是超乎预料之外\n',
            '的危险设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25D5(): pass

    label('loc_25D5')

    Sleep(200)

    Fade(500)
    CameraMove(54380, 8000, 29400, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 54380, 8000, 29400, 90)
    ChrSetPos(0x0001, 54380, 8000, 29400, 90)
    ChrSetPos(0x0002, 54380, 8000, 29400, 90)
    ChrSetPos(0x0003, 54380, 8000, 29400, 90)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x2667
@scena.Code('func_12_2667')
def func_12_2667():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_26E4'),
        (0x00000001, 'loc_26EA'),
        (-1, 'loc_26F0'),
    )

    def _loc_26E4(): pass

    label('loc_26E4')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_26F0')

    def _loc_26EA(): pass

    label('loc_26EA')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_26F0')

    def _loc_26F0(): pass

    label('loc_26F0')

    Return()

# id: 0x0013 offset: 0x26F1
@scena.Code('func_13_26F1')
def func_13_26F1():
    MapClearFlags(0x00000001)
    CameraMove(64510, 0, -14780, 92)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['凯文神父'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0014 offset: 0x274E
@scena.Code('func_14_274E')
def func_14_274E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 0, 0x1C90)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 1, 0x1C91)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29EB',
    )

    EventBegin(0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有大型的『福音』。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010321271V#1004F咦……这不是\n',
            '新型福音吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(3000)
    ChrSetPos(0x0000, -7520, 20, -3140, 0)
    ChrSetPos(0x0001, -8620, 20, -3320, 0)
    ChrSetPos(0x0002, -9230, 20, -4070, 0)
    ChrSetPos(0x0003, -6590, 20, -3840, 0)

    @scena.Lambda('lambda_282D')
    def lambda_282D():
        CameraMove(-8010, 730, -510, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_282D)

    @scena.Lambda('lambda_2845')
    def lambda_2845():
        OP_6C(333000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2845)

    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2892',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321272V#042F看来没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2963')

    def _loc_2892(): pass

    label('loc_2892')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28C6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321273V#032F看来没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2963')

    def _loc_28C6(): pass

    label('loc_28C6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28FA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321274V#050F看来没错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2963')

    def _loc_28FA(): pass

    label('loc_28FA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2932',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321275V#062F嗯，看来没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2963')

    def _loc_2932(): pass

    label('loc_2932')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2963',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321276V#072F看来没错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2963(): pass

    label('loc_2963')

    ChrTalk(
        0x0101,
        (
            '#0010321277V#1015F……新型福音\n',
            '就是在这个设施制造出来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321278V#1063F没想到，『福音』\n',
            '竟然是在利贝尔制造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0392, 0, 0x1C90))
    EventEnd(0x00)

    Jump('loc_2C7D')

    def _loc_29EB(): pass

    label('loc_29EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 0, 0x1C90)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 1, 0x1C91)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C4F',
    )

    EventBegin(0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有大型的『福音』。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrSetDirection(0x0000, 0, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010321271V#1004F咦……这不是\n',
            '新型福音吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(3000)
    ChrSetPos(0x0000, -7520, 20, -3140, 0)
    ChrSetPos(0x0001, -8620, 20, -3320, 0)
    ChrSetPos(0x0002, -9230, 20, -4070, 0)
    ChrSetPos(0x0003, -6590, 20, -3840, 0)

    @scena.Lambda('lambda_2AD0')
    def lambda_2AD0():
        CameraMove(-8010, 730, -510, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AD0)

    @scena.Lambda('lambda_2AE8')
    def lambda_2AE8():
        OP_6C(333000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2AE8)

    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B35',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321272V#042F看来没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C06')

    def _loc_2B35(): pass

    label('loc_2B35')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B69',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321273V#032F看来没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C06')

    def _loc_2B69(): pass

    label('loc_2B69')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B9D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321274V#050F看来没错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C06')

    def _loc_2B9D(): pass

    label('loc_2B9D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BD5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321275V#062F嗯，看来没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C06')

    def _loc_2BD5(): pass

    label('loc_2BD5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C06',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321276V#072F看来没错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C06(): pass

    label('loc_2C06')

    ChrTalk(
        0x0101,
        (
            '#0010321277V#1015F……新型福音\n',
            '就是在这个设施制造出来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0392, 0, 0x1C90))
    EventEnd(0x00)

    Jump('loc_2C7D')

    def _loc_2C4F(): pass

    label('loc_2C4F')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有大型的福音。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_2C7D(): pass

    label('loc_2C7D')

    Return()

# id: 0x0015 offset: 0x2C7E
@scena.Code('func_15_2C7E')
def func_15_2C7E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 0, 0x1C90)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 1, 0x1C91)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FB4',
    )

    EventBegin(0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有制作成『桩』的形状的装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010321279V#1004F咦……这个难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(3000)
    ChrSetPos(0x0000, -21420, 20, -3140, 0)
    ChrSetPos(0x0001, -22470, 20, -3320, 0)
    ChrSetPos(0x0002, -23030, 20, -4070, 0)
    ChrSetPos(0x0003, -20590, 20, -3840, 0)

    @scena.Lambda('lambda_2D62')
    def lambda_2D62():
        CameraMove(-21890, 1010, -480, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D62)

    @scena.Lambda('lambda_2D7A')
    def lambda_2D7A():
        OP_6C(333000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2D7A)

    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DE6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321280V#072F嗯，看来和瓦鲁特使用的\n',
            '『桩』是一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F39')

    def _loc_2DE6(): pass

    label('loc_2DE6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E3F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321281V#062F嗯，似乎和在蔡斯扰乱\n',
            '七耀脉的『桩』是同样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F39')

    def _loc_2E3F(): pass

    label('loc_2E3F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E92',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321282V#022F这好像和『瘦狼』使用的\n',
            '『桩』是一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F39')

    def _loc_2E92(): pass

    label('loc_2E92')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EE5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321283V#050F这好像和『瘦狼』使用的\n',
            '『桩』是一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F39')

    def _loc_2EE5(): pass

    label('loc_2EE5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F39',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321284V#032F唔，看来和在蔡斯引起地震的\n',
            '『桩』是一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F39(): pass

    label('loc_2F39')

    ChrTalk(
        0x0101,
        (
            '#0010321285V#1015F……那个装置是这里制造的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321286V#1063F没想到，这种东西\n',
            '竟然是在利贝尔制造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0392, 1, 0x1C91))
    EventEnd(0x00)

    Jump('loc_32EC')

    def _loc_2FB4(): pass

    label('loc_2FB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 0, 0x1C90)),
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 1, 0x1C91)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32B0',
    )

    EventBegin(0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有制作成『桩』的形状的装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010321279V#1004F咦……这个难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(3000)
    ChrSetPos(0x0000, -21420, 20, -3140, 0)
    ChrSetPos(0x0001, -22470, 20, -3320, 0)
    ChrSetPos(0x0002, -23030, 20, -4070, 0)
    ChrSetPos(0x0003, -20590, 20, -3840, 0)

    @scena.Lambda('lambda_3097')
    def lambda_3097():
        CameraMove(-21890, 1010, -480, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3097)

    @scena.Lambda('lambda_30AF')
    def lambda_30AF():
        OP_6C(333000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_30AF)

    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_311B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321280V#072F唔，看来和瓦鲁特使用的\n',
            '『桩』是一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_326E')

    def _loc_311B(): pass

    label('loc_311B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3174',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321281V#062F嗯，似乎和在蔡斯扰乱\n',
            '七耀脉的『桩』是同样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_326E')

    def _loc_3174(): pass

    label('loc_3174')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31C7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321282V#022F这好像和『瘦狼』使用的\n',
            '『桩』是一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_326E')

    def _loc_31C7(): pass

    label('loc_31C7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_321A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321283V#050F这好像和『瘦狼』使用的\n',
            '『桩』是一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_326E')

    def _loc_321A(): pass

    label('loc_321A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_326E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321284V#032F唔，看来和在蔡斯引起地震的\n',
            '『桩』是一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_326E(): pass

    label('loc_326E')

    ChrTalk(
        0x0101,
        (
            '#0010321285V#1015F……连那个装置都是在这里制造的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0392, 1, 0x1C91))
    EventEnd(0x00)

    Jump('loc_32EC')

    def _loc_32B0(): pass

    label('loc_32B0')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有制作成『桩』的形状的装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_32EC(): pass

    label('loc_32EC')

    Return()

# id: 0x0016 offset: 0x32ED
@scena.Code('func_16_32ED')
def func_16_32ED():
    ClearScenaFlags(ScenaFlag(0x0393, 2, 0x1C9A))
    ClearScenaFlags(ScenaFlag(0x0393, 3, 0x1C9B))
    ClearScenaFlags(ScenaFlag(0x0393, 4, 0x1C9C))
    SetScenaFlags(ScenaFlag(0x0393, 5, 0x1C9D))
    ClearScenaFlags(ScenaFlag(0x0393, 6, 0x1C9E))
    ClearScenaFlags(ScenaFlag(0x0393, 7, 0x1C9F))

    Return()

# id: 0x0017 offset: 0x3300
@scena.Code('func_17_3300')
def func_17_3300():
    ClearScenaFlags(ScenaFlag(0x0393, 2, 0x1C9A))
    ClearScenaFlags(ScenaFlag(0x0393, 3, 0x1C9B))
    ClearScenaFlags(ScenaFlag(0x0393, 4, 0x1C9C))
    ClearScenaFlags(ScenaFlag(0x0393, 5, 0x1C9D))
    SetScenaFlags(ScenaFlag(0x0393, 6, 0x1C9E))
    ClearScenaFlags(ScenaFlag(0x0393, 7, 0x1C9F))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
