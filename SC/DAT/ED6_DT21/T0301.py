import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0301   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0301.x'
    header.mapIndex       = 15
    header.bgm            = 84
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
            dword_00        = 0x000007D0,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFE890,
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
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00002580,
            dword_04        = 0x0000036B,
            dword_08        = 0x0000012C,
            word_0C         = 0x0004,
            word_0E         = 0x0076,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00002580,
            dword_04        = 0x0000036B,
            dword_08        = 0x0000012C,
            word_0C         = 0x0004,
            word_0E         = 0x0076,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00002580,
            dword_04        = 0x0000036B,
            dword_08        = 0x0000012C,
            word_0C         = 0x0004,
            word_0E         = 0x0076,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0x174
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x174
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾利兹街道方向',
            x                   = 4110,
            z                   = -1000,
            y                   = -46140,
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

# id: 0x10002 offset: 0x194
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x194
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x194
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x194
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -125000, -133000, 2293763)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1BC',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_02_1EE)

    Jump('loc_1D4')

    def _loc_1BC(): pass

    label('loc_1BC')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 0, 0x1818)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D4',
    )

    Event(0, func_03_2BC)

    def _loc_1D4(): pass

    label('loc_1D4')

    Return()

# id: 0x0001 offset: 0x1D5
@scena.Code('func_01_1D5')
def func_01_1D5():
    MapSetFlags(0x00000010)
    OP_11(0x4B, 0x4B, 0x96, 0, 60000, 0)
    StopEffect(0x80, 0x02)

    Return()

# id: 0x0002 offset: 0x1EE
@scena.Code('func_02_1EE')
def func_02_1EE():
    EventBegin(0x00)
    OP_11(0x4B, 0x4B, 0x96, 0, 70000, 0)
    CameraMove(-9230, 0, 8720, 0)
    OP_67(0, 9280, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(39000, 0)
    OP_6E(334, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_024C')
    def lambda_024C():
        CameraMove(4580, 450, 4260, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_024C)

    @scena.Lambda('lambda_0264')
    def lambda_0264():
        OP_67(0, 7240, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0264)

    OP_6C(25000, 8000)

    @scena.Lambda('lambda_0285')
    def lambda_0285():
        CameraSetDistance(3500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0285)

    @scena.Lambda('lambda_0295')
    def lambda_0295():
        OP_6E(275, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0295)

    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0311._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x2BC
@scena.Code('func_03_2BC')
def func_03_2BC():
    EventBegin(0x00)
    ChrSetPos(0x0101, -1820, 3450, 860, 270)
    CameraMove(-3930, 3450, 850, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 59)
    OP_73(0x0002)
    Sleep(500)

    ChrWalkTo(0x0101, -3690, 3450, 1080, 1500, 0x00)
    OP_72(0x0002, 0x0800)
    OP_6F(0x0002, 59)
    OP_70(0x0002, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)

    @scena.Lambda('lambda_0366')
    def lambda_0366():
        CameraMove(-6160, 3450, 1600, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0366)

    ChrWalkTo(0x0101, -6490, 3450, 1670, 1500, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    OP_71(0x0002, 0x0800)

    ChrTalk(
        0x0101,
        (
            '#0010290168V#1335F唉……\n',
            '还是这么大的雾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290169V#452F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT24/C_VIS172._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    Sleep(2000)

    OP_AE(0x000001F4)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290170V#1336F好了……\n',
            '确认１层吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_71(0x0002, 0x0010)
    SetScenaFlags(ScenaFlag(0x0303, 0, 0x1818))
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
