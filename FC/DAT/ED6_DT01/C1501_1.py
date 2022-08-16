import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1501_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1501_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C1501.x'
    header.mapIndex       = 61
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
    Return()

# id: 0x0001 offset: 0x65
@scena.Code('func_01_65')
def func_01_65():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Or,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7D',
    )

    Return()

    def _loc_7D(): pass

    label('loc_7D')

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20A7',
    )

    OP_28(0x001F, 0x01, 0x4000)
    OP_28(0x001F, 0x04, 0x08)
    MapClearFlags(0x00000001)
    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB',
    )

    ChrTurnDirection(0x0101, 0x0008, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010160586V#004F啊…………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18E')

    def _loc_EB(): pass

    label('loc_EB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13B',
    )

    ChrTurnDirection(0x0102, 0x0008, 0)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0102,
        (
            '#0020160587V#014F那是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18E')

    def _loc_13B(): pass

    label('loc_13B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18E',
    )

    ChrTurnDirection(0x0105, 0x0008, 0)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0105,
        (
            '#0060160588V#044F那、那是…………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18E(): pass

    label('loc_18E')

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_01A8')
    def lambda_01A8():
        CameraMove(-101100, 3350, 66300, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_01A8)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_01D2')
    def lambda_01D2():
        ChrWalkTo(0x0008, -101100, 3350, 66300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_01D2)

    @scena.Lambda('lambda_01ED')
    def lambda_01ED():
        ChrWalkTo(0x0009, -101300, 3350, 66200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_01ED)

    @scena.Lambda('lambda_0208')
    def lambda_0208():
        ChrWalkTo(0x000A, -101100, 3350, 65900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0208)

    @scena.Lambda('lambda_0223')
    def lambda_0223():
        ChrWalkTo(0x000B, -101200, 3350, 66500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0223)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0105, 0x0040)

    @scena.Lambda('lambda_0252')
    def lambda_0252():
        ChrWalkTo(0x0101, -96100, 4000, 73700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0252)

    @scena.Lambda('lambda_026D')
    def lambda_026D():
        ChrWalkTo(0x0102, -95100, 4000, 74700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_026D)

    @scena.Lambda('lambda_0288')
    def lambda_0288():
        ChrWalkTo(0x0105, -94100, 4000, 75700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0288)

    ChrSetDirection(0x0008, 0, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)
    ChrSetDirection(0x0008, 180, 400)
    CreateThread(0x0008, 0x01, 0x01, 0x0002)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_02DE')
    def lambda_02DE():
        ChrWalkTo(0x0009, -103900, 2100, 63700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_02DE)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_02FE')
    def lambda_02FE():
        ChrWalkTo(0x000A, -102300, 2500, 64000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_02FE)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_031E')
    def lambda_031E():
        ChrWalkTo(0x000B, -101000, 2650, 63200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_031E)

    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_0343')
    def lambda_0343():
        ChrWalkTo(0x0009, -103900, 2100, 59900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0343)

    @scena.Lambda('lambda_035E')
    def lambda_035E():
        ChrWalkTo(0x0101, -101700, 2400, 63500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_035E)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_037E')
    def lambda_037E():
        ChrWalkTo(0x000A, -103000, 2100, 61200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_037E)

    @scena.Lambda('lambda_0399')
    def lambda_0399():
        ChrWalkTo(0x0102, -102800, 2600, 64599, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0399)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_03B9')
    def lambda_03B9():
        ChrWalkTo(0x000B, -100800, 2230, 61000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_03B9)

    @scena.Lambda('lambda_03D4')
    def lambda_03D4():
        ChrWalkTo(0x0105, -101200, 3100, 65500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_03D4)

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 0)
    ChrSetChipByIndex(0x0101, 3)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0444')
    def lambda_0444():
        OP_69(0x000C, 800)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0444)

    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0008, 0)
    ChrSetChipByIndex(0x0102, 5)
    WaitForThreadExit(0x0105, 0x0001)
    ChrTurnDirection(0x0105, 0x0008, 0)
    ChrSetChipByIndex(0x0105, 7)
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#1070160589V哇、哇～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1070160590V救、救救我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160591V#005F约修亚，我们上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160592V#012F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetFlags(0x0105, 0x1000)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0105, 8)

    @scena.Lambda('lambda_0513')
    def lambda_0513():
        OP_94(0x01, 0x0101, 0x0000, 0x000002BC, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0513)

    @scena.Lambda('lambda_0529')
    def lambda_0529():
        OP_94(0x01, 0x0102, 0x0000, 0x000002BC, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0529)

    @scena.Lambda('lambda_053F')
    def lambda_053F():
        OP_94(0x01, 0x0105, 0x0000, 0x000002BC, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_053F)

    Sleep(400)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Battle(0x000003F4, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    FormationAddMember(0x36, 0x03)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)
    ChrSetChipByIndex(0x0105, 7)
    ChrSetPos(0x0101, -101700, 2400, 63500, 180)
    ChrSetPos(0x0102, -104300, 2000, 63100, 180)
    ChrSetPos(0x0105, -102900, 2500, 64200, 180)
    ChrSetPos(0x0137, -102260, 1950, 58980, 356)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000C, 0)
    OP_6C(265000, 0)
    OP_0D()
    ChrSetChipByIndex(0x0105, 65535)
    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160593V#043F呼……\n',
            '我们总算是赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_0694')
    def lambda_0694():
        ChrTurnDirection(0x0102, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0694)

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160594V#002F是啊，\n',
            '真是千钧一发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160595V#010F您没有受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0706')
    def lambda_0706():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0706)

    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1070160596V嗯，我没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0778')
    def lambda_0778():
        OP_69(0x000C, 800)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0778)

    ChrWalkTo(0x0137, -103000, 2100, 61600, 2000, 0x00)
    WaitForThreadExit(0x0137, 0x0001)
    TalkBegin(0x0137)
    ChrTurnDirection(0x0137, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_11A4',
    )

    OP_28(0x001F, 0x01, 0x0008)
    OP_28(0x001F, 0x01, 0x0010)

    ChrTalk(
        0x0137,
        (
            '#1070160597V多亏了你们，\n',
            '我没有受一点伤…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160598V………………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160599V我好像…………\n',
            '在哪里见过你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0137, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160600V#000F咦，这么说来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0137, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0137,
        (
            '#1070160601V哦，想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160602V你不就是洛连特的\n',
            '那个小村姑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160603V#004F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160604V#005F你、你是那个\n',
            '寻找蘑菇的大奸商！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160605V#018F艾丝蒂尔……\n',
            '不要太失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0137, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160606V还是和以前一样，\n',
            '连最基本的礼貌都不懂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160607V真是的，\n',
            '这就是在乡下长大的关系吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160608V#009F胡、胡说八道～\n',
            '你自己才是个怪异食材的收集狂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160609V反正这次也肯定是\n',
            '为了找那些奇怪的食物吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160610V哼，\n',
            '今天我已经采集到了珍贵的野菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160611V跟你说，\n',
            '这种野菜可是比『荧光菇』\n',
            '更有个性的食材哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160612V哼哼，\n',
            '这次的生意一定会很顺利的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160613V#004F哎呀呀？\n',
            '『这次的』一定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160614V#507F那个叫『荧光菇』的东西\n',
            '果然没有卖出去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0137, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0137,
        (
            '#1070160615V胡、胡说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160616V只、只是\n',
            '碰巧没人需要罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160617V#044F啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160618V听到和野菜有关的事情，\n',
            '你有没有想起什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160619V#505F嗯，听你这么一说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160620V#010F是和玛诺利亚村的\n',
            '阿梅莉娅小姐有关的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0102, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160621V你说阿梅莉娅？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160622V我的侄女\n',
            '就叫做阿梅莉娅……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0137, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160623V#004F啊…………？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160624V……这么说，\n',
            '这个人就是阿梅莉娅小姐的叔父吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0137, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160625V#010F看来就是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0137, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160626V你们说什么？\n',
            '我侄女她怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160627V#010F实际上，\n',
            '就是阿梅莉娅小姐\n',
            '委托我们为您做护卫的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160628V可是当我们到达玛诺利亚村时，\n',
            '您已经出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160629V……嗯，是这样啊。\n',
            '的确是让阿梅莉娅担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160630V可是，我也没有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160631V为了下次的生意，\n',
            '我好歹也要准备一些礼品嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160632V#002F可是就为了这种荒唐的事，\n',
            '你差一点就成为\n',
            '危险魔兽的食物了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160633V如果变成那样，\n',
            '做生意什么的也就毫无意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0101, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160634V…………唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160635V#002F回去后好好地\n',
            '向阿梅莉娅小姐道歉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160636V她现在一定很担心你的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160637V…………嗯，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160638V等这回在格兰赛尔的\n',
            '生意做完之后，\n',
            '我保证好好向她道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160639V#010F嗯，\n',
            '我也觉得应该这样做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160640V…………那么，\n',
            '我们这就出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160641V把您送回村子里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0102, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160642V哦，那太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160643V回去的路上就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_208C')

    def _loc_11A4(): pass

    label('loc_11A4')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_19E7',
    )

    OP_28(0x001F, 0x01, 0x0008)
    OP_28(0x001F, 0x01, 0x0010)

    ChrTalk(
        0x0137,
        (
            '#1070160597V多亏了你们，\n',
            '我没有受一点伤…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160645V…………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160599V我好像…………\n',
            '在哪里见过你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0137, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_12F7',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160603V#004F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160604V#005F你、你是那个\n',
            '寻找蘑菇的大奸商！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160605V#018F艾丝蒂尔……\n',
            '不要太失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0137, 400)

    Jump('loc_1318')

    def _loc_12F7(): pass

    label('loc_12F7')

    ChrTalk(
        0x0101,
        (
            '#0010160650V#004F哎，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1318(): pass

    label('loc_1318')

    OP_62(0x0137, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0137,
        (
            '#1070160601V哦，想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160652V你们不就是\n',
            '我在洛连特见过的游击士吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0137, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160653V#010F很久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160654V工作还顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0102, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160655V唔，\n',
            '今天也采到了贵重的野菜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160656V跟你说，\n',
            '这种野菜可是比『荧光菇』\n',
            '更有个性的食材哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160657V这次的商谈\n',
            '肯定会进行得很顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160617V#044F啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160618V听到和野菜有关的事情，\n',
            '你有没有想起什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160619V#505F嗯，听你这么一说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160620V#010F是和玛诺利亚村的\n',
            '阿梅莉娅小姐有关的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0102, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160621V你说阿梅莉娅？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160622V我的侄女\n',
            '就叫做阿梅莉娅……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0137, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160623V#004F啊…………？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160624V……这么说，\n',
            '这个人就是阿梅莉娅小姐的叔父吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0137, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160625V#010F看来就是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0137, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160626V你们说什么？\n',
            '我侄女她怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160627V#010F实际上，\n',
            '就是阿梅莉娅小姐\n',
            '委托我们为您做护卫的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160628V可是当我们到达玛诺利亚村时，\n',
            '您已经出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160629V……嗯，是这样啊。\n',
            '的确是让阿梅莉娅担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160630V可是，我也没有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160631V为了下次的生意，\n',
            '我好歹也要准备一些礼品嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160632V#002F可是就为了这种荒唐的事，\n',
            '你差一点就成为\n',
            '危险魔兽的食物了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160633V如果变成那样，\n',
            '做生意什么的也就毫无意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0101, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160634V…………唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160635V#002F回去后好好地\n',
            '向阿梅莉娅小姐道歉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160636V她现在一定很担心你的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160637V…………嗯，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160638V等这回在格兰赛尔的\n',
            '生意做完之后，\n',
            '我保证好好向她道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160639V#010F嗯，\n',
            '我也觉得应该这样做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160640V…………那么，\n',
            '我们这就出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160641V把您送回村子里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0102, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160642V哦，那太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160643V回去的路上就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_208C')

    def _loc_19E7(): pass

    label('loc_19E7')

    OP_28(0x001F, 0x01, 0x0020)
    OP_28(0x001F, 0x01, 0x0040)

    ChrTalk(
        0x0137,
        (
            '#1070160685V多亏了你们，\n',
            '我也毫发无伤呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160686V不愧是游击士，\n',
            '功夫真是厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0137, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160687V#501F那么，你在这种山路上\n',
            '到底是想干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160688V唔，\n',
            '我是专门收集高级食材的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160689V今天是为了\n',
            '寻找贵重的野菜\n',
            '才来这种地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160690V#044F野菜…………？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160691V啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160618V听到和野菜有关的事情，\n',
            '你有没有想起什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160619V#505F嗯，听你这么一说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160620V#010F是和玛诺利亚村的\n',
            '阿梅莉娅小姐有关的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0102, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160621V你说阿梅莉娅？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160622V我的侄女\n',
            '就叫做阿梅莉娅……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0137, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160623V#004F啊…………？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160624V……这么说，\n',
            '这个人就是阿梅莉娅小姐的叔父吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0137, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160625V#010F看来就是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0137, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160626V你们说什么？\n',
            '我侄女她怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160627V#010F实际上，\n',
            '就是阿梅莉娅小姐\n',
            '委托我们为您做护卫的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160628V可是当我们到达玛诺利亚村时，\n',
            '您已经出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160629V……嗯，是这样啊。\n',
            '的确是让阿梅莉娅担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160630V可是，我也没有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160631V为了下次的生意，\n',
            '我好歹也要准备一些礼品嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160632V#002F可是就为了这种荒唐的事，\n',
            '你差一点就成为\n',
            '危险魔兽的食物了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160633V如果变成那样，\n',
            '做生意什么的也就毫无意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0101, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160634V…………唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160635V#002F回去后好好地\n',
            '向阿梅莉娅小姐道歉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160636V她现在一定很担心你的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160637V…………嗯，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160638V等这回在格兰赛尔的\n',
            '生意做完之后，\n',
            '我保证好好向她道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160639V#010F嗯，\n',
            '我也觉得应该这样做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160640V…………那么，\n',
            '我们这就出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160641V把您送回村子里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0137, 0x0102, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160642V哦，那太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160643V回去的路上就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_208C(): pass

    label('loc_208C')

    ChrSetFlags(0x0008, 0x0080)
    ChrClearFlags(0x0137, 0x0004)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0102, 0x0040)
    ChrClearFlags(0x0137, 0x0040)
    EventEnd(0x00)

    def _loc_20A7(): pass

    label('loc_20A7')

    Return()

# id: 0x0002 offset: 0x20A8
@scena.Code('func_02_20A8')
def func_02_20A8():
    TerminateThread(0x000C, 0x01)

    @scena.Lambda('lambda_20B2')
    def lambda_20B2():
        CameraMove(-102000, 1930, 59600, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_20B2)

    ChrWalkTo(0x0008, -102200, 2500, 62500, 3000, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0008, 0, 400)
    Sleep(400)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetFlags(0x0008, 0x0004)
    OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)
    Sleep(400)

    OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)
    Sleep(400)

    OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)
    Sleep(400)

    ChrSetDirection(0x0008, 180, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrSetDirection(0x0008, 0, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
