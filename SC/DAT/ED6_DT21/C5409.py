import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5409_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5409   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5409.x'
    header.mapIndex       = 1
    header.bgm            = 28
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
        ('ED6_DT29/CH12390._CH', 'ED6_DT29/CH12390P._CP'),
        ('ED6_DT29/CH12391._CH', 'ED6_DT29/CH12391P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = 'Pale Apache',
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
            name                = 'Pale Apache',
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
            name                = 'Pale Apache',
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
    )

# id: 0x10002 offset: 0x132
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x132
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -8100,
            y           = 0,
            z           = -54880,
            range       = 9750,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF3170,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
    )

# id: 0x10004 offset: 0x152
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x152
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x153
@scena.Code('func_01_153')
def func_01_153():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_171',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_171(): pass

    label('loc_171')

    PlaySE(305, 0x01, 0x3C)
    PlaySE(451, 0x01, 0x64)

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

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x1AF
@scena.Code('func_02_1AF')
def func_02_1AF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 3, 0x2223)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 4, 0x2224)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1BC',
    )

    Return()

    def _loc_1BC(): pass

    label('loc_1BC')

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
        'loc_1E1',
    )

    Call(0, 0x0008)
    Call(0, 0x0009)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_1E1(): pass

    label('loc_1E1')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_206'),
        (0x00000003, 'loc_213'),
        (0x00000004, 'loc_220'),
        (0x00000005, 'loc_22D'),
        (0x00000006, 'loc_23A'),
        (0x00000007, 'loc_247'),
        (0x00000008, 'loc_254'),
        (-1, 'loc_261'),
    )

    def _loc_206(): pass

    label('loc_206')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 5)

    Jump('loc_261')

    def _loc_213(): pass

    label('loc_213')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 5)

    Jump('loc_261')

    def _loc_220(): pass

    label('loc_220')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 5)

    Jump('loc_261')

    def _loc_22D(): pass

    label('loc_22D')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 5)

    Jump('loc_261')

    def _loc_23A(): pass

    label('loc_23A')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 5)

    Jump('loc_261')

    def _loc_247(): pass

    label('loc_247')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 5)

    Jump('loc_261')

    def _loc_254(): pass

    label('loc_254')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 5)

    Jump('loc_261')

    def _loc_261(): pass

    label('loc_261')

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    CameraMove(1900, 0, -54180, 0)
    OP_67(0, 6340, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(321, 0)
    ChrSetPos(0x0101, 550, 0, -54530, 0)
    ChrSetPos(0x0102, 1790, 0, -54700, 0)
    ChrSetPos(0x010B, 200, 0, -55930, 0)
    ChrSetPos(0x00F9, 1610, 0, -56100, 0)
    OP_0D()
    PlaySE(119, 0x00, 0x64)
    PlaySE(309, 0x01, 0x32)
    Sleep(100)

    OP_24(0x0135, 0x3C)
    Sleep(100)

    OP_24(0x0135, 0x46)
    Sleep(100)

    OP_24(0x0135, 0x50)
    Sleep(100)

    OP_24(0x0135, 0x5A)
    Sleep(100)

    OP_24(0x0135, 0x64)
    Sleep(300)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_03A8')
    def lambda_03A8():
        CameraMove(3330, 0, -53050, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_03A8)

    @scena.Lambda('lambda_03C0')
    def lambda_03C0():
        OP_67(0, 5530, -10000, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03C0)

    @scena.Lambda('lambda_03D8')
    def lambda_03D8():
        CameraSetDistance(4500, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03D8)

    ChrSetPos(0x0008, -11850, 3000, -61530, 180)
    ChrSetPos(0x0009, 11620, 3000, -62560, 180)
    ChrSetPos(0x000A, 2009, 3000, -43000, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, func_03_595)
    CreateThread(0x0009, 0x00, 0x00, func_04_5C5)
    CreateThread(0x000A, 0x00, 0x00, func_05_5F5)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0102, 3)
    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    @scena.Lambda('lambda_0467')
    def lambda_0467():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0000, lambda_0467)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x010B, 4)
    ChrSetSubChip(0x010B, 0)
    Sleep(100)

    @scena.Lambda('lambda_0489')
    def lambda_0489():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_0489)

    ChrSetChipByIndex(0x00F9, 5)
    ChrSetSubChip(0x00F9, 0)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    @scena.Lambda('lambda_04BA')
    def lambda_04BA():
        CameraMove(2280, 0, -53910, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04BA)

    @scena.Lambda('lambda_04D2')
    def lambda_04D2():
        OP_67(0, 6120, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_04D2)

    @scena.Lambda('lambda_04EA')
    def lambda_04EA():
        CameraSetDistance(3100, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_04EA)

    @scena.Lambda('lambda_04FA')
    def lambda_04FA():
        ChrWalkTo(0x00FE, 1180, 1500, -57770, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_04FA)

    Sleep(50)

    @scena.Lambda('lambda_051A')
    def lambda_051A():
        ChrWalkTo(0x00FE, 40, 1500, -54080, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_051A)

    Sleep(20)

    @scena.Lambda('lambda_053A')
    def lambda_053A():
        ChrWalkTo(0x00FE, 3120, 1500, -52910, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_053A)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    Battle(0x00000433, 0x00000000, 0x01, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_581'),
        (0x00000000, 'loc_586'),
        (0x00000002, 'loc_58D'),
        (-1, 'loc_594'),
    )

    def _loc_581(): pass

    label('loc_581')

    OP_B4(0x00)

    Jump('loc_594')

    def _loc_586(): pass

    label('loc_586')

    Call(0, 0x0006)

    Jump('loc_594')

    def _loc_58D(): pass

    label('loc_58D')

    Call(0, 0x0007)

    Jump('loc_594')

    def _loc_594(): pass

    label('loc_594')

    Return()

# id: 0x0003 offset: 0x595
@scena.Code('func_03_595')
def func_03_595():
    OP_97(0x00FE, -3180, -57000, 175000, 8000, 0x0001)
    ChrSetDirection(0x00FE, 225, 200)

    @scena.Lambda('lambda_05B7')
    def lambda_05B7():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_05B7')

    DispatchAsync2(0x00FE, 0x0001, lambda_05B7)

    Return()

# id: 0x0004 offset: 0x5C5
@scena.Code('func_04_5C5')
def func_04_5C5():
    OP_97(0x00FE, 4050, -56500, 170000, 8000, 0x0001)
    ChrSetDirection(0x00FE, 135, 200)

    @scena.Lambda('lambda_05E7')
    def lambda_05E7():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_05E7')

    DispatchAsync2(0x00FE, 0x0001, lambda_05E7)

    Return()

# id: 0x0005 offset: 0x5F5
@scena.Code('func_05_5F5')
def func_05_5F5():
    OP_97(0x00FE, 1450, -53500, 185000, 8000, 0x0001)
    ChrSetDirection(0x00FE, 0, 200)

    @scena.Lambda('lambda_0617')
    def lambda_0617():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_0617')

    DispatchAsync2(0x00FE, 0x0001, lambda_0617)

    Return()

# id: 0x0006 offset: 0x625
@scena.Code('func_06_625')
def func_06_625():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    CameraMove(1110, 0, -55250, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 1110, 0, -55250, 0)
    ChrSetPos(0x0001, 1110, 0, -55250, 0)
    ChrSetPos(0x0002, 1110, 0, -55250, 0)
    ChrSetPos(0x0003, 1110, 0, -55250, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x010B, 65535)
    ChrSetSubChip(0x010B, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    SetScenaFlags(ScenaFlag(0x0444, 4, 0x2224))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x709
@scena.Code('func_07_709')
def func_07_709():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    CameraMove(1110, 0, -57250, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 1110, 0, -57250, 180)
    ChrSetPos(0x0001, 1110, 0, -57250, 180)
    ChrSetPos(0x0002, 1110, 0, -57250, 180)
    ChrSetPos(0x0003, 1110, 0, -57250, 180)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x010B, 65535)
    ChrSetSubChip(0x010B, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x7EA
@scena.Code('func_08_7EA')
def func_08_7EA():
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
        (0x00000000, 'loc_864'),
        (0x00000001, 'loc_86A'),
        (-1, 'loc_870'),
    )

    def _loc_864(): pass

    label('loc_864')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_870')

    def _loc_86A(): pass

    label('loc_86A')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_870')

    def _loc_870(): pass

    label('loc_870')

    Return()

# id: 0x0009 offset: 0x871
@scena.Code('func_09_871')
def func_09_871():
    FadeOut(0, 0, -1)
    CameraMove(-107890, 0, -346700, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            ChrTable['乔丝特'],
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
