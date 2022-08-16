import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0810_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0810_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0810.x'
    header.mapIndex       = 1
    header.bgm            = 1
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/E0810._SN', 'ED6_DT21/E0810_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    MapClearFlags(0x00000010)
    CameraMove(-153630, 3450, -35320, 0)
    OP_67(0, -2990, -10000, 0)
    CameraSetDistance(3800, 0)
    OP_6C(0, 0)
    OP_6E(542, 0)
    OP_72(0x0000, 0x0004)
    OP_A1(0x000D, 0x0000)
    ChrSetPos(0x000D, -158650, -10000, -35510, 0)
    OP_B0(0x0000, 0x14)
    ChrSetPos(0x0008, -158650, -5000, -35510, 90)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 1)
    ChrClearFlags(0x0008, 0x0080)
    OP_CF(0x0008, 0x00, 'Frame143_back_Null1')

    @scena.Lambda('lambda_015E')
    def lambda_015E():
        ChrMoveToRelative(0x00FE, 0, 40000, 100000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_015E)

    CreateThread(0x000D, 0x02, 0x01, 0x0001)
    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_018A')
    def lambda_018A():
        OP_67(0, -4360, -10000, 13000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_018A)

    @scena.Lambda('lambda_01A2')
    def lambda_01A2():
        CameraSetDistance(5920, 13000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_01A2)

    Sleep(2000)

    @scena.Lambda('lambda_01B7')
    def lambda_01B7():
        ChrMoveToRelative(0x00FE, 0, 40000, 100000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_01B7)

    SetMessageWindowPos(250, 240, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0051860002V#1P#3S可恶～～～！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    Sleep(2000)

    @scena.Lambda('lambda_021F')
    def lambda_021F():
        ChrMoveToRelative(0x00FE, 0, 40000, 100000, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_021F)

    OP_56(0x00)
    MapSetFlags(0x02000000)
    FadeOut(3000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x00000010)
    TerminateThread(0x000D, 0x02)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/T1103._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0001 offset: 0x25D
@scena.Code('func_01_25D')
def func_01_25D():
    Sleep(1000)

    PlaySE(288, 0x00, 0x64)
    Sleep(1000)

    PlaySE(288, 0x00, 0x5A)
    Sleep(1000)

    PlaySE(288, 0x00, 0x50)
    Sleep(1000)

    PlaySE(288, 0x00, 0x46)
    Sleep(1000)

    PlaySE(288, 0x00, 0x3C)
    Sleep(1000)

    PlaySE(288, 0x00, 0x32)
    Sleep(1000)

    PlaySE(288, 0x00, 0x28)
    Sleep(1000)

    PlaySE(288, 0x00, 0x1E)
    Sleep(1000)

    PlaySE(288, 0x00, 0x14)
    Sleep(1000)

    PlaySE(288, 0x00, 0x0A)

    Return()

# id: 0x0002 offset: 0x2C2
@scena.Code('func_02_2C2')
def func_02_2C2():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    MapClearFlags(0x00000010)
    CameraMove(-153630, 3450, -35320, 0)
    OP_67(0, -2990, -10000, 0)
    CameraSetDistance(3800, 0)
    OP_6C(0, 0)
    OP_6E(542, 0)
    OP_72(0x0000, 0x0004)
    OP_A1(0x000D, 0x0000)
    ChrSetPos(0x000D, -158650, -10000, -35510, 0)
    OP_B0(0x0000, 0x14)
    ChrSetPos(0x0008, -158650, -5000, -35510, 90)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 1)
    ChrClearFlags(0x0008, 0x0080)
    OP_CF(0x0008, 0x00, 'Frame143_back_Null1')
    CreateThread(0x000D, 0x02, 0x01, 0x0001)

    @scena.Lambda('lambda_037F')
    def lambda_037F():
        ChrMoveToRelative(0x00FE, 0, 40000, 100000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_037F)

    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_03A4')
    def lambda_03A4():
        OP_67(0, -4360, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_03A4)

    @scena.Lambda('lambda_03BC')
    def lambda_03BC():
        CameraSetDistance(5920, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_03BC)

    Sleep(2000)

    @scena.Lambda('lambda_03D1')
    def lambda_03D1():
        ChrMoveToRelative(0x00FE, 0, 40000, 100000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_03D1)

    Sleep(2000)

    @scena.Lambda('lambda_03F1')
    def lambda_03F1():
        ChrMoveToRelative(0x00FE, 0, 40000, 100000, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_03F1)

    FadeOut(3000, 0, -1)
    OP_20(0x00000BB8)
    OP_0D()
    OP_21()
    OP_DC()
    MapClearFlags(0x02000000)
    MapSetFlags(0x00000010)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C1103._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x42F
@scena.Code('func_03_42F')
def func_03_42F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0101, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    CameraMove(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    CameraSetDistance(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 700000, 0)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, 10000, 20000, 0, 270)
    PlaySE(293, 0x01, 0x50)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)

    @scena.Lambda('lambda_04DF')
    def lambda_04DF():
        CameraSetDistance(3130, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_04DF)

    @scena.Lambda('lambda_04EF')
    def lambda_04EF():
        OP_6E(282, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04EF)

    FadeIn(2000, 0)

    @scena.Lambda('lambda_0508')
    def lambda_0508():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0508)

    Sleep(500)

    @scena.Lambda('lambda_0528')
    def lambda_0528():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0528)

    OP_24(0x0125, 0x55)
    Sleep(500)

    @scena.Lambda('lambda_054C')
    def lambda_054C():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_054C)

    OP_24(0x0125, 0x5A)
    Sleep(500)

    @scena.Lambda('lambda_0570')
    def lambda_0570():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0570)

    OP_24(0x0125, 0x5F)
    Sleep(500)

    @scena.Lambda('lambda_0594')
    def lambda_0594():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0594)

    OP_24(0x0125, 0x64)
    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    MapSetFlags(0x00100000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1102._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x5E4
@scena.Code('func_04_5E4')
def func_04_5E4():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x01, 'map\\\\mp078_00.eff')
    LoadEffect(0x02, 'monster\\\\ms10997.eff')
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-2510, 8550, -1900, 0)
    OP_67(0, 13580, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(57000, 0)
    OP_6E(860, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -5, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -10, 0, 0, 0x00, 0x00)
    PlaySE(451, 0x00, 0x64)
    OP_A1(0x000D, 0x0000)
    ChrClearFlags(0x000D, 0x0100)
    OP_D1(0x000D, 0, 270000, 0, 0)
    ChrSetPos(0x000D, 0, 0, 0, 270)
    CreateThread(0x0014, 0x03, 0x01, 0x0005)
    OP_A1(0x000E, 0x0001)
    OP_A1(0x000F, 0x0002)
    OP_A1(0x0010, 0x0003)
    ChrClearFlags(0x000E, 0x0100)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    OP_D1(0x000E, 0, 90000, 0, 0)
    OP_D1(0x000F, 0, 90000, 0, 0)
    OP_D1(0x0010, 0, 90000, 0, 0)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_0762')
    def lambda_0762():
        CameraMove(10080, -10000, 12130, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0762)

    @scena.Lambda('lambda_077A')
    def lambda_077A():
        OP_67(0, 6620, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_077A)

    @scena.Lambda('lambda_0792')
    def lambda_0792():
        CameraSetDistance(5200, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0792)

    @scena.Lambda('lambda_07A2')
    def lambda_07A2():
        OP_6C(57000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_07A2)

    @scena.Lambda('lambda_07B2')
    def lambda_07B2():
        OP_6E(723, 4000)

        ExitThread()

    DispatchAsync(0x0014, 0x0000, lambda_07B2)

    WaitForThreadExit(0x0101, 0x0000)
    OP_72(0x0001, 0x0004)
    OP_71(0x0001, 0x0020)
    OP_B0(0x0001, 0x3C)
    OP_6F(0x0001, 701)
    OP_70(0x0001, 900)
    ChrSetPos(0x000E, 88460, -4550, 76480, 270)
    OP_D1(0x000E, 0, 90000, 0, 0)
    PlaySE(121, 0x01, 0x50)

    @scena.Lambda('lambda_080C')
    def lambda_080C():
        OP_D1(0x00FE, 0, 90000, -20000, 4500)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_080C)

    @scena.Lambda('lambda_0826')
    def lambda_0826():
        ChrMoveTo(0x00FE, 8460, -4550, 36480, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0826)

    Sleep(4000)

    OP_24(0x0079, 0x55)

    @scena.Lambda('lambda_084A')
    def lambda_084A():
        ChrMoveTo(0x00FE, 8460, -4550, 36480, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_084A)

    Sleep(200)

    OP_24(0x0079, 0x5A)

    @scena.Lambda('lambda_086E')
    def lambda_086E():
        ChrMoveTo(0x00FE, 8460, -4550, 36480, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_086E)

    Sleep(200)

    OP_24(0x0079, 0x5F)

    @scena.Lambda('lambda_0892')
    def lambda_0892():
        ChrMoveTo(0x00FE, 8460, -4550, 36480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0892)

    Sleep(100)

    OP_24(0x0079, 0x64)

    @scena.Lambda('lambda_08B6')
    def lambda_08B6():
        ChrMoveTo(0x00FE, 8460, -4550, 36480, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_08B6)

    Sleep(1000)

    OP_72(0x0001, 0x0020)
    OP_73(0x0001)

    @scena.Lambda('lambda_08DE')
    def lambda_08DE():
        CameraMove(32950, -10000, 22130, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_08DE)

    OP_B0(0x0001, 0x5A)
    OP_6F(0x0001, 701)
    OP_70(0x0001, 940)
    CreateThread(0x000E, 0x01, 0x01, 0x0007)
    Sleep(2700)

    Fade(500)
    TerminateThread(0x0101, 0x00)
    ChrSetPos(0x000E, 54240, -6550, 20200, 270)
    OP_D1(0x000E, 5000, 70000, 20000, 0)
    CameraMove(33690, -3500, 13040, 0)
    OP_67(0, 500, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(225000, 0)
    OP_6E(723, 0)
    OP_0D()
    OP_71(0x0001, 0x0020)
    OP_B0(0x0001, 0x3C)
    OP_6F(0x0001, 941)
    OP_70(0x0001, 1000)
    CreateThread(0x0000, 0x00, 0x00, 0x0020)
    PlayEffect(0x01, 0x01, 0x000E, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    CreateThread(0x000D, 0x03, 0x01, 0x0006)
    Sleep(2000)

    OP_72(0x0001, 0x0020)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_23(0x0235)
    TerminateThread(0x0000, 0x00)
    Sleep(2000)

    @scena.Lambda('lambda_0A00')
    def lambda_0A00():
        CameraMove(44940, 0, 13160, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A00)

    @scena.Lambda('lambda_0A18')
    def lambda_0A18():
        OP_6C(200000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A18)

    @scena.Lambda('lambda_0A28')
    def lambda_0A28():
        OP_6E(829, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A28)

    OP_72(0x0002, 0x0004)
    OP_B0(0x0002, 0x3C)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 701)
    OP_70(0x0002, 900)
    ChrSetPos(0x000F, 93570, 14000, -1680, 270)
    OP_D1(0x000F, 0, 90000, -20000, 0)
    OP_72(0x0003, 0x0004)
    OP_B0(0x0003, 0x3C)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 701)
    OP_70(0x0003, 900)
    ChrSetPos(0x0010, 85510, 5000, -36750, 270)
    OP_D1(0x0010, 0, 90000, -40000, 0)
    CreateThread(0x000F, 0x01, 0x01, 0x0008)

    @scena.Lambda('lambda_0ABF')
    def lambda_0ABF():
        OP_D1(0x00FE, -5000, 90000, 0, 3000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_0ABF)

    Sleep(2500)

    CreateThread(0x0010, 0x01, 0x01, 0x0009)

    @scena.Lambda('lambda_0AE5')
    def lambda_0AE5():
        OP_D1(0x00FE, 0, 110000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_0AE5)

    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    Fade(500)
    CameraMove(11050, 4050, -830, 0)
    OP_67(0, 2210, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(91000, 0)
    OP_6E(829, 0)
    OP_0D()
    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0001, 941)
    OP_70(0x0001, 1000)
    OP_6F(0x0002, 941)
    OP_70(0x0002, 1000)
    OP_6F(0x0003, 941)
    OP_70(0x0003, 1000)
    CreateThread(0x0000, 0x00, 0x00, 0x0020)
    PlayEffect(0x01, 0x01, 0x000E, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x02, 0x000F, 0, 1500, -5000, 90, 355, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x03, 0x0010, 0, 1500, -5000, 110, 0, 340, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    CreateThread(0x000D, 0x03, 0x01, 0x0006)
    Sleep(2000)

    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_6F(0x0000, 125)
    OP_70(0x0000, 145)
    OP_73(0x0000)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    OP_6F(0x0000, 100)
    OP_70(0x0000, 120)
    Sleep(500)

    PlaySE(405, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 30)
    CreateThread(0x000D, 0x03, 0x01, 0x000A)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    Sleep(200)

    StopEffect(0x05, 0x00)
    StopEffect(0x06, 0x00)
    CreateThread(0x0010, 0x03, 0x01, 0x000E)
    Sleep(200)

    StopEffect(0x03, 0x00)
    StopEffect(0x04, 0x00)
    CreateThread(0x000F, 0x03, 0x01, 0x000D)
    Sleep(200)

    StopEffect(0x01, 0x00)
    StopEffect(0x02, 0x00)
    OP_23(0x0235)
    TerminateThread(0x0000, 0x00)
    CreateThread(0x000E, 0x03, 0x01, 0x000C)
    Sleep(400)

    CreateThread(0x0010, 0x00, 0x01, 0x000B)
    Sleep(1000)

    CreateThread(0x000F, 0x00, 0x01, 0x000B)
    Sleep(1000)

    CreateThread(0x000E, 0x00, 0x01, 0x000B)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x000D, 0x03)
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xD32
@scena.Code('func_05_D32')
def func_05_D32():
    Sleep(900)

    def _loc_D37(): pass

    label('loc_D37')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D4D',
    )

    PlaySE(288, 0x00, 0x50)
    Sleep(1300)

    Jump('loc_D37')

    def _loc_D4D(): pass

    label('loc_D4D')

    Return()

# id: 0x0006 offset: 0xD4E
@scena.Code('func_06_D4E')
def func_06_D4E():
    PlayEffect(0x02, 0xFF, 0x000D, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    def _loc_D88(): pass

    label('loc_D88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DCD',
    )

    PlayEffect(0x02, 0xFF, 0x000D, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Jump('loc_D88')

    def _loc_DCD(): pass

    label('loc_DCD')

    Return()

# id: 0x0007 offset: 0xDCE
@scena.Code('func_07_DCE')
def func_07_DCE():
    @scena.Lambda('lambda_0DD4')
    def lambda_0DD4():
        OP_D1(0x00FE, 5000, 70000, 20000, 2600)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0DD4)

    @scena.Lambda('lambda_0DEE')
    def lambda_0DEE():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0DEE)

    Sleep(100)

    @scena.Lambda('lambda_0E0E')
    def lambda_0E0E():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0E0E)

    Sleep(100)

    @scena.Lambda('lambda_0E2E')
    def lambda_0E2E():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0E2E)

    Sleep(200)

    @scena.Lambda('lambda_0E4E')
    def lambda_0E4E():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0E4E)

    Sleep(300)

    @scena.Lambda('lambda_0E6E')
    def lambda_0E6E():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0E6E)

    Sleep(500)

    @scena.Lambda('lambda_0E8E')
    def lambda_0E8E():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0E8E)

    Sleep(1800)

    @scena.Lambda('lambda_0EAE')
    def lambda_0EAE():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0EAE)

    Sleep(400)

    @scena.Lambda('lambda_0ECE')
    def lambda_0ECE():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0ECE)

    Sleep(300)

    @scena.Lambda('lambda_0EEE')
    def lambda_0EEE():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0EEE)

    Sleep(200)

    @scena.Lambda('lambda_0F0E')
    def lambda_0F0E():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0F0E)

    Sleep(100)

    @scena.Lambda('lambda_0F2E')
    def lambda_0F2E():
        ChrMoveTo(0x00FE, 54240, -6550, 20200, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0F2E)

    Return()

# id: 0x0008 offset: 0xF44
@scena.Code('func_08_F44')
def func_08_F44():
    @scena.Lambda('lambda_0F4A')
    def lambda_0F4A():
        ChrMoveTo(0x00FE, 56930, 7000, -1680, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0F4A)

    OP_72(0x0002, 0x0020)
    Sleep(2100)

    @scena.Lambda('lambda_0F6F')
    def lambda_0F6F():
        ChrMoveTo(0x00FE, 56930, 7000, -1680, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0F6F)

    OP_6F(0x0002, 901)
    OP_70(0x0002, 940)
    Sleep(400)

    @scena.Lambda('lambda_0F9D')
    def lambda_0F9D():
        ChrMoveTo(0x00FE, 56930, 7000, -1680, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0F9D)

    Sleep(300)

    @scena.Lambda('lambda_0FBD')
    def lambda_0FBD():
        ChrMoveTo(0x00FE, 56930, 7000, -1680, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0FBD)

    Sleep(200)

    @scena.Lambda('lambda_0FDD')
    def lambda_0FDD():
        ChrMoveTo(0x00FE, 56930, 7000, -1680, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0FDD)

    Return()

# id: 0x0009 offset: 0xFF3
@scena.Code('func_09_FF3')
def func_09_FF3():
    @scena.Lambda('lambda_0FF9')
    def lambda_0FF9():
        ChrMoveTo(0x00FE, 61430, 1000, -23970, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_0FF9)

    OP_72(0x0003, 0x0020)
    Sleep(900)

    OP_6F(0x0003, 901)
    OP_70(0x0003, 940)
    Sleep(900)

    @scena.Lambda('lambda_1031')
    def lambda_1031():
        ChrMoveTo(0x00FE, 61430, 1000, -23970, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_1031)

    Sleep(400)

    @scena.Lambda('lambda_1051')
    def lambda_1051():
        ChrMoveTo(0x00FE, 61430, 1000, -23970, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_1051)

    Sleep(300)

    @scena.Lambda('lambda_1071')
    def lambda_1071():
        ChrMoveTo(0x00FE, 61430, 1000, -23970, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_1071)

    Sleep(200)

    @scena.Lambda('lambda_1091')
    def lambda_1091():
        ChrMoveTo(0x00FE, 61430, 1000, -23970, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_1091)

    Return()

# id: 0x000A offset: 0x10A7
@scena.Code('func_0A_10A7')
def func_0A_10A7():
    @scena.Lambda('lambda_10AD')
    def lambda_10AD():
        OP_D1(0x00FE, 0, 270000, -50000, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_10AD)

    @scena.Lambda('lambda_10C7')
    def lambda_10C7():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_10C7)

    Sleep(100)

    @scena.Lambda('lambda_10E7')
    def lambda_10E7():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_10E7)

    Sleep(100)

    @scena.Lambda('lambda_1107')
    def lambda_1107():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1107)

    Sleep(200)

    @scena.Lambda('lambda_1127')
    def lambda_1127():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1127)

    Sleep(200)

    @scena.Lambda('lambda_1147')
    def lambda_1147():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1147)

    Sleep(300)

    @scena.Lambda('lambda_1167')
    def lambda_1167():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 48000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1167)

    Return()

# id: 0x000B offset: 0x117D
@scena.Code('func_0B_117D')
def func_0B_117D():
    @scena.Lambda('lambda_1183')
    def lambda_1183():
        OP_D1(0x00FE, 0, 90000, 30000, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1183)

    @scena.Lambda('lambda_119D')
    def lambda_119D():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_119D)

    Sleep(100)

    @scena.Lambda('lambda_11BD')
    def lambda_11BD():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_11BD)

    Sleep(100)

    @scena.Lambda('lambda_11DD')
    def lambda_11DD():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_11DD)

    Sleep(200)

    @scena.Lambda('lambda_11FD')
    def lambda_11FD():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_11FD)

    Sleep(200)

    @scena.Lambda('lambda_121D')
    def lambda_121D():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_121D)

    Sleep(300)

    @scena.Lambda('lambda_123D')
    def lambda_123D():
        ChrMoveToRelativeAsync(0x00FE, -800000, 100000, 300000, 48000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_123D)

    Return()

# id: 0x000C offset: 0x1253
@scena.Code('func_0C_1253')
def func_0C_1253():
    OP_72(0x0001, 0x0020)
    OP_73(0x0001)
    OP_6F(0x0001, 940)
    OP_70(0x0001, 901)
    OP_73(0x0001)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 900)
    OP_70(0x0001, 701)

    Return()

# id: 0x000D offset: 0x1280
@scena.Code('func_0D_1280')
def func_0D_1280():
    OP_72(0x0002, 0x0020)
    OP_73(0x0002)
    OP_6F(0x0002, 940)
    OP_70(0x0002, 901)
    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 900)
    OP_70(0x0002, 701)

    Return()

# id: 0x000E offset: 0x12AD
@scena.Code('func_0E_12AD')
def func_0E_12AD():
    OP_72(0x0003, 0x0020)
    OP_73(0x0003)
    OP_6F(0x0003, 940)
    OP_70(0x0003, 901)
    OP_73(0x0003)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 900)
    OP_70(0x0003, 701)

    Return()

# id: 0x000F offset: 0x12DA
@scena.Code('func_0F_12DA')
def func_0F_12DA():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0101, 0x0080)
    CameraMove(-98750, -550, -5980, 0)
    OP_67(0, 11650, -10000, 0)
    CameraSetDistance(7460, 0)
    OP_6C(219000, 0)
    OP_6E(905, 0)
    PlaySE(451, 0x00, 0x64)
    OP_76(0x00FF, 0x00000000, 0x0001, 1, 0, 0, 0x00, 0x00)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 455000, 0)
    OP_71(0x0000, 0x0004)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, -100000, 10250, 0, 90)
    OP_A1(0x000F, 0x0001)
    OP_A1(0x0010, 0x0002)
    OP_A1(0x0011, 0x0003)
    OP_A1(0x0012, 0x0004)
    ChrSetPos(0x000F, 90000, 0, -150000, 315)
    ChrSetPos(0x0010, 113500, 0, -130000, 315)
    ChrSetPos(0x0011, 137000, 0, -110000, 315)
    ChrSetPos(0x0012, 160500, 0, -90000, 315)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    ChrClearFlags(0x0012, 0x0100)
    OP_D1(0x000F, 0, 135000, 0, 0)
    OP_D1(0x0010, 0, 135000, 0, 0)
    OP_D1(0x0011, 0, 135000, 0, 0)
    OP_D1(0x0012, 0, 135000, 0, 0)
    PlaySE(293, 0x01, 0x50)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1449')
    def lambda_1449():
        OP_67(0, 4930, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1449)

    WaitForThreadExit(0x0101, 0x0000)
    OP_B0(0x0001, 0x3C)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 701)
    OP_70(0x0001, 900)
    Sleep(100)

    OP_B0(0x0003, 0x3C)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 701)
    OP_70(0x0003, 900)
    Sleep(100)

    OP_B0(0x0002, 0x3C)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 701)
    OP_70(0x0002, 900)
    Sleep(100)

    OP_B0(0x0004, 0x3C)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 701)
    OP_70(0x0004, 900)

    @scena.Lambda('lambda_14D1')
    def lambda_14D1():
        CameraMove(-56120, -2750, -26300, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_14D1)

    @scena.Lambda('lambda_14E9')
    def lambda_14E9():
        OP_67(0, 4930, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14E9)

    @scena.Lambda('lambda_1501')
    def lambda_1501():
        CameraSetDistance(7460, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1501)

    @scena.Lambda('lambda_1511')
    def lambda_1511():
        OP_6C(139000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1511)

    @scena.Lambda('lambda_1521')
    def lambda_1521():
        OP_6E(905, 4000)

        ExitThread()

    DispatchAsync(0x0014, 0x0000, lambda_1521)

    Sleep(2000)

    PlaySE(121, 0x01, 0x50)
    CreateThread(0x000F, 0x01, 0x01, 0x0010)
    CreateThread(0x0010, 0x01, 0x01, 0x0011)
    CreateThread(0x0011, 0x01, 0x01, 0x0012)
    CreateThread(0x0012, 0x01, 0x01, 0x0013)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_155C')
    def lambda_155C():
        CameraMove(-25590, -2750, 4840, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_155C)

    @scena.Lambda('lambda_1574')
    def lambda_1574():
        OP_6C(107000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1574)

    Sleep(2000)

    TerminateThread(0x000F, 0x02)

    @scena.Lambda('lambda_158D')
    def lambda_158D():
        OP_D1(0x00FE, 0, 250000, 0, 9000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_158D)

    OP_72(0x0001, 0x0020)
    Sleep(500)

    TerminateThread(0x0010, 0x02)

    @scena.Lambda('lambda_15B5')
    def lambda_15B5():
        OP_D1(0x00FE, 0, 270000, 0, 9000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_15B5)

    OP_72(0x0002, 0x0020)
    Sleep(500)

    TerminateThread(0x0011, 0x02)

    @scena.Lambda('lambda_15DD')
    def lambda_15DD():
        OP_D1(0x00FE, 0, 270000, 0, 9000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_15DD)

    OP_72(0x0003, 0x0020)
    Sleep(500)

    TerminateThread(0x0012, 0x02)

    @scena.Lambda('lambda_1605')
    def lambda_1605():
        OP_D1(0x00FE, 0, 290000, 0, 9000)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_1605)

    OP_72(0x0004, 0x0020)
    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0012, 0x0001)
    TerminateThread(0x000F, 0x03)
    ChrSetPos(0x000F, 10000, 0, -45000, 315)
    TerminateThread(0x0010, 0x03)
    ChrSetPos(0x0010, 0, 6000, -16000, 315)
    TerminateThread(0x0011, 0x03)
    ChrSetPos(0x0011, 0, 6000, 16000, 315)
    TerminateThread(0x0012, 0x03)
    ChrSetPos(0x0012, 10000, 0, 45000, 315)
    Fade(1000)
    CameraMove(-13160, -10000, -660, 0)
    OP_67(0, 5060, -10000, 0)
    CameraSetDistance(7460, 0)
    OP_6C(282000, 0)
    OP_6E(1343, 0)
    OP_24(0x0079, 0x64)
    OP_24(0x0125, 0x46)
    WaitForThreadExit(0x0012, 0x0002)
    Sleep(400)

    OP_B0(0x0001, 0x1E)
    OP_6F(0x0001, 901)
    OP_70(0x0001, 940)
    Sleep(400)

    OP_B0(0x0002, 0x1E)
    OP_6F(0x0002, 901)
    OP_70(0x0002, 940)
    Sleep(400)

    OP_B0(0x0003, 0x1E)
    OP_6F(0x0003, 901)
    OP_70(0x0003, 940)
    Sleep(400)

    OP_B0(0x0004, 0x1E)
    OP_6F(0x0004, 901)
    OP_70(0x0004, 940)
    OP_73(0x0004)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x1752
@scena.Code('func_10_1752')
def func_10_1752():
    OP_94(0x01, 0x00FE, 0x0000, 0x00013880, 0x00007530, 0x00)

    @scena.Lambda('lambda_1767')
    def lambda_1767():
        OP_D1(0x00FE, 0, 135000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1767)

    @scena.Lambda('lambda_1781')
    def lambda_1781():
        ChrMoveTo(0x00FE, 0, 0, -45000, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1781)

    Sleep(1900)

    @scena.Lambda('lambda_17A1')
    def lambda_17A1():
        ChrMoveTo(0x00FE, 0, 0, -45000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_17A1)

    Sleep(200)

    @scena.Lambda('lambda_17C1')
    def lambda_17C1():
        ChrMoveTo(0x00FE, 0, 0, -45000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_17C1)

    Sleep(200)

    @scena.Lambda('lambda_17E1')
    def lambda_17E1():
        ChrMoveTo(0x00FE, 0, 0, -45000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_17E1)

    Sleep(100)

    @scena.Lambda('lambda_1801')
    def lambda_1801():
        ChrMoveTo(0x00FE, 0, 0, -45000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1801)

    Sleep(100)

    @scena.Lambda('lambda_1821')
    def lambda_1821():
        ChrMoveTo(0x00FE, 0, 0, -45000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1821)

    Return()

# id: 0x0011 offset: 0x1837
@scena.Code('func_11_1837')
def func_11_1837():
    OP_94(0x01, 0x00FE, 0x0000, 0x00013880, 0x00007530, 0x00)

    @scena.Lambda('lambda_184C')
    def lambda_184C():
        OP_D1(0x00FE, 0, 135000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_184C)

    @scena.Lambda('lambda_1866')
    def lambda_1866():
        ChrMoveTo(0x00FE, 0, 0, -16000, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1866)

    Sleep(2500)

    @scena.Lambda('lambda_1886')
    def lambda_1886():
        ChrMoveTo(0x00FE, 0, 0, -16000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1886)

    Sleep(200)

    @scena.Lambda('lambda_18A6')
    def lambda_18A6():
        ChrMoveTo(0x00FE, 0, 0, -16000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_18A6)

    Sleep(200)

    @scena.Lambda('lambda_18C6')
    def lambda_18C6():
        ChrMoveTo(0x00FE, 0, 0, -16000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_18C6)

    Sleep(100)

    @scena.Lambda('lambda_18E6')
    def lambda_18E6():
        ChrMoveTo(0x00FE, 0, 0, -16000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_18E6)

    Sleep(100)

    @scena.Lambda('lambda_1906')
    def lambda_1906():
        ChrMoveTo(0x00FE, 0, 0, -16000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1906)

    Return()

# id: 0x0012 offset: 0x191C
@scena.Code('func_12_191C')
def func_12_191C():
    OP_94(0x01, 0x00FE, 0x0000, 0x00013880, 0x00007530, 0x00)

    @scena.Lambda('lambda_1931')
    def lambda_1931():
        OP_D1(0x00FE, 0, 135000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1931)

    @scena.Lambda('lambda_194B')
    def lambda_194B():
        ChrMoveTo(0x00FE, 0, 0, 16000, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_194B)

    Sleep(3300)

    @scena.Lambda('lambda_196B')
    def lambda_196B():
        ChrMoveTo(0x00FE, 0, 0, 16000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_196B)

    Sleep(200)

    @scena.Lambda('lambda_198B')
    def lambda_198B():
        ChrMoveTo(0x00FE, 0, 0, 16000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_198B)

    Sleep(200)

    @scena.Lambda('lambda_19AB')
    def lambda_19AB():
        ChrMoveTo(0x00FE, 0, 0, 16000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_19AB)

    Sleep(100)

    @scena.Lambda('lambda_19CB')
    def lambda_19CB():
        ChrMoveTo(0x00FE, 0, 0, 16000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_19CB)

    Sleep(100)

    @scena.Lambda('lambda_19EB')
    def lambda_19EB():
        ChrMoveTo(0x00FE, 0, 0, 16000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_19EB)

    Return()

# id: 0x0013 offset: 0x1A01
@scena.Code('func_13_1A01')
def func_13_1A01():
    OP_94(0x01, 0x00FE, 0x0000, 0x00013880, 0x00007530, 0x00)

    @scena.Lambda('lambda_1A16')
    def lambda_1A16():
        OP_D1(0x00FE, 0, 135000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1A16)

    @scena.Lambda('lambda_1A30')
    def lambda_1A30():
        ChrMoveTo(0x00FE, 0, 0, 45000, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1A30)

    Sleep(4300)

    @scena.Lambda('lambda_1A50')
    def lambda_1A50():
        ChrMoveTo(0x00FE, 0, 0, 45000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1A50)

    Sleep(200)

    @scena.Lambda('lambda_1A70')
    def lambda_1A70():
        ChrMoveTo(0x00FE, 0, 0, 45000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1A70)

    Sleep(200)

    @scena.Lambda('lambda_1A90')
    def lambda_1A90():
        ChrMoveTo(0x00FE, 0, 0, 45000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1A90)

    Sleep(100)

    @scena.Lambda('lambda_1AB0')
    def lambda_1AB0():
        ChrMoveTo(0x00FE, 0, 0, 45000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1AB0)

    Sleep(100)

    @scena.Lambda('lambda_1AD0')
    def lambda_1AD0():
        ChrMoveTo(0x00FE, 0, 0, 45000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1AD0)

    Return()

# id: 0x0014 offset: 0x1AE6
@scena.Code('func_14_1AE6')
def func_14_1AE6():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x01, 'map\\\\mp078_00.eff')
    LoadEffect(0x02, 'monster\\\\ms10997.eff')
    ChrSetFlags(0x0101, 0x0080)
    OP_71(0x0000, 0x0004)
    CameraMove(-95940, 3750, -1830, 0)
    OP_67(0, 1090, -10000, 0)
    CameraSetDistance(7300, 0)
    OP_6C(225000, 0)
    OP_6E(919, 0)
    PlaySE(451, 0x00, 0x64)
    OP_76(0x00FF, 0x00000000, 0x0001, 1, 0, 0, 0x00, 0x00)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, -100000, 10250, 0, 90)
    OP_A1(0x000F, 0x0001)
    OP_A1(0x0010, 0x0002)
    OP_A1(0x0011, 0x0003)
    OP_A1(0x0012, 0x0004)
    ChrSetPos(0x000F, 10000, 0, -45000, 315)
    ChrSetPos(0x0010, 0, 6000, -15000, 315)
    ChrSetPos(0x0011, 0, 6000, 15000, 315)
    ChrSetPos(0x0012, 10000, 0, 45000, 315)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    ChrClearFlags(0x0012, 0x0100)
    OP_D1(0x000F, 0, 260000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)
    OP_D1(0x0012, 0, 280000, 0, 0)
    PlaySE(293, 0x01, 0x50)
    PlaySE(121, 0x01, 0x64)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    OP_6F(0x0001, 940)
    OP_6F(0x0002, 940)
    OP_6F(0x0003, 940)
    OP_6F(0x0004, 940)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1C91')
    def lambda_1C91():
        CameraMove(-8020, 3750, 7710, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1C91)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    OP_A1(0x000D, 0x0000)
    ChrSetPos(0x000D, 150000, 0, 0, 270)
    OP_72(0x0000, 0x0004)
    OP_D1(0x000F, 5000, 70000, 20000, 0)
    OP_D1(0x0010, -5000, 90000, 0, 0)
    OP_D1(0x0011, 0, 110000, -20000, 0)
    ChrSetPos(0x000F, 224240, -6550, 20200, 270)
    ChrSetPos(0x0010, 226930, 7000, -1680, 270)
    ChrSetPos(0x0011, 231430, 1000, -23970, 270)
    OP_B0(0x0001, 0x3C)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 941)
    OP_70(0x0001, 1000)
    OP_B0(0x0002, 0x3C)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 941)
    OP_70(0x0002, 1000)
    OP_B0(0x0003, 0x3C)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 941)
    OP_70(0x0003, 1000)
    OP_76(0x00FF, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -5, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 400000, 0)
    Fade(1000)
    CameraMove(168880, 3750, 210, 0)
    OP_67(0, 1090, -10000, 0)
    CameraSetDistance(6360, 0)
    OP_6C(110000, 0)
    OP_6E(916, 0)
    PlaySE(121, 0x01, 0x64)
    OP_23(0x0125)
    CreateThread(0x0014, 0x03, 0x01, 0x0005)
    OP_0D()
    CreateThread(0x0000, 0x00, 0x00, 0x0020)
    PlayEffect(0x01, 0x01, 0x000F, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0x07, 0x000D, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    StopEffect(0x01, 0x00)
    PlayEffect(0x01, 0x02, 0x0010, 0, 1500, -5000, 90, 355, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0x07, 0x000D, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    StopEffect(0x02, 0x00)
    StopEffect(0x07, 0x00)
    TerminateThread(0x0000, 0x00)
    OP_23(0x0235)

    @scena.Lambda('lambda_1F25')
    def lambda_1F25():
        CameraMove(169150, 3750, 0, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1F25)

    @scena.Lambda('lambda_1F3D')
    def lambda_1F3D():
        OP_67(0, 1740, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F3D)

    @scena.Lambda('lambda_1F55')
    def lambda_1F55():
        OP_6C(90000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F55)

    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_6F(0x0000, 100)
    OP_70(0x0000, 120)
    Sleep(500)

    PlaySE(405, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 30)
    OP_B0(0x0000, 0x14)

    @scena.Lambda('lambda_1F9F')
    def lambda_1F9F():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1F9F)

    Sleep(100)

    @scena.Lambda('lambda_1FBF')
    def lambda_1FBF():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1FBF)

    Sleep(100)

    @scena.Lambda('lambda_1FDF')
    def lambda_1FDF():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1FDF)

    Sleep(200)

    @scena.Lambda('lambda_1FFF')
    def lambda_1FFF():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1FFF)

    Sleep(200)

    @scena.Lambda('lambda_201F')
    def lambda_201F():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_201F)

    Sleep(300)

    @scena.Lambda('lambda_203F')
    def lambda_203F():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_203F)

    Sleep(1000)

    TerminateThread(0x0014, 0x03)
    OP_72(0x0001, 0x0020)
    CreateThread(0x000F, 0x00, 0x01, 0x0015)
    Sleep(200)

    OP_72(0x0002, 0x0020)
    CreateThread(0x0010, 0x00, 0x01, 0x0015)
    Sleep(200)

    OP_72(0x0003, 0x0020)
    CreateThread(0x0011, 0x00, 0x01, 0x0015)
    Sleep(3000)

    OP_11(0xB8, 0xD8, 0xFF, 20000, 555000, 0)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    OP_76(0x00FF, 0x00000000, 0x0001, 2, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, 0, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -1, -1, 0, 0x00, 0x00)
    TerminateThread(0x000D, 0x01)
    ChrSetPos(0x000D, 250000, 0, 0, 270)

    @scena.Lambda('lambda_2118')
    def lambda_2118():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2118)

    OP_B0(0x0000, 0x0F)
    ChrSetPos(0x000F, 10000, 0, -45000, 315)
    ChrSetPos(0x0010, 0, 6000, -15000, 315)
    ChrSetPos(0x0011, 0, 6000, 15000, 315)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0001, 940)
    OP_6F(0x0002, 940)
    OP_6F(0x0003, 940)
    OP_6F(0x0004, 940)
    OP_D1(0x000F, 0, 260000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)
    Fade(1000)
    CameraMove(38580, 3750, 0, 0)
    OP_67(0, 1090, -10000, 0)
    CameraSetDistance(7300, 0)
    OP_6C(90000, 0)
    OP_6E(919, 0)
    PlaySE(121, 0x01, 0x64)
    PlaySE(293, 0x01, 0x46)
    OP_0D()

    @scena.Lambda('lambda_2234')
    def lambda_2234():
        CameraMove(38580, 3750, 0, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2234)

    @scena.Lambda('lambda_224C')
    def lambda_224C():
        OP_67(0, 1200, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_224C)

    @scena.Lambda('lambda_2264')
    def lambda_2264():
        CameraSetDistance(12530, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2264)

    @scena.Lambda('lambda_2274')
    def lambda_2274():
        OP_6E(970, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2274)

    PlaySE(288, 0x00, 0x3C)
    Sleep(1300)

    PlaySE(288, 0x00, 0x41)
    Sleep(1300)

    PlaySE(288, 0x00, 0x46)
    Sleep(1300)

    FadeOut(1000, 0, -1)
    PlaySE(288, 0x00, 0x4B)
    Sleep(1300)

    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x22BF
@scena.Code('func_15_22BF')
def func_15_22BF():
    @scena.Lambda('lambda_22C5')
    def lambda_22C5():
        OP_D1(0x00FE, 20000, 90000, 30000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_22C5)

    @scena.Lambda('lambda_22DF')
    def lambda_22DF():
        ChrMoveToRelativeAsync(0x00FE, 0, -30000, 400000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_22DF)

    Sleep(100)

    @scena.Lambda('lambda_22FF')
    def lambda_22FF():
        ChrMoveToRelativeAsync(0x00FE, 0, -30000, 400000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_22FF)

    Sleep(100)

    @scena.Lambda('lambda_231F')
    def lambda_231F():
        ChrMoveToRelativeAsync(0x00FE, 0, -30000, 400000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_231F)

    Sleep(200)

    @scena.Lambda('lambda_233F')
    def lambda_233F():
        ChrMoveToRelativeAsync(0x00FE, 0, -30000, 400000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_233F)

    Sleep(300)

    @scena.Lambda('lambda_235F')
    def lambda_235F():
        ChrMoveToRelativeAsync(0x00FE, 0, -30000, 400000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_235F)

    Sleep(500)

    @scena.Lambda('lambda_237F')
    def lambda_237F():
        ChrMoveToRelativeAsync(0x00FE, 0, -30000, 400000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_237F)

    Return()

# id: 0x0016 offset: 0x2395
@scena.Code('func_16_2395')
def func_16_2395():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x00, 'battle\\\\btbomb00.eff')
    LoadEffect(0x01, 'map\\\\mp078_00.eff')
    LoadEffect(0x02, 'monster\\\\ms10997.eff')
    ChrSetFlags(0x0101, 0x0080)
    CameraMove(17660, 13750, -20070, 0)
    OP_67(0, 2990, -10000, 0)
    CameraSetDistance(3670, 0)
    OP_6C(60000, 0)
    OP_6E(1289, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, 2, 0, 0, 0x00, 0x00)
    PlaySE(451, 0x00, 0x64)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, -100000, 10250, 0, 90)
    OP_A1(0x000F, 0x0001)
    OP_A1(0x0010, 0x0002)
    OP_A1(0x0011, 0x0003)
    OP_A1(0x0012, 0x0004)
    ChrSetPos(0x000F, 10000, 0, -45000, 90)
    ChrSetPos(0x0010, 0, 6000, -15000, 90)
    ChrSetPos(0x0011, 0, 6000, 15000, 90)
    ChrSetPos(0x0012, 10000, 0, 45000, 90)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    ChrClearFlags(0x0012, 0x0100)
    OP_D1(0x000F, 0, 260000, 0, 0)
    OP_D1(0x0010, 0, 268000, 0, 0)
    OP_D1(0x0011, 0, 272000, 0, 0)
    OP_D1(0x0012, 0, 280000, 0, 0)
    PlaySE(121, 0x00, 0x64)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    OP_B0(0x0001, 0x3C)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 941)
    OP_70(0x0001, 1000)
    OP_B0(0x0002, 0x3C)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 941)
    OP_70(0x0002, 1000)
    OP_B0(0x0003, 0x3C)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 941)
    OP_70(0x0003, 1000)
    OP_B0(0x0004, 0x3C)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 941)
    OP_70(0x0004, 1000)
    OP_A1(0x000D, 0x0000)
    ChrSetPos(0x000D, 150000, 4000, 0, 270)
    ChrClearFlags(0x000D, 0x0100)
    OP_D1(0x000D, 0, 270000, 0, 0)
    FadeIn(2000, 0)
    Sleep(600)

    CreateThread(0x0000, 0x03, 0x00, 0x0020)
    PlayEffect(0x01, 0x01, 0x000F, 0, 1500, -5000, 250, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x02, 0x0010, 0, 1500, -5000, 268, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0x03, 0x0011, 0, 1500, -5000, 272, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x04, 0x0012, 0, 1500, -5000, 290, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x000D, 0x00, 0x01, 0x0018)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    CreateThread(0x000D, 0x03, 0x01, 0x0017)

    @scena.Lambda('lambda_26B1')
    def lambda_26B1():
        CameraMove(17020, 13750, 23220, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_26B1)

    @scena.Lambda('lambda_26C9')
    def lambda_26C9():
        OP_6C(120000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_26C9)

    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_6F(0x0000, 170)
    OP_70(0x0000, 190)
    OP_73(0x0000)
    OP_6F(0x0000, 195)
    OP_70(0x0000, 215)
    OP_73(0x0000)
    OP_6F(0x0000, 220)
    OP_70(0x0000, 230)
    PlaySE(405, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 235)
    OP_70(0x0000, 265)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    ChrSetPos(0x000D, 60000, 4000, 0, 270)
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000D, 0x01)
    CameraMove(63240, 6750, -2890, 0)
    OP_67(0, 2630, -10000, 0)
    CameraSetDistance(5120, 0)
    OP_6C(120000, 0)
    OP_6E(934, 0)
    OP_0D()

    @scena.Lambda('lambda_278D')
    def lambda_278D():
        CameraMove(62720, 6750, 2750, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_278D)

    @scena.Lambda('lambda_27A5')
    def lambda_27A5():
        CameraSetDistance(3990, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27A5)

    @scena.Lambda('lambda_27B5')
    def lambda_27B5():
        OP_6C(57000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27B5)

    Sleep(1000)

    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_6F(0x0000, 235)
    OP_70(0x0000, 265)
    PlaySE(405, 0x00, 0x64)
    OP_73(0x0000)
    OP_B0(0x0000, 0x0D)
    OP_6F(0x0000, 235)
    OP_70(0x0000, 265)
    OP_73(0x0000)
    OP_B0(0x0000, 0x0B)
    OP_6F(0x0000, 235)
    OP_70(0x0000, 265)
    PlaySE(405, 0x00, 0x64)
    OP_73(0x0000)
    OP_B0(0x0000, 0x09)
    OP_6F(0x0000, 235)
    OP_70(0x0000, 265)
    OP_73(0x0000)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    StopEffect(0x03, 0x02)
    StopEffect(0x04, 0x02)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_23(0x0235)
    TerminateThread(0x0000, 0x03)
    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 270)
    OP_70(0x0000, 290)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    Fade(1000)
    CameraMove(60540, 6750, 220, 0)
    OP_67(0, -129430, -10000, 0)
    CameraSetDistance(660, 0)
    OP_6C(90000, 0)
    OP_6E(934, 0)

    @scena.Lambda('lambda_28A2')
    def lambda_28A2():
        ChrMoveToRelativeAsync(0x00FE, 0, -100000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_28A2)

    OP_73(0x0000)
    OP_B0(0x0000, 0x02)
    OP_6F(0x0000, 290)
    OP_70(0x0000, 300)
    Sleep(100)

    @scena.Lambda('lambda_28D7')
    def lambda_28D7():
        ChrMoveToRelativeAsync(0x00FE, 0, -100000, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_28D7)

    Sleep(100)

    @scena.Lambda('lambda_28F7')
    def lambda_28F7():
        ChrMoveToRelativeAsync(0x00FE, 0, -100000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_28F7)

    Sleep(200)

    @scena.Lambda('lambda_2917')
    def lambda_2917():
        ChrMoveToRelativeAsync(0x00FE, 0, -100000, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2917)

    Sleep(200)

    @scena.Lambda('lambda_2937')
    def lambda_2937():
        ChrMoveToRelativeAsync(0x00FE, 0, -100000, 0, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2937)

    Sleep(300)

    @scena.Lambda('lambda_2957')
    def lambda_2957():
        ChrMoveToRelativeAsync(0x00FE, 0, -100000, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2957)

    Sleep(2500)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    PlaySE(220, 0x00, 0x64)
    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    OP_DC()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x29AD
@scena.Code('func_17_29AD')
def func_17_29AD():
    PlayEffect(0x02, 0x07, 0x000D, -5000, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    def _loc_29E7(): pass

    label('loc_29E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A2C',
    )

    PlayEffect(0x02, 0x07, 0x000D, -5000, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Jump('loc_29E7')

    def _loc_2A2C(): pass

    label('loc_2A2C')

    Return()

# id: 0x0018 offset: 0x2A2D
@scena.Code('func_18_2A2D')
def func_18_2A2D():
    @scena.Lambda('lambda_2A33')
    def lambda_2A33():
        ChrMoveTo(0x00FE, 60000, 4000, 0, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A33)

    Sleep(2500)

    @scena.Lambda('lambda_2A53')
    def lambda_2A53():
        ChrMoveTo(0x00FE, 60000, 4000, 0, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A53)

    Sleep(400)

    @scena.Lambda('lambda_2A73')
    def lambda_2A73():
        ChrMoveTo(0x00FE, 60000, 4000, 0, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A73)

    Sleep(300)

    @scena.Lambda('lambda_2A93')
    def lambda_2A93():
        ChrMoveTo(0x00FE, 60000, 4000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A93)

    Sleep(200)

    @scena.Lambda('lambda_2AB3')
    def lambda_2AB3():
        ChrMoveTo(0x00FE, 60000, 4000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2AB3)

    Sleep(100)

    @scena.Lambda('lambda_2AD3')
    def lambda_2AD3():
        ChrMoveTo(0x00FE, 60000, 4000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2AD3)

    Return()

# id: 0x0019 offset: 0x2AE9
@scena.Code('func_19_2AE9')
def func_19_2AE9():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0004, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 255000, 0)
    CameraMove(-30090, -10000, -9900, 0)
    OP_67(0, -12470, -10000, 0)
    CameraSetDistance(3480, 0)
    OP_6C(57000, 0)
    OP_6E(923, 0)
    OP_A1(0x000F, 0x0001)
    OP_A1(0x0010, 0x0002)
    OP_A1(0x0011, 0x0003)
    ChrSetPos(0x000F, -30000, 0, 0, 90)
    ChrSetPos(0x0010, -15000, 0, 25000, 90)
    ChrSetPos(0x0011, -15000, 0, -25000, 90)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    OP_D1(0x000F, 0, 90000, 0, 0)
    OP_D1(0x0010, 0, 90000, 0, 0)
    OP_D1(0x0011, 0, 90000, 0, 0)
    PlaySE(121, 0x00, 0x64)
    OP_B0(0x0001, 0x1E)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 520)
    OP_B0(0x0003, 0x1E)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 500)
    OP_70(0x0003, 520)
    OP_B0(0x0002, 0x1E)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 500)
    OP_70(0x0002, 520)
    OP_0D()
    LoadEffect(0x00, 'map\\\\mp079_00.eff')

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_2C6D')
    def lambda_2C6D():
        OP_6E(1100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2C6D)

    PlayEffect(0x00, 0xFF, 0x00FF, -35000, -35000, 0, 90, -90, 0, 10000, 10000, 10000, 0x00FF, 0, 0, 0, 0)
    PlaySE(289, 0x00, 0x64)
    Sleep(600)

    CreateThread(0x000F, 0x02, 0x01, 0x001B)
    CreateThread(0x0010, 0x02, 0x01, 0x001C)
    CreateThread(0x0011, 0x02, 0x01, 0x001D)
    Sleep(3000)

    @scena.Lambda('lambda_2CD6')
    def lambda_2CD6():
        CameraMove(-13570, 30000, -19950, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2CD6)

    @scena.Lambda('lambda_2CEE')
    def lambda_2CEE():
        OP_67(0, -10590, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2CEE)

    @scena.Lambda('lambda_2D06')
    def lambda_2D06():
        CameraSetDistance(2480, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2D06)

    OP_12(0x00004E20, 0x0006F158, 0x00001388)
    OP_72(0x0000, 0x0020)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 55)
    OP_70(0x0000, 75)
    OP_A1(0x000D, 0x0000)
    ChrSetPos(0x000D, -25000, -55000, 0, 90)
    OP_72(0x0000, 0x0004)
    CreateThread(0x000D, 0x02, 0x01, 0x001A)

    @scena.Lambda('lambda_2D5D')
    def lambda_2D5D():
        ChrMoveToRelativeAsync(0x000D, 120000, 200000, 0, 36000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2D5D)

    Sleep(1000)

    @scena.Lambda('lambda_2D7D')
    def lambda_2D7D():
        ChrMoveToRelativeAsync(0x000D, 120000, 200000, 0, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2D7D)

    Sleep(1000)

    @scena.Lambda('lambda_2D9D')
    def lambda_2D9D():
        ChrMoveToRelativeAsync(0x000D, 120000, 200000, 0, 46000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2D9D)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x000D, 0x02)
    MapSetFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/E0900._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x2DD9
@scena.Code('func_1A_2DD9')
def func_1A_2DD9():
    PlaySE(288, 0x00, 0x64)
    Sleep(1300)

    PlaySE(288, 0x00, 0x5A)
    Sleep(1300)

    PlaySE(288, 0x00, 0x50)
    Sleep(1300)

    PlaySE(288, 0x00, 0x46)
    Sleep(1300)

    PlaySE(288, 0x00, 0x3C)
    Sleep(1300)

    PlaySE(288, 0x00, 0x32)
    Sleep(1300)

    PlaySE(288, 0x00, 0x28)
    Sleep(1300)

    PlaySE(288, 0x00, 0x1E)
    Sleep(1300)

    PlaySE(288, 0x00, 0x14)
    Sleep(1300)

    PlaySE(288, 0x00, 0x0A)

    Return()

# id: 0x001B offset: 0x2E39
@scena.Code('func_1B_2E39')
def func_1B_2E39():
    @scena.Lambda('lambda_2E3F')
    def lambda_2E3F():
        ChrMoveToRelativeAsync(0x00FE, -6000, 0, -2000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2E3F)

    OP_D1(0x000F, -10000, 80000, -10000, 700)
    OP_D1(0x000F, 10000, 95000, 5000, 700)
    OP_D1(0x000F, -5000, 85000, -5000, 800)
    OP_D1(0x000F, 0, 90000, 0, 800)

    Return()

# id: 0x001C offset: 0x2EA1
@scena.Code('func_1C_2EA1')
def func_1C_2EA1():
    @scena.Lambda('lambda_2EA7')
    def lambda_2EA7():
        ChrMoveToRelativeAsync(0x00FE, -5000, 0, 3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2EA7)

    OP_D1(0x0010, -10000, 95000, 10000, 600)
    OP_D1(0x0010, 5000, 80000, -10000, 600)
    OP_D1(0x0010, -5000, 95000, 5000, 700)
    OP_D1(0x0010, 0, 90000, 0, 700)

    Return()

# id: 0x001D offset: 0x2F09
@scena.Code('func_1D_2F09')
def func_1D_2F09():
    @scena.Lambda('lambda_2F0F')
    def lambda_2F0F():
        ChrMoveToRelativeAsync(0x00FE, 3000, 0, -3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2F0F)

    OP_D1(0x0011, 15000, 80000, -10000, 700)
    OP_D1(0x0011, -5000, 90000, 10000, 700)
    OP_D1(0x0011, 5000, 85000, -8000, 800)
    OP_D1(0x0011, 0, 90000, 0, 800)

    Return()

# id: 0x001E offset: 0x2F71
@scena.Code('func_1E_2F71')
def func_1E_2F71():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x01, 'map\\\\mp077_00.eff')
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-20560, 20530, -22790, 0)
    OP_67(0, 5360, -10000, 0)
    CameraSetDistance(8670, 0)
    OP_6C(54000, 0)
    OP_6E(523, 0)
    PlaySE(451, 0x00, 0x64)
    OP_71(0x0000, 0x0004)
    OP_A1(0x000F, 0x0001)
    OP_A1(0x0010, 0x0002)
    OP_A1(0x0011, 0x0003)
    OP_A1(0x0012, 0x0004)
    ChrSetPos(0x000F, 20000, 0, 20000, 90)
    ChrSetPos(0x0010, 20000, 0, -20000, 90)
    ChrSetPos(0x0011, 60000, 0, 30000, 90)
    ChrSetPos(0x0012, 60000, 0, -30000, 90)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    ChrClearFlags(0x0012, 0x0100)
    OP_D1(0x000F, 0, 90000, 0, 0)
    OP_D1(0x0010, 0, 90000, 0, 0)
    OP_D1(0x0011, 0, 90000, 0, 0)
    OP_D1(0x0012, 0, 90000, 0, 0)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, -10000, 0, 0, 270)
    Yield()
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetBattleFlags(0x000A, 0x0020)
    ChrSetBattleFlags(0x0009, 0x0020)
    ChrSetBattleFlags(0x000B, 0x0020)
    ChrSetBattleFlags(0x000C, 0x0020)
    OP_89(0x000A, -28840, 3200, 90, 270)
    OP_89(0x0009, -28240, 3200, 820, 270)
    OP_89(0x000B, -27820, 3200, -1500, 270)
    OP_89(0x000C, -28450, 3200, -850, 270)
    OP_E5(0x0A, 0x00, 0x00)
    OP_E5(0x09, 0x00, 0x00)
    OP_E5(0x0C, 0x00, 0x00)
    OP_E5(0x0B, 0x00, 0x00)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x28,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    PlaySE(293, 0x01, 0x50)
    PlaySE(121, 0x01, 0x50)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_B0(0x0005, 0x0A)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)

    @scena.Lambda('lambda_3185')
    def lambda_3185():
        CameraSetDistance(7490, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3185)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    CameraMove(-27780, 3000, -200, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(54000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x000C,
        (
            '#0280311222V#156F#5P这么久了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280311223V艾丝蒂尔他们\n',
            '不要紧吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0270311224V#142F#2P该不会\n',
            '被击败了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100311225V#176F#5P如果是那样，基库\n',
            '应该会回来报告危机的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100311226V#178F现在只能信任他们继续等待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0270311227V#145F#2P可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600311228V#160F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311229V#163F离黄昏还有一个小时……\n',
            '时间一到，就开始突入。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311230V上尉，你先做好准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100311231V#175F#5P遵命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311232V#3S不用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0270311233V#143F#2P什、什么声音！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100311234V#178F#5P刚才那是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600311235V#161F#5P从哪儿传来的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0280311236V#153F#5P咦～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280311237V好像有什么庞然大物\n',
            '从下面飞上来了哦～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100311238V#173F#5P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    CameraMove(-73960, 11720, -1060, 0)
    OP_67(0, 7820, -10000, 0)
    CameraSetDistance(1500, 0)
    OP_6C(311000, 0)
    OP_6E(901, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    OP_72(0x0000, 0x0004)
    OP_A1(0x000D, 0x0000)
    ChrSetPos(0x000D, -130000, -30000, 0, 90)
    OP_6F(0x0000, 55)
    OP_70(0x0000, 75)
    Sleep(400)

    PlayEffect(0x01, 0xFF, 0x00FF, -104000, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -104000, 0, 15000, 270, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -104000, 0, -15000, 270, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x000D, 0x03, 0x01, 0x001F)
    Sleep(200)

    CreateThread(0x000D, 0x00, 0x01, 0x0020)
    OP_75(0x00, 0x0000000D, 0x07)
    Sleep(3000)

    Fade(500)
    CameraMove(-6420, 12220, -23160, 0)
    OP_67(0, 1380, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(290000, 0)
    OP_6E(528, 0)
    WaitForThreadExit(0x000D, 0x0000)
    OP_72(0x0000, 0x0020)
    OP_73(0x0000)

    @scena.Lambda('lambda_36F5')
    def lambda_36F5():
        CameraSetDistance(10, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_36F5)

    @scena.Lambda('lambda_3705')
    def lambda_3705():
        OP_67(0, 500, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3705)

    @scena.Lambda('lambda_371D')
    def lambda_371D():
        OP_6E(360, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_371D)

    OP_6F(0x0000, 76)
    OP_70(0x0000, 95)
    OP_73(0x0000)
    OP_6F(0x0000, 170)
    OP_70(0x0000, 195)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 195)
    OP_70(0x0000, 215)
    Sleep(1500)

    SetMessageWindowPos(230, 280, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311239V所有守护利贝尔的\n',
            '士兵们请听着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311240V我名叫『雷格纳特』。\n',
            '是自古沉眠于此地的龙之眷族。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311241V之前虽然被恶人所控制，\n',
            '不过现已被游击士们解救。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311242V详细情况请向他们询问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    WaitForThreadExit(0x0101, 0x0000)
    OP_72(0x0000, 0x0020)
    OP_73(0x0000)

    @scena.Lambda('lambda_3868')
    def lambda_3868():
        OP_67(0, -1000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3868)

    @scena.Lambda('lambda_3880')
    def lambda_3880():
        ChrMoveToRelativeAsync(0x00FE, 100000, 100000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3880)

    OP_6F(0x0000, 575)
    OP_70(0x0000, 600)

    @scena.Lambda('lambda_38A9')
    def lambda_38A9():
        ChrSetDirection(0x000D, 315, 100)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_38A9)

    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 600)
    OP_70(0x0000, 620)
    CreateThread(0x000D, 0x00, 0x01, 0x0021)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    CameraMove(-120890, 30000, 45390, 0)
    OP_67(0, 34330, -10000, 0)
    CameraSetDistance(2280, 0)
    OP_6C(125000, 0)
    OP_6E(1200, 0)
    OP_0D()

    @scena.Lambda('lambda_391C')
    def lambda_391C():
        CameraSetDistance(2500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_391C)

    Sleep(6000)

    Fade(500)
    TerminateThread(0x000D, 0x03)
    CameraMove(-27780, 3000, -200, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(54000, 0)
    OP_6E(262, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_0D()
    Sleep(1000)

    OP_63(0x000A)
    OP_63(0x000B)
    OP_63(0x000C)
    OP_63(0x0009)
    OP_E5(0x0A, 0x00, 0x01)
    OP_E5(0x09, 0x00, 0x01)
    OP_E5(0x0C, 0x00, 0x01)
    OP_E5(0x0B, 0x00, 0x01)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x000A,
        (
            '#0600311243V#161F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0280311244V#153F#5P啊啊……\n',
            '已经看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0270311245V#143F#2P请问……\n',
            '我们不用追上去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100311246V#176F#5P……到了那种高度\n',
            '我们就束手无策了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100311247V就算『埃尔赛尤』能上去，\n',
            '我们也会窒息的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600311248V#163F#5P真没办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311249V#165F这下可要彻彻底底\n',
            '向他们问个清楚才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_24(0x0079, 0x50)
    OP_24(0x0125, 0x50)
    Sleep(200)

    OP_24(0x0079, 0x46)
    OP_24(0x0125, 0x46)
    Sleep(200)

    OP_24(0x0079, 0x3C)
    OP_24(0x0125, 0x3C)
    Sleep(200)

    OP_24(0x0079, 0x32)
    OP_24(0x0125, 0x32)
    Sleep(200)

    OP_24(0x0079, 0x28)
    OP_24(0x0125, 0x28)
    Sleep(200)

    OP_24(0x0079, 0x1E)
    OP_24(0x0125, 0x1E)
    Sleep(200)

    OP_23(0x0079)
    OP_23(0x0125)
    OP_0D()
    Sleep(1000)

    SetMessageWindowPos(-1, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，扰乱柏斯地区平静的\n',
            '古代龙骚动终于顺利落幕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人则向摩尔根将军\n',
            '报告了整个事件的详细经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在好不容易解脱之后，\n',
            '他们便将龙托付的金耀石结晶\n',
            '分别送交了市长和村长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '然后，一个星期过去了──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1202._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0x3CE0
@scena.Code('func_1F_3CE0')
def func_1F_3CE0():
    Sleep(200)

    PlaySE(288, 0x00, 0x64)
    Sleep(1000)

    PlaySE(288, 0x00, 0x64)
    Sleep(1000)

    PlaySE(288, 0x00, 0x64)
    Sleep(1500)

    PlaySE(288, 0x00, 0x64)
    Sleep(1600)

    PlaySE(288, 0x00, 0x64)
    Sleep(1500)

    PlaySE(288, 0x00, 0x64)
    Sleep(1800)

    def _loc_3D21(): pass

    label('loc_3D21')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D37',
    )

    PlaySE(288, 0x00, 0x64)
    Sleep(1300)

    Jump('loc_3D21')

    def _loc_3D37(): pass

    label('loc_3D37')

    Return()

# id: 0x0020 offset: 0x3D38
@scena.Code('func_20_3D38')
def func_20_3D38():
    @scena.Lambda('lambda_3D3E')
    def lambda_3D3E():
        ChrMoveTo(0x00FE, -80000, 3000, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3D3E)

    Sleep(900)

    @scena.Lambda('lambda_3D5E')
    def lambda_3D5E():
        ChrMoveTo(0x00FE, -80000, 3000, 0, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3D5E)

    Sleep(800)

    @scena.Lambda('lambda_3D7E')
    def lambda_3D7E():
        ChrMoveTo(0x00FE, -80000, 3000, 0, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3D7E)

    Sleep(700)

    @scena.Lambda('lambda_3D9E')
    def lambda_3D9E():
        ChrMoveTo(0x00FE, -80000, 3000, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3D9E)

    Sleep(500)

    @scena.Lambda('lambda_3DBE')
    def lambda_3DBE():
        ChrMoveTo(0x00FE, -80000, 3000, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3DBE)

    Sleep(400)

    @scena.Lambda('lambda_3DDE')
    def lambda_3DDE():
        ChrMoveTo(0x00FE, -80000, 3000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3DDE)

    Sleep(300)

    @scena.Lambda('lambda_3DFE')
    def lambda_3DFE():
        ChrMoveTo(0x00FE, -80000, 3000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3DFE)

    WaitForThreadExit(0x000D, 0x0001)

    Return()

# id: 0x0021 offset: 0x3E19
@scena.Code('func_21_3E19')
def func_21_3E19():
    @scena.Lambda('lambda_3E1F')
    def lambda_3E1F():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3E1F)

    Sleep(200)

    @scena.Lambda('lambda_3E3F')
    def lambda_3E3F():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3E3F)

    Sleep(200)

    @scena.Lambda('lambda_3E5F')
    def lambda_3E5F():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3E5F)

    Sleep(200)

    @scena.Lambda('lambda_3E7F')
    def lambda_3E7F():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3E7F)

    Sleep(200)

    @scena.Lambda('lambda_3E9F')
    def lambda_3E9F():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3E9F)

    Sleep(200)

    @scena.Lambda('lambda_3EBF')
    def lambda_3EBF():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3EBF)

    Sleep(200)

    @scena.Lambda('lambda_3EDF')
    def lambda_3EDF():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3EDF)

    Sleep(200)

    @scena.Lambda('lambda_3EFF')
    def lambda_3EFF():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3EFF)

    Sleep(200)

    @scena.Lambda('lambda_3F1F')
    def lambda_3F1F():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3F1F)

    Sleep(200)

    @scena.Lambda('lambda_3F3F')
    def lambda_3F3F():
        ChrMoveTo(0x00FE, -260000, 250000, 160000, 36000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3F3F)

    Return()

# id: 0x0022 offset: 0x3F55
@scena.Code('func_22_3F55')
def func_22_3F55():
    @scena.Lambda('lambda_3F5B')
    def lambda_3F5B():
        ChrMoveTo(0x00FE, -100000, 0, 25000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3F5B)

    Sleep(200)

    @scena.Lambda('lambda_3F7B')
    def lambda_3F7B():
        ChrMoveTo(0x00FE, -100000, 0, -25000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3F7B)

    Sleep(500)

    @scena.Lambda('lambda_3F9B')
    def lambda_3F9B():
        ChrMoveTo(0x00FE, -55000, 0, 25000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3F9B)

    Sleep(200)

    @scena.Lambda('lambda_3FBB')
    def lambda_3FBB():
        ChrMoveTo(0x00FE, -55000, 0, -25000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3FBB)

    WaitForThreadExit(0x000F, 0x0001)

    @scena.Lambda('lambda_3FDB')
    def lambda_3FDB():
        OP_D1(0x00FE, 0, 45000, 0, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3FDB)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_3FFA')
    def lambda_3FFA():
        OP_D1(0x00FE, 0, 135000, 0, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3FFA)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_4019')
    def lambda_4019():
        OP_D1(0x00FE, 0, 135000, 0, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_4019)

    WaitForThreadExit(0x0012, 0x0001)

    @scena.Lambda('lambda_4038')
    def lambda_4038():
        OP_D1(0x00FE, 0, 45000, 0, 1000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_4038)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
