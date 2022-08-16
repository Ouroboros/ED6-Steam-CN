import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1502_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1502_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R1502.x'
    header.mapIndex       = 59
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_592',
    )

    EventBegin(0x00)
    PlaySE(133, 0x01, 0x55)
    ChrSetPos(0x0008, -75050, -2009, -3930, 106)
    ChrTurnDirection(0x0000, 0x0008, 0)
    ChrTurnDirection(0x0001, 0x0008, 0)
    ChrTurnDirection(0x0002, 0x0008, 0)
    Sleep(300)

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    LoadEffect(0x00, 'map\\\\mp023_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -75080, -50, -3790, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0101, -71140, -60, -3530, 290)
    ChrSetPos(0x0103, -70970, -20, -4830, 290)
    ChrSetPos(0x0102, -69490, -80, -4330, 290)
    ChrSetChipByIndex(0x0103, 5)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0101, 3)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_019E')
    def lambda_019E():
        OP_6C(250000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_019E)

    @scena.Lambda('lambda_01AE')
    def lambda_01AE():
        CameraMove(-75050, 10, -3930, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_01AE)

    Sleep(3000)

    @scena.Lambda('lambda_01CB')
    def lambda_01CB():
        CameraSetDistance(2800, 6000)

        ExitThread()

    DispatchAsync(0x0002, 0x0002, lambda_01CB)

    @scena.Lambda('lambda_01DB')
    def lambda_01DB():
        OP_67(0, 6510, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0002, 0x0003, lambda_01DB)

    OP_24(0x0085, 0x64)
    PlayEffect(0x00, 0x01, 0x00FF, -75080, -50, -3790, 0, 0, 0, 600, 600, 600, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_022C')
    def lambda_022C():
        ChrMoveTo(0x0008, -75050, 10, -3930, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_022C)

    @scena.Lambda('lambda_0247')
    def lambda_0247():
        ChrSetRGBAMask(0x0008, 255, 255, 255, 255, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0247)

    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    StopEffect(0x01, 0x02)
    StopEffect(0x00, 0x02)
    OP_24(0x0085, 0x50)
    Sleep(1000)

    OP_6A(0x0008)
    CreateThread(0x0008, 0x00, 0x01, 0x0001)
    Sleep(200)

    Sleep(800)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    OP_6A(0x0000)
    MapClearFlags(0x00000001)
    OP_23(0x0085)
    StopEffect(0x00, 0x02)
    OP_84(0x00)
    Battle(0x000003EE, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2CA'),
        (-1, 'loc_2CD'),
    )

    def _loc_2CA(): pass

    label('loc_2CA')

    OP_B4(0x00)

    Return()

    def _loc_2CD(): pass

    label('loc_2CD')

    EventBegin(0x00)
    OP_66(0x0001)
    CameraMove(-71660, -90, -2720, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -72450, -70, -2130, 315)
    ChrSetPos(0x0103, -71630, -90, -4019, 315)
    ChrSetPos(0x0102, -70980, 10, -2250, 315)
    ChrSetFlags(0x0008, 0x0080)
    OP_0D()
    Sleep(400)

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151458V#004F呼～好险啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151459V没想到它会在这种地方出现……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_03B9')
    def lambda_03B9():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03B9)

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151460V#022F看来是依靠我们的脚步声\n',
            '来展开攻击的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151461V真是趁人不备，突然袭击啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151462V#012F如果村里的人被它袭击可就糟了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151463V幸好及时消灭掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151464V#020F是啊，确实是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151465V那我们这就回去向村长报告情况吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151466V#010F嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151467V#000F好的，我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x000E, 0x04, 0x10)
    OP_28(0x000E, 0x01, 0x0008)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【搜寻山道的魔兽】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    def _loc_592(): pass

    label('loc_592')

    Return()

# id: 0x0001 offset: 0x593
@scena.Code('func_01_593')
def func_01_593():
    ChrSetChipByIndex(0x0008, 2)
    PlaySE(571, 0x00, 0x64)
    OP_24(0x0085, 0x46)

    @scena.Lambda('lambda_05A7')
    def lambda_05A7():
        ChrJumpTo(0x0008, -78350, -80, -3400, 1000, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_05A7)

    @scena.Lambda('lambda_05C5')
    def lambda_05C5():
        CameraSetDistance(3500, 3000)

        ExitThread()

    DispatchAsync(0x0002, 0x0002, lambda_05C5)

    OP_99(0x0008, 0x00, 0x00, 0)
    Sleep(20)

    OP_99(0x0008, 0x01, 0x01, 0)
    Sleep(20)

    OP_99(0x0008, 0x02, 0x02, 0)
    Sleep(20)

    OP_99(0x0008, 0x03, 0x03, 0)
    WaitForThreadExit(0x0008, 0x0003)
    OP_99(0x0008, 0x00, 0x00, 0)
    PlaySE(571, 0x00, 0x64)
    OP_24(0x0085, 0x46)

    @scena.Lambda('lambda_061F')
    def lambda_061F():
        ChrJumpTo(0x0008, -77670, 2000, -820, 2200, 14000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_061F)

    OP_99(0x0008, 0x00, 0x00, 0)
    Sleep(20)

    OP_99(0x0008, 0x01, 0x01, 0)
    Sleep(20)

    OP_99(0x0008, 0x02, 0x02, 0)
    Sleep(20)

    OP_99(0x0008, 0x03, 0x03, 0)
    WaitForThreadExit(0x0008, 0x0003)
    OP_99(0x0008, 0x00, 0x00, 0)
    PlaySE(571, 0x00, 0x64)
    OP_24(0x0085, 0x3C)

    @scena.Lambda('lambda_0687')
    def lambda_0687():
        ChrJumpTo(0x0008, -71660, 5000, -3000, 5200, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0687)

    OP_99(0x0008, 0x00, 0x00, 0)
    Sleep(20)

    OP_99(0x0008, 0x01, 0x01, 0)
    Sleep(20)

    OP_99(0x0008, 0x02, 0x02, 0)
    Sleep(20)

    OP_99(0x0008, 0x03, 0x03, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
