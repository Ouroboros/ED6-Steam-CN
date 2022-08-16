import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5700_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5700   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5700.x'
    header.mapIndex       = 1
    header.bgm            = 62
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
        ('ED6_DT29/CH12060._CH', 'ED6_DT29/CH12060P._CP'),
        ('ED6_DT29/CH12061._CH', 'ED6_DT29/CH12061P._CP'),
        ('ED6_DT29/CH12190._CH', 'ED6_DT29/CH12190P._CP'),
        ('ED6_DT29/CH12191._CH', 'ED6_DT29/CH12191P._CP'),
        ('ED6_DT29/CH12970._CH', 'ED6_DT29/CH12970P._CP'),
        ('ED6_DT29/CH12971._CH', 'ED6_DT29/CH12971P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '工业区域『法克特里亚』2',
            x                   = -1870,
            z                   = 4000,
            y                   = 70500,
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

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -1660,
            z           = 4000,
            y           = -82810,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0514,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -2200,
            z           = 4000,
            y           = -35950,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0515,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -2080,
            z           = 4000,
            y           = 6660,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0514,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -33090,
            z           = 4000,
            y           = -85830,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0515,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -63370,
            z           = 4000,
            y           = -95010,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0516,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -65340,
            z           = 4000,
            y           = -75570,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0516,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -23570,
            z           = 4000,
            y           = 39810,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0516,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -23470,
            z           = 4000,
            y           = -28170,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0516,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 54520,
            z           = 4000,
            y           = -15020,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0516,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 42010,
            z           = 4250,
            y           = 48860,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0516,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -35030,
            triggerZ            = 4000,
            triggerY            = 5960,
            triggerRange        = 5000,
            actorX              = -31230,
            actorZ              = 5500,
            actorY              = 5960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -72130,
            triggerZ            = 4000,
            triggerY            = -77200,
            triggerRange        = 1000,
            actorX              = -71520,
            actorZ              = 4000,
            actorY              = -77200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41290,
            triggerZ            = 4250,
            triggerY            = -37040,
            triggerRange        = 1000,
            actorX              = 41910,
            actorZ              = 4250,
            actorY              = -37040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 55710,
            triggerZ            = 4000,
            triggerY            = 72760,
            triggerRange        = 1000,
            actorX              = 55970,
            actorZ              = 4000,
            actorY              = 73340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2A2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2B3',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_05_673)

    Jump('loc_2D1')

    def _loc_2B3(): pass

    label('loc_2B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 4, 0x221C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D1',
    )

    MapSetFlags(0x10000000)
    Event(0, func_06_6E7)

    def _loc_2D1(): pass

    label('loc_2D1')

    Return()

# id: 0x0001 offset: 0x2D2
@scena.Code('func_01_2D2')
def func_01_2D2():
    OP_16(0x02, 4000, -117000, -145000, 2293876)
    PlaySE(455, 0x00, 0x64)
    OP_71(0x000A, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0464, 0, 0x2320)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_300',
    )

    OP_6F(0x0007, 0)

    Jump('loc_307')

    def _loc_300(): pass

    label('loc_300')

    OP_6F(0x0007, 60)

    def _loc_307(): pass

    label('loc_307')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0464, 1, 0x2321)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_319',
    )

    OP_6F(0x0008, 0)

    Jump('loc_320')

    def _loc_319(): pass

    label('loc_319')

    OP_6F(0x0008, 60)

    def _loc_320(): pass

    label('loc_320')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0464, 2, 0x2322)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_332',
    )

    OP_6F(0x0009, 0)

    Jump('loc_339')

    def _loc_332(): pass

    label('loc_332')

    OP_6F(0x0009, 60)

    def _loc_339(): pass

    label('loc_339')

    Return()

# id: 0x0002 offset: 0x33A
@scena.Code('func_02_33A')
def func_02_33A():
    UnlockAchievement(0x02, 0x01AF, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0464, 0, 0x2320)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_417',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ω巨无霸'], 1)"),
            Expr.Return,
        ),
        'loc_3AE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['Ω巨无霸']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0464, 0, 0x2320))

    Jump('loc_414')

    def _loc_3AE(): pass

    label('loc_3AE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['Ω巨无霸']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['Ω巨无霸']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_414(): pass

    label('loc_414')

    Jump('loc_448')

    def _loc_417(): pass

    label('loc_417')

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
    def _loc_448(): pass

    label('loc_448')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x456
@scena.Code('func_03_456')
def func_03_456():
    UnlockAchievement(0x02, 0x01B0, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0464, 1, 0x2321)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_533',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['幻耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_4CA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['幻耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0464, 1, 0x2321))

    Jump('loc_530')

    def _loc_4CA(): pass

    label('loc_4CA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['幻耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['幻耀珠']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_530(): pass

    label('loc_530')

    Jump('loc_564')

    def _loc_533(): pass

    label('loc_533')

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
    def _loc_564(): pass

    label('loc_564')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x572
@scena.Code('func_04_572')
def func_04_572():
    UnlockAchievement(0x02, 0x01B1, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0464, 2, 0x2322)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_647',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 30)
    OP_73(0x0009)
    OP_6F(0x0009, 30)
    AddSepith(0x00, 100)
    AddSepith(0x01, 100)
    AddSepith(0x02, 100)
    AddSepith(0x03, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0464, 2, 0x2322))

    Jump('loc_661')

    def _loc_647(): pass

    label('loc_647')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_661(): pass

    label('loc_661')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x673
@scena.Code('func_05_673')
def func_05_673():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(40820, 4350, -31840, 0)
    OP_67(0, 7210, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(339000, 0)
    OP_6E(890, 0)
    FadeIn(500, 0)
    OP_0D()
    Sleep(2000)

    PlaySE(124, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x6E7
@scena.Code('func_06_6E7')
def func_06_6E7():
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
        'loc_6FE',
    )

    Call(0, 0x000B)
    Call(0, 0x000C)

    def _loc_6FE(): pass

    label('loc_6FE')

    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-3530, 4350, -118640, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3730, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 0)
    OP_70(0x0000, 30)
    OP_73(0x0000)

    @scena.Lambda('lambda_0770')
    def lambda_0770():
        CameraMove(-2020, 4000, -124090, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0770)

    CreateThread(0x0101, 0x01, 0x00, func_07_10CB)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_08_110A)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_09_1150)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_0A_1196)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010400001V#1004F#6P这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400002V#1044F好宽阔的地方啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_11(0xAA, 0xC8, 0xFF, 0, 400000, 0)
    CameraMove(-2020, 4000, -124090, 0)
    OP_67(0, 12070, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(321000, 0)
    OP_6E(439, 0)

    @scena.Lambda('lambda_085E')
    def lambda_085E():
        CameraMove(50600, 4000, -6600, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_085E)

    @scena.Lambda('lambda_0876')
    def lambda_0876():
        OP_67(0, 8940, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0876)

    @scena.Lambda('lambda_088E')
    def lambda_088E():
        CameraSetDistance(12250, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_088E)

    @scena.Lambda('lambda_089E')
    def lambda_089E():
        OP_6C(338000, 12000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_089E)

    @scena.Lambda('lambda_08AE')
    def lambda_08AE():
        OP_6E(600, 12000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_08AE)

    OP_C8(0x0200, 0x0046, 'C_PLAC27._CH', 0x00, 0x0FA0)
    Sleep(2000)

    @scena.Lambda('lambda_08D8')
    def lambda_08D8():
        ChrWalkTo(0x00FE, 4990, 4000, -120440, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_08D8)

    Sleep(800)

    @scena.Lambda('lambda_08F8')
    def lambda_08F8():
        ChrWalkTo(0x00FE, 6220, 4000, -120530, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_08F8)

    Sleep(800)

    @scena.Lambda('lambda_0918')
    def lambda_0918():
        ChrWalkTo(0x00FE, 4920, 4000, -121730, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_0918)

    Sleep(800)

    @scena.Lambda('lambda_0938')
    def lambda_0938():
        ChrWalkTo(0x00FE, 6760, 4000, -122050, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_0938)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    OP_6F(0x0000, 0)
    OP_11(0xAA, 0xC8, 0xFF, 75000, 100000, 0)
    CameraMove(4980, 4000, -120120, 0)
    OP_67(0, 5900, -10000, 0)
    CameraSetDistance(3860, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetPos(0x0101, 6250, 4000, -120500, 0)
    ChrSetPos(0x0102, 4950, 4000, -120500, 0)
    ChrSetPos(0x00F8, 6250, 4000, -121800, 0)
    ChrSetPos(0x00F9, 4950, 4000, -121800, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A75',
    )

    ChrTalk(
        0x0102,
        (
            '#0020400003V#1044F#5P……放眼望去，\n',
            '到处都林立着巨大的建筑物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7F')

    def _loc_A75(): pass

    label('loc_A75')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ACE',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400004V#1064F#6P这真是，放眼望去\n',
            '到处都林立着巨大的建筑物啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7F')

    def _loc_ACE(): pass

    label('loc_ACE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B24',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400005V#023F#6P……放眼望去，\n',
            '到处都林立着巨大的建筑物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7F')

    def _loc_B24(): pass

    label('loc_B24')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B7A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400006V#052F#6P……放眼望去，\n',
            '到处都林立着巨大的建筑物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7F')

    def _loc_B7A(): pass

    label('loc_B7A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400007V#073F#6P……放眼望去，\n',
            '到处都林立着巨大的建筑物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7F')

    def _loc_BD0(): pass

    label('loc_BD0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C26',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400008V#033F#6P呵，放眼望去，\n',
            '到处都林立着巨大的建筑物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7F')

    def _loc_C26(): pass

    label('loc_C26')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C7F',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400009V#213F#6P这真是，放眼望去，\n',
            '到处都林立着巨大的建筑物呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C7F(): pass

    label('loc_C7F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD6',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400010V#1163F#6P道路也相当宽敞……\n',
            '究竟是个什么样的地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_CD6(): pass

    label('loc_CD6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D2A',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400011V#212F#6P道路也很宽阔……\n',
            '究竟是个什么样的地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_D2A(): pass

    label('loc_D2A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D80',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400012V#035F#6P嗯，道路也很宽阔，\n',
            '究竟是个什么样的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_D80(): pass

    label('loc_D80')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DD6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400013V#073F#6P道路也相当宽阔……\n',
            '究竟是个什么样的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_DD6(): pass

    label('loc_DD6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E2C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400014V#555F#6P道路也相当宽阔……\n',
            '究竟是个什么样的地方啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_E2C(): pass

    label('loc_E2C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E7D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400015V#022F#6P道路也很宽阔……\n',
            '究竟是个什么样的地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E7D(): pass

    label('loc_E7D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FAE',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400016V#560F#6P或许……\n',
            '这里是工业区域也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070400017V如果将大量的水想成是工业用水，\n',
            '感觉上就很吻合了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400018V#1040F#5P原来如此，说得过去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400019V#1016F#5P的确，作为居住区的话，\n',
            '气氛就不那么安定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400020V#1006F……好。\n',
            '马上开始探索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1091')

    def _loc_FAE(): pass

    label('loc_FAE')

    ChrTalk(
        0x0102,
        (
            '#0020400021V#1035F#5P……或许\n',
            '这里是工业区域也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400022V#1040F如果将大量的水想成是工业用水，\n',
            '不就说得过去了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400023V#1015F#5P原来如此，的确有这可能啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400020V#1006F……好。\n',
            '马上开始探索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1091(): pass

    label('loc_1091')

    SetScenaFlags(ScenaFlag(0x0443, 6, 0x221E))
    OP_28(0x009E, 0x04, 0x02)
    OP_28(0x009E, 0x04, 0x08)

    @scena.Lambda('lambda_10A4')
    def lambda_10A4():
        CameraSetDistance(4600, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10A4)

    @scena.Lambda('lambda_10B4')
    def lambda_10B4():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_10B4)

    OP_30(0x00)
    WaitForThreadExit(0x0101, 0x0001)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0007 offset: 0x10CB
@scena.Code('func_07_10CB')
def func_07_10CB():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -2120, 4350, -118450, 180)
    ChrWalkTo(0x00FE, -2110, 4000, -123080, 2000, 0x00)
    ChrWalkTo(0x00FE, -2050, 4000, -125260, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0x110A
@scena.Code('func_08_110A')
def func_08_110A():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -2120, 4350, -118450, 180)
    ChrWalkTo(0x00FE, -2110, 4000, -123080, 2000, 0x00)
    ChrWalkTo(0x00FE, -920, 4000, -124130, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0009 offset: 0x1150
@scena.Code('func_09_1150')
def func_09_1150():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -2120, 4350, -118450, 180)
    ChrWalkTo(0x00FE, -2110, 4000, -123080, 2000, 0x00)
    ChrWalkTo(0x00FE, -3100, 4000, -123910, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x000A offset: 0x1196
@scena.Code('func_0A_1196')
def func_0A_1196():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -2120, 4350, -118450, 180)
    ChrWalkTo(0x00FE, -2110, 4000, -123080, 2000, 0x00)

    Return()

# id: 0x000B offset: 0x11C1
@scena.Code('func_0B_11C1')
def func_0B_11C1():
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
        (0x00000000, 'loc_123B'),
        (0x00000001, 'loc_1241'),
        (-1, 'loc_1247'),
    )

    def _loc_123B(): pass

    label('loc_123B')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1247')

    def _loc_1241(): pass

    label('loc_1241')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1247')

    def _loc_1247(): pass

    label('loc_1247')

    Return()

# id: 0x000C offset: 0x1248
@scena.Code('func_0C_1248')
def func_0C_1248():
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

# id: 0x000D offset: 0x12DB
@scena.Code('func_0D_12DB')
def func_0D_12DB():
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
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
