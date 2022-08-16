import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5701_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5701   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5701.x'
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
            name                = '工业区域『法克特里亚』１',
            x                   = 8150,
            z                   = 4000,
            y                   = -23500,
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
            name                = '工业区域『法克特里亚』３',
            x                   = 70670,
            z                   = 4000,
            y                   = 9930,
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

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 8000,
            z           = 4000,
            y           = 17890,
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
            x           = -50130,
            z           = 4000,
            y           = 8970,
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
            x           = -78880,
            z           = 4000,
            y           = 9720,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0515,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x16E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -50000,
            y           = 4650,
            z           = -30000,
            range       = 2000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x18E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -107940,
            triggerZ            = 4350,
            triggerY            = 7670,
            triggerRange        = 1000,
            actorX              = -107540,
            actorZ              = 5350,
            actorY              = 7670,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1B2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1C8',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_03_242)

    Jump('loc_1D6')

    def _loc_1C8(): pass

    label('loc_1C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_1D6',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_05_448)

    def _loc_1D6(): pass

    label('loc_1D6')

    Return()

# id: 0x0001 offset: 0x1D7
@scena.Code('func_01_1D7')
def func_01_1D7():
    OP_16(0x02, 4000, -149000, -118000, 2293877)
    PlaySE(455, 0x00, 0x64)
    OP_10(0x03, 0x00)
    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 6, 0x222E)),
            Expr.Return,
        ),
        'loc_20B',
    )

    OP_71(0x0000, 0x0010)
    OP_71(0x0002, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_20B(): pass

    label('loc_20B')

    Return()

# id: 0x0002 offset: 0x20C
@scena.Code('func_02_20C')
def func_02_20C():
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

# id: 0x0003 offset: 0x242
@scena.Code('func_03_242')
def func_03_242():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-49940, 6000, -29920, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_02A4')
    def lambda_02A4():
        CameraMove(-107940, 4350, 6860, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02A4)

    OP_6C(315000, 7000)
    Fade(500)
    CameraMove(-109590, 4350, 9620, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3130, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    PlaySE(170, 0x00, 0x64)
    OP_71(0x0002, 0x0004)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C6002._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x32E
@scena.Code('func_04_32E')
def func_04_32E():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-49850, 6000, -29900, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_89(0x0101, -50000, 6000, -29000, 0)
    OP_89(0x0102, -51000, 6000, -30000, 0)
    OP_89(0x00F8, -49000, 6000, -30000, 0)
    OP_89(0x00F9, -50000, 6000, -31000, 0)
    OP_0D()
    Sleep(100)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 600)
    OP_12(0x00007530, 0x0006DDD0, 0x00001F40)

    @scena.Lambda('lambda_03E7')
    def lambda_03E7():
        CameraMove(-49850, 55000, -29900, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03E7)

    @scena.Lambda('lambda_03FF')
    def lambda_03FF():
        OP_67(0, 10590, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03FF)

    @scena.Lambda('lambda_0417')
    def lambda_0417():
        OP_6C(30000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0417)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C6002._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x448
@scena.Code('func_05_448')
def func_05_448():
    EventBegin(0x00)
    CameraMove(-49850, 60000, -29900, 0)
    OP_67(0, 10590, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(30000, 0)
    OP_6E(262, 0)
    OP_11(0x92, 0xBE, 0xD2, 30000, 450000, 0)
    OP_6F(0x0001, 600)
    Yield()
    OP_89(0x0101, -50000, 80000, -29000, 0)
    OP_89(0x0102, -51000, 80000, -30000, 0)
    OP_89(0x00F8, -49000, 80000, -30000, 0)
    OP_89(0x00F9, -50000, 80000, -31000, 0)
    PlaySE(235, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_12(0x00007530, 0x000493E0, 0x00002328)

    @scena.Lambda('lambda_0504')
    def lambda_0504():
        CameraMove(-49850, 6000, -29900, 10500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0504)

    @scena.Lambda('lambda_051C')
    def lambda_051C():
        OP_67(0, 6500, -10000, 10500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_051C)

    @scena.Lambda('lambda_0534')
    def lambda_0534():
        OP_6C(45000, 10500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0534)

    OP_70(0x0001, 0)
    OP_73(0x0001)
    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(200)

    Fade(500)
    CameraMove(-49850, 6000, -28020, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -49850, 6000, -28020, 0)
    ChrSetPos(0x0001, -49850, 6000, -28020, 0)
    ChrSetPos(0x0002, -49850, 6000, -28020, 0)
    ChrSetPos(0x0003, -49850, 6000, -28020, 0)
    OP_0D()
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
