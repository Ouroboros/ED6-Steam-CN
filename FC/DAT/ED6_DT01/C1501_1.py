import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1501_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1501_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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

# id: 0xFFFF offset: 0x1EE1
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x65
@scena.Code('Init')
def Init():
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
        'loc_1E13',
    )

    OP_28(0x001F, 0x01, 0x4000)
    OP_28(0x001F, 0x04, 0x08)
    ClearMapFlags(0x00000001)
    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E6',
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

    Jump('loc_17F')

    def _loc_E6(): pass

    label('loc_E6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_131',
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

    Jump('loc_17F')

    def _loc_131(): pass

    label('loc_131')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17F',
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

    def _loc_17F(): pass

    label('loc_17F')

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_0199')
    def lambda_0199():
        CameraMove(-101100, 3350, 66300, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0199)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_01C3')
    def lambda_01C3():
        ChrWalkTo(0x0008, -101100, 3350, 66300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_01C3)

    @scena.Lambda('lambda_01DE')
    def lambda_01DE():
        ChrWalkTo(0x0009, -101300, 3350, 66200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_01DE)

    @scena.Lambda('lambda_01F9')
    def lambda_01F9():
        ChrWalkTo(0x000A, -101100, 3350, 65900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_01F9)

    @scena.Lambda('lambda_0214')
    def lambda_0214():
        ChrWalkTo(0x000B, -101200, 3350, 66500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0214)

    WaitForThreadExit(0x0008, 0x0001)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0105, 0x0040)

    @scena.Lambda('lambda_0243')
    def lambda_0243():
        ChrWalkTo(0x0101, -96100, 4000, 73700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0243)

    @scena.Lambda('lambda_025E')
    def lambda_025E():
        ChrWalkTo(0x0102, -95100, 4000, 74700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_025E)

    @scena.Lambda('lambda_0279')
    def lambda_0279():
        ChrWalkTo(0x0105, -94100, 4000, 75700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0279)

    SetChrDirection(0x0008, 0, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)
    SetChrDirection(0x0008, 180, 400)
    CreateThread(0x0008, 0x01, 0x01, 0x0002)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_02CF')
    def lambda_02CF():
        ChrWalkTo(0x0009, -103900, 2100, 63700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_02CF)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_02EF')
    def lambda_02EF():
        ChrWalkTo(0x000A, -102300, 2500, 64000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_02EF)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_030F')
    def lambda_030F():
        ChrWalkTo(0x000B, -101000, 2650, 63200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_030F)

    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_0334')
    def lambda_0334():
        ChrWalkTo(0x0009, -103900, 2100, 59900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0334)

    @scena.Lambda('lambda_034F')
    def lambda_034F():
        ChrWalkTo(0x0101, -101700, 2400, 63500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_034F)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_036F')
    def lambda_036F():
        ChrWalkTo(0x000A, -103000, 2100, 61200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_036F)

    @scena.Lambda('lambda_038A')
    def lambda_038A():
        ChrWalkTo(0x0102, -102800, 2600, 64599, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_038A)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_03AA')
    def lambda_03AA():
        ChrWalkTo(0x000B, -100800, 2230, 61000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_03AA)

    @scena.Lambda('lambda_03C5')
    def lambda_03C5():
        ChrWalkTo(0x0105, -101200, 3100, 65500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_03C5)

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 0)
    SetChrChipByIndex(0x0101, 3)

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

    @scena.Lambda('lambda_0435')
    def lambda_0435():
        OP_69(0x000C, 800)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0435)

    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0008, 0)
    SetChrChipByIndex(0x0102, 5)
    WaitForThreadExit(0x0105, 0x0001)
    ChrTurnDirection(0x0105, 0x0008, 0)
    SetChrChipByIndex(0x0105, 7)
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
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
    SetChrFlags(0x0105, 0x1000)
    SetChrChipByIndex(0x0101, 4)
    SetChrChipByIndex(0x0102, 6)
    SetChrChipByIndex(0x0105, 8)

    @scena.Lambda('lambda_04F0')
    def lambda_04F0():
        OP_94(0x01, 0x0101, 0x0000, 0x000002BC, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04F0)

    @scena.Lambda('lambda_0506')
    def lambda_0506():
        OP_94(0x01, 0x0102, 0x0000, 0x000002BC, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0506)

    @scena.Lambda('lambda_051C')
    def lambda_051C():
        OP_94(0x01, 0x0105, 0x0000, 0x000002BC, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_051C)

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
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    ClearChrFlags(0x0105, 0x1000)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 5)
    SetChrChipByIndex(0x0105, 7)
    SetChrPos(0x0101, -101700, 2400, 63500, 180)
    SetChrPos(0x0102, -104300, 2000, 63100, 180)
    SetChrPos(0x0105, -102900, 2500, 64200, 180)
    SetChrPos(0x0137, -102260, 1950, 58980, 356)

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
    SetChrChipByIndex(0x0105, 65535)
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
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_066C')
    def lambda_066C():
        ChrTurnDirection(0x0102, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_066C)

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

    @scena.Lambda('lambda_06D4')
    def lambda_06D4():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06D4)

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

    @scena.Lambda('lambda_0741')
    def lambda_0741():
        OP_69(0x000C, 800)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0741)

    ChrWalkTo(0x0137, -103000, 2100, 61600, 2000, 0x00)
    WaitForThreadExit(0x0137, 0x0001)
    TalkBegin(0x0137)
    ChrTurnDirection(0x0137, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1082',
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

    Jump('loc_1DF8')

    def _loc_1082(): pass

    label('loc_1082')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_17F8',
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
        'loc_11B7',
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

    Jump('loc_11D3')

    def _loc_11B7(): pass

    label('loc_11B7')

    ChrTalk(
        0x0101,
        (
            '#0010160650V#004F哎，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11D3(): pass

    label('loc_11D3')

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

    Jump('loc_1DF8')

    def _loc_17F8(): pass

    label('loc_17F8')

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

    def _loc_1DF8(): pass

    label('loc_1DF8')

    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0137, 0x0004)
    ClearChrFlags(0x0101, 0x0040)
    ClearChrFlags(0x0102, 0x0040)
    ClearChrFlags(0x0137, 0x0040)
    EventEnd(0x00)

    def _loc_1E13(): pass

    label('loc_1E13')

    Return()

# id: 0x0002 offset: 0x1E14
@scena.Code('ReInit')
def ReInit():
    TerminateThread(0x000C, 0x01)

    @scena.Lambda('lambda_1E1E')
    def lambda_1E1E():
        CameraMove(-102000, 1930, 59600, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1E1E)

    ChrWalkTo(0x0008, -102200, 2500, 62500, 3000, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrDirection(0x0008, 0, 400)
    Sleep(400)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrFlags(0x0008, 0x0004)
    OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)
    Sleep(400)

    OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)
    Sleep(400)

    OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)
    Sleep(400)

    SetChrDirection(0x0008, 180, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    SetChrDirection(0x0008, 0, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
