import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import E0500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0500   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0500.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x547
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A1(0x0000, 0x0000)
    Event(0, 0x0002)

    Return()

# id: 0x0001 offset: 0xBB
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xBC
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0004)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrPos(0x0000, -33360, 29260, 37770, 155)
    SetMapFlags(0x00000001)
    OP_66(0x0000)
    PlaySE(121, 0x00, 0x64)
    OP_24(0x0079, 0x46)
    CameraMove(-33360, 29260, 37770, 0)
    OP_67(-36960, 15020, -20740, 0)
    CameraSetDistance(1730, 0)
    OP_6C(3000, 0)
    OP_6E(697, 0)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 700)
    OP_70(0x0000, 780)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0158')
    def lambda_0158():
        SetChrDirection(0x00FE, 205, 10)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0158)

    @scena.Lambda('lambda_0166')
    def lambda_0166():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0166)

    Sleep(400)

    @scena.Lambda('lambda_0186')
    def lambda_0186():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0186)

    Sleep(400)

    OP_24(0x0079, 0x4B)

    @scena.Lambda('lambda_01AA')
    def lambda_01AA():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_01AA)

    Sleep(800)

    OP_24(0x0079, 0x50)

    @scena.Lambda('lambda_01CE')
    def lambda_01CE():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_01CE)

    Sleep(800)

    OP_24(0x0079, 0x55)

    @scena.Lambda('lambda_01F2')
    def lambda_01F2():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_01F2)

    Sleep(1100)

    OP_24(0x0079, 0x5A)

    @scena.Lambda('lambda_0216')
    def lambda_0216():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0216)

    Sleep(100)

    @scena.Lambda('lambda_0236')
    def lambda_0236():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0236)

    Sleep(100)

    @scena.Lambda('lambda_0256')
    def lambda_0256():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0256)

    Sleep(100)

    @scena.Lambda('lambda_0276')
    def lambda_0276():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0276)

    Sleep(100)

    @scena.Lambda('lambda_0296')
    def lambda_0296():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0296)

    @scena.Lambda('lambda_02B1')
    def lambda_02B1():
        SetChrDirection(0x00FE, 285, 10)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_02B1)

    Sleep(100)

    @scena.Lambda('lambda_02C4')
    def lambda_02C4():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_02C4)

    @scena.Lambda('lambda_02DF')
    def lambda_02DF():
        SetChrDirection(0x00FE, 285, 8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_02DF)

    Sleep(100)

    @scena.Lambda('lambda_02F2')
    def lambda_02F2():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_02F2)

    @scena.Lambda('lambda_030D')
    def lambda_030D():
        SetChrDirection(0x00FE, 285, 6)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_030D)

    Sleep(100)

    @scena.Lambda('lambda_0320')
    def lambda_0320():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0320)

    @scena.Lambda('lambda_033B')
    def lambda_033B():
        SetChrDirection(0x00FE, 285, 4)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_033B)

    Sleep(100)

    @scena.Lambda('lambda_034E')
    def lambda_034E():
        ChrMoveTo(0x0000, -26830, 29260, -7290, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_034E)

    @scena.Lambda('lambda_0369')
    def lambda_0369():
        SetChrDirection(0x00FE, 285, 2)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0369)

    Sleep(100)

    @scena.Lambda('lambda_037C')
    def lambda_037C():
        SetChrDirection(0x00FE, 285, 10)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_037C)

    TerminateThread(0x0000, 0x02)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 1021)
    OP_70(0x0000, 1050)
    OP_73(0x0000)
    OP_6F(0x0000, 1051)
    OP_70(0x0000, 1110)

    @scena.Lambda('lambda_03B2')
    def lambda_03B2():
        SetChrDirection(0x00FE, -19536, 1)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_03B2)

    OP_66(0x0001)

    @scena.Lambda('lambda_03C3')
    def lambda_03C3():
        OP_67(0, -7220, -17030, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_03C3)

    @scena.Lambda('lambda_03DB')
    def lambda_03DB():
        OP_6C(22000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_03DB)

    OP_24(0x0079, 0x64)

    @scena.Lambda('lambda_03EF')
    def lambda_03EF():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_03EF)

    Sleep(100)

    @scena.Lambda('lambda_040F')
    def lambda_040F():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_040F)

    Sleep(100)

    @scena.Lambda('lambda_042F')
    def lambda_042F():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_042F)

    Sleep(100)

    @scena.Lambda('lambda_044F')
    def lambda_044F():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_044F)

    Sleep(100)

    @scena.Lambda('lambda_046F')
    def lambda_046F():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_046F)

    Sleep(100)

    @scena.Lambda('lambda_048F')
    def lambda_048F():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_048F)

    Sleep(700)

    @scena.Lambda('lambda_04AF')
    def lambda_04AF():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_04AF)

    Sleep(800)

    @scena.Lambda('lambda_04CF')
    def lambda_04CF():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_04CF)

    Sleep(900)

    @scena.Lambda('lambda_04EF')
    def lambda_04EF():
        ChrMoveTo(0x0000, -26830, -29260, -8290, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_04EF)

    FadeOut(2000, 0, -1)
    Sleep(1000)

    @scena.Lambda('lambda_0519')
    def lambda_0519():
        ChrMoveTo(0x0000, -26830, -129259, -8290, 17000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0519)

    OP_0D()
    SetMapFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
