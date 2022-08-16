import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1600_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1600   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1600.x'
    header.mapIndex       = 60
    header.bgm            = 125
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
        ('ED6_DT29/CH12450._CH', 'ED6_DT29/CH12450P._CP'),
        ('ED6_DT29/CH12451._CH', 'ED6_DT29/CH12451P._CP'),
        ('ED6_DT09/CH10840._CH', 'ED6_DT09/CH10840P._CP'),
        ('ED6_DT09/CH10841._CH', 'ED6_DT09/CH10841P._CP'),
        ('ED6_DT29/CH12460._CH', 'ED6_DT29/CH12460P._CP'),
        ('ED6_DT29/CH12461._CH', 'ED6_DT29/CH12461P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10551._CH', 'ED6_DT09/CH10551P._CP'),
        ('ED6_DT29/CH12500._CH', 'ED6_DT29/CH12500P._CP'),
        ('ED6_DT29/CH12501._CH', 'ED6_DT29/CH12501P._CP'),
        ('ED6_DT29/CH12560._CH', 'ED6_DT29/CH12560P._CP'),
        ('ED6_DT29/CH12561._CH', 'ED6_DT29/CH12561P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT27/CH03550._CH', 'ED6_DT27/CH03550P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = 'Silver-Haired Youth',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = 'Weissmann',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -5230,
            z           = 4000,
            y           = -12590,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 28010,
            z           = 6000,
            y           = -9400,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 21830,
            z           = 6560,
            y           = -1430,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -35520,
            z           = 16000,
            y           = 14970,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 8390,
            z           = 16000,
            y           = -3360,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 25620,
            z           = 22000,
            y           = 15270,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x202
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x202
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x202
@scena.Code('Init')
def Init():
    OP_11(0xFF, 0xFF, 0xFF, 45000, 70000, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_233',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    OP_B5(0x00)
    Event(0, func_02_286)

    Jump('loc_268')

    def _loc_233(): pass

    label('loc_233')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_249',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_06_43B)

    Jump('loc_268')

    def _loc_249(): pass

    label('loc_249')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_255'),
        (-1, 'loc_268'),
    )

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 0, 0x1A28)),
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 1, 0x1A29)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_265',
    )

    Event(0, func_05_42C)

    def _loc_265(): pass

    label('loc_265')

    Jump('loc_268')

    def _loc_268(): pass

    label('loc_268')

    Return()

# id: 0x0001 offset: 0x269
@scena.Code('func_01_269')
def func_01_269():
    OP_C4(0x00, 0x00000004)

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xBF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xBF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x286
@scena.Code('func_02_286')
def func_02_286():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-860, 4000, -2200, 0)
    OP_67(0, 11370, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(10000, 0)
    OP_6E(545, 0)
    MapSetFlags(0x00000010)
    OP_11(0xC8, 0xC8, 0xC8, 30000, 45000, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_02FE')
    def lambda_02FE():
        CameraMove(-4920, 22000, 20420, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02FE)

    @scena.Lambda('lambda_0316')
    def lambda_0316():
        OP_6C(0, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0316)

    @scena.Lambda('lambda_0326')
    def lambda_0326():
        OP_67(0, 7350, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0326)

    Sleep(2000)

    CreateThread(0x0009, 0x00, 0x00, func_03_398)
    Sleep(500)

    CreateThread(0x0008, 0x00, 0x00, func_04_3E2)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_035B')
    def lambda_035B():
        CameraSetDistance(3800, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_035B)

    @scena.Lambda('lambda_036B')
    def lambda_036B():
        OP_6E(262, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_036B)

    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C1603._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x398
@scena.Code('func_03_398')
def func_03_398():
    ChrSetPos(0x00FE, -920, 22000, 11580, 315)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -5500, 22000, 14020, 2000, 0x00)
    ChrWalkTo(0x00FE, -5500, 22000, 23500, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

    Return()

# id: 0x0004 offset: 0x3E2
@scena.Code('func_04_3E2')
def func_04_3E2():
    ChrSetPos(0x00FE, 640, 22000, 11430, 315)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -4040, 22000, 13830, 2000, 0x00)
    ChrWalkTo(0x00FE, -4310, 22000, 23500, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

    Return()

# id: 0x0005 offset: 0x42C
@scena.Code('func_05_42C')
def func_05_42C():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x43B
@scena.Code('func_06_43B')
def func_06_43B():
    EventBegin(0x00)
    CameraMove(-5920, 10000, 180, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -5920, 10000, 180, 180)
    ChrSetPos(0x0106, -5920, 10000, 180, 180)
    ChrSetPos(0x0107, -5920, 10000, 180, 180)
    ChrSetPos(0x00F9, -5920, 10000, 180, 180)
    FadeIn(1000, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0345, 1, 0x1A29))
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
