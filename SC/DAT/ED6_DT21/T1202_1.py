import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1202_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1202_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1202_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    FadeOut(0, 0, -1)
    FormationDelMember(0x46, 0xFF)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0016, -1350, 0, 6540, 0)
    ChrSetPos(0x0101, -1550, 0, 5470, 0)
    ChrSetPos(0x00F7, -2700, 0, 5320, 0)
    ChrSetPos(0x00F8, -1170, 0, 4200, 0)
    ChrSetPos(0x00F9, -2410, 0, 3740, 0)
    CreateThread(0x0016, 0x00, 0x01, 0x0001)
    Sleep(100)

    CreateThread(0x0101, 0x00, 0x01, 0x0002)
    Sleep(100)

    CreateThread(0x00F7, 0x00, 0x01, 0x0003)
    Sleep(100)

    CreateThread(0x00F8, 0x00, 0x01, 0x0004)
    Sleep(100)

    CreateThread(0x00F9, 0x00, 0x01, 0x0005)
    CameraMove(-1980, 0, 8520, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3240, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_018B')
    def lambda_018B():
        CameraMove(-1190, 0, 12330, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_018B)

    FadeIn(2000, 0)
    Sleep(5000)

    @scena.Lambda('lambda_01B1')
    def lambda_01B1():
        CameraMove(21820, -4000, 13880, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_01B1)

    @scena.Lambda('lambda_01C9')
    def lambda_01C9():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_01C9)

    @scena.Lambda('lambda_01D9')
    def lambda_01D9():
        OP_67(0, 8990, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_01D9)

    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_01F6')
    def lambda_01F6():
        OP_6C(0, 14000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_01F6)

    CameraSetDistance(4000, 4000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Fade(1000)
    TerminateThread(0x0101, 0x03)
    ChrSetPos(0x0016, 8570, 0, 9930, 90)
    ChrSetPos(0x0101, 6990, 0, 9850, 92)
    ChrSetPos(0x00F7, 6630, 0, 11050, 96)
    ChrSetPos(0x00F8, 6210, 0, 9160, 89)
    ChrSetPos(0x00F9, 5490, 0, 10320, 93)
    CameraMove(6600, 0, 10880, 0)
    OP_67(0, 6110, -10000, 0)
    CameraSetDistance(3240, 0)
    OP_6C(308000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0016,
        (
            '#3710490120V原来如此，消息真灵通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490121V果树园那边\n',
            '总算也开始重建了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38E',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490122V#1060F嗯，看来是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490123V虽然重建工作很艰苦，\n',
            '不过千里之行始于足下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_552')

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490124V#051F嗯，重建工作很艰苦，\n',
            '不过已经迈出了重要的第一步呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_552')

    def _loc_3E9(): pass

    label('loc_3E9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490125V#020F虽然重建不易，\n',
            '不过已经迈出了重要的第一步呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_552')

    def _loc_43E(): pass

    label('loc_43E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4BD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490126V#070F嗯，虽然重建十分艰苦，\n',
            '不过已经迈出了重要的第一步呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490127V千里之行始于足下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_552')

    def _loc_4BD(): pass

    label('loc_4BD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_552',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490128V#030F嗯，虽然重建工作艰苦，\n',
            '不过已经迈出了重要的第一步呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490129V无论田地如何荒芜，\n',
            '播撒种子后才有可能有收获。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_552(): pass

    label('loc_552')

    ChrTalk(
        0x0101,
        (
            '#0010490130V#1000F嗯，也有各种形式的\n',
            '援助到村子里来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490131V一定能把村子恢复原状的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490132V嗯，我相信这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490133V我们这些商人\n',
            '也会想办法为大家出力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010490134V#1011F啊，莫非……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490135V米拉诺小姐也是来\n',
            '支援村子的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490136V想这么愚蠢的事\n',
            '是会遭报应的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490137V我来这里根本上\n',
            '就是为了做生意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490138V总之我先确认了一下\n',
            '果树园的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490139V当然，有必要的话\n',
            '我也准备进行『投资』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0016, 270, 400)

    ChrTalk(
        0x0016,
        (
            '#3710490140V──那我就先去\n',
            '忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490141V#1006F啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490142V那就在这里告别吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490143V嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushValueByIndex, 0x15),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F5',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7F5',
    )

    OP_28(0x007C, 0x01, 0x0010)
    OP_2B(0x007C, 0x0002)
    OP_2C(0x007C, 0x1388)

    def _loc_7F5(): pass

    label('loc_7F5')

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_8D8',
    )

    ChrTalk(
        0x0016,
        (
            '#3710490144V你们的本事……\n',
            '很不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490145V我已经通知协会\n',
            '给你们额外奖励了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490146V#1004F啊，真的吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490147V我干吗要撒\n',
            '这种谎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490148V总之，你们就期待着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_942')

    def _loc_8D8(): pass

    label('loc_8D8')

    ChrTalk(
        0x0016,
        (
            '#3710490149V嗯，你们也算\n',
            '干得不错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#3710490150V虽然还没到值得给予\n',
            '额外奖励的程度，有点遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_942(): pass

    label('loc_942')

    ChrTalk(
        0x0016,
        (
            '#3710490151V那么再见了，回去的\n',
            '路上要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490152V#1006F您也努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_099F')
    def lambda_099F():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_099F')

    DispatchAsync2(0x0000, 0x0001, lambda_099F)

    @scena.Lambda('lambda_09B0')
    def lambda_09B0():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_09B0')

    DispatchAsync2(0x0001, 0x0001, lambda_09B0)

    @scena.Lambda('lambda_09C1')
    def lambda_09C1():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_09C1')

    DispatchAsync2(0x0002, 0x0001, lambda_09C1)

    @scena.Lambda('lambda_09D2')
    def lambda_09D2():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_09D2')

    DispatchAsync2(0x0003, 0x0001, lambda_09D2)

    CreateThread(0x0016, 0x00, 0x01, 0x0006)
    CameraMove(4800, 0, 14700, 3000)
    Sleep(1000)

    CameraMove(6600, 0, 10880, 2500)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(23, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【护送商人】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    OP_28(0x007C, 0x01, 0x0008)
    OP_28(0x007C, 0x04, 0x10)
    TerminateThread(0x0016, 0x00)
    ChrSetPos(0x0016, 25990, -4000, 14870, 270)
    CreateThread(0x0016, 0x00, 0x00, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0xA96
@scena.Code('func_01_A96')
def func_01_A96():
    ChrWalkTo(0x0016, -1350, 0, 13230, 2000, 0x00)
    ChrSetDirection(0x0016, 180, 400)
    Sleep(1000)

    ChrSetDirection(0x0016, 90, 400)
    Sleep(1000)

    OP_94(0x01, 0x0016, 0x000F, 0x00000FA0, 0x000007D0, 0x00)

    Return()

# id: 0x0002 offset: 0xAD2
@scena.Code('func_02_AD2')
def func_02_AD2():
    ChrWalkTo(0x0101, -1550, 0, 11580, 2000, 0x00)
    Sleep(2500)

    ChrSetDirection(0x0101, 90, 400)
    Sleep(2000)

    OP_A6(0x000C)
    OP_94(0x01, 0x0101, 0x0000, 0x00000BB8, 0x000007D0, 0x00)

    Return()

# id: 0x0003 offset: 0xB0A
@scena.Code('func_03_B0A')
def func_03_B0A():
    ChrWalkTo(0x00F7, -2700, 0, 11190, 2000, 0x00)
    Sleep(2500)

    ChrSetDirection(0x00F7, 90, 400)
    Sleep(2000)

    OP_A6(0x000C)
    OP_94(0x01, 0x00F7, 0x0000, 0x00000BB8, 0x000007D0, 0x00)

    Return()

# id: 0x0004 offset: 0xB42
@scena.Code('func_04_B42')
def func_04_B42():
    ChrWalkTo(0x00F8, -1170, 0, 10550, 2000, 0x00)
    Sleep(2500)

    ChrSetDirection(0x00F8, 90, 400)
    Sleep(2000)

    OP_A6(0x000C)
    OP_94(0x01, 0x00F8, 0x0000, 0x00000BB8, 0x000007D0, 0x00)

    Return()

# id: 0x0005 offset: 0xB7A
@scena.Code('func_05_B7A')
def func_05_B7A():
    ChrWalkTo(0x00F9, -2410, 0, 10040, 2000, 0x00)
    Sleep(2500)

    ChrSetDirection(0x00F9, 90, 400)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    OP_94(0x01, 0x00F9, 0x0000, 0x00000BB8, 0x000007D0, 0x00)

    Return()

# id: 0x0006 offset: 0xBB2
@scena.Code('func_06_BB2')
def func_06_BB2():
    ChrWalkTo(0x0016, 5730, 0, 13910, 2000, 0x00)
    ChrWalkTo(0x0016, 260, 0, 28220, 2000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
