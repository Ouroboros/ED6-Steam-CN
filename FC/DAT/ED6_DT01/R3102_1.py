import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3102_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3102_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3102.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x28D2
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
            word_3A         = 144,
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    Fade(1000)
    CameraMove(-19410, 40, -38900, 0)
    SetChrPos(0x0101, -18990, 50, -38440, 180)
    SetChrPos(0x0102, -20320, 20, -39060, 135)
    SetChrPos(0x0107, -19090, 50, -36910, 180)
    OP_6C(300000, 0)
    CameraSetDistance(3000, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2060180552V呜～……\n',
            '难道出故障了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180553V啊……\n',
            '看来的确是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180554V偏偏坏在平原正中间，\n',
            '真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180555V#501F请问这里是怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180556V你们是不是遇到什么麻烦了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 400)
    ChrTurnDirection(0x0009, 0x0101, 400)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Return,
        ),
        'loc_30A',
    )

    ChrTalk(
        0x0008,
        (
            '#2060180557V啊啊，我以为是谁呢……\n',
            '原来是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180558V#000F您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180559V#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2070180560V是认识的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180561V嗯，\n',
            '他们和我一样也是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180562V#010F不过我们还只是准游击士。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    Jump('loc_4A0')

    def _loc_30A(): pass

    label('loc_30A')

    ChrTalk(
        0x0009,
        (
            '#2070180563V怎么了？\n',
            '你们几个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180564V咦？那个徽章……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180565V难道说你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180566V#006F嗯，对啊，\n',
            '我们是准游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180567V我叫艾丝蒂尔，\n',
            '旁边的那位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180568V#010F我叫约修亚，请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180569V哟，\n',
            '这么年轻就当上游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180570V对了，你们就是传说中的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180571V请多指教，我叫王，\n',
            '是蔡斯支部所属的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180572V你们的事情，\n',
            '我在雾香小姐那里听说过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A0(): pass

    label('loc_4A0')

    ChrTalk(
        0x0008,
        (
            '#2060180573V可是你们\n',
            '为什么会到这里来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180574V#000F啊，是这样的。\n',
            '我们正在护送这个女孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180575V#060F啊，是的。\n',
            '我要去一趟亚尔摩村……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180576V所以就让艾丝蒂尔姐姐她们送我过去。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0107, 400)

    ChrTalk(
        0x0009,
        (
            '#2070180577V哦，我就说在哪儿见过你，\n',
            '你不是提妲小妹妹吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180578V又是博士叫你去的吧？\n',
            '每次要你去做的事情都很辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180579V#067F呵呵…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180580V#000F……王先生，\n',
            '你们在这里做什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180581V刚才看你们的样子，\n',
            '好像遇到了什么麻烦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180582V啊，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180583V我们打算把运输车\n',
            '护送到沃尔费堡垒去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180584V刚走到这里\n',
            '车子就突然出毛病了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180585V我想应该是\n',
            '导力引擎出了故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180586V刚开始发出咔嗒咔嗒的声音时，\n',
            '我还以为是路况不平引起的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180587V#003F哎呀，这可就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0028, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_8E5',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010180588V#002F啊，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180589V公告板上有一个寻找运输车的委托。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180590V难道说就是王先生你们这辆吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180591V#012F嗯，应该就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180592V这样啊……\n',
            '原来协会也开始找我们了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180593V#063F唔～可是……\n',
            '是导力引擎出了故障。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180594V如果是这个原因，\n',
            '那么不把内部用的\n',
            '驱动导力器全部更换掉是不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_943')

    def _loc_8E5(): pass

    label('loc_8E5')

    ChrTalk(
        0x0107,
        (
            '#0070180595V#063F是导力引擎的故障吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180596V那么不把内部用的\n',
            '驱动导力器全部更换掉是不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_943(): pass

    label('loc_943')

    @scena.Lambda('lambda_0949')
    def lambda_0949():
        ChrTurnDirection(0x0102, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0949)

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180597V#004F啊…………？\n',
            '现在不能进行修理吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070180598V#063F因为导力引擎的核心\n',
            '是极为精密的机械……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180599V如果要拆开修理，\n',
            '就必须有相应的设备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180600V只用简单的工具是无从下手的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180601V#013F原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180602V要在室外修理的确是比较困难。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180603V#012F………………嗯！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    SetChrDirection(0x0102, 215, 400)
    Sleep(800)

    OP_21()
    PlayBGM(86)

    @scena.Lambda('lambda_0AB6')
    def lambda_0AB6():
        ChrTurnDirection(0x0008, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AB6)

    @scena.Lambda('lambda_0AC4')
    def lambda_0AC4():
        ChrTurnDirection(0x0107, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0AC4)

    @scena.Lambda('lambda_0AD2')
    def lambda_0AD2():
        ChrTurnDirection(0x0009, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0AD2)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180604V#002F怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180605V#012F嗯，这个感觉是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B29')
    def lambda_0B29():
        CameraMove(-27480, -30, -42850, 3000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0B29)

    @scena.Lambda('lambda_0B41')
    def lambda_0B41():
        OP_6C(270000, 3000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_0B41)

    Sleep(700)

    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 8)
    SetChrPos(0x000A, -26150, -50, -46240, 45)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 8)
    SetChrPos(0x000B, -27650, 30, -47100, 45)
    ClearChrFlags(0x000C, 0x0080)
    SetChrChipByIndex(0x000C, 8)
    SetChrPos(0x000C, -28470, -90, -45180, 45)
    ClearChrFlags(0x000D, 0x0080)
    SetChrChipByIndex(0x000D, 8)
    SetChrPos(0x000D, -30510, -30, -44920, 45)
    ClearChrFlags(0x000E, 0x0080)
    SetChrChipByIndex(0x000E, 8)
    SetChrPos(0x000E, -29310, -90, -43270, 45)
    ClearChrFlags(0x000F, 0x0080)
    SetChrChipByIndex(0x000F, 8)
    SetChrPos(0x000F, -30380, 0, -46760, 45)
    CreateThread(0x000A, 0x01, 0x01, 0x0004)
    CreateThread(0x000C, 0x01, 0x01, 0x0006)
    CreateThread(0x000E, 0x01, 0x01, 0x0008)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0C3B')
    def lambda_0C3B():
        SetChrDirection(0x0008, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C3B)

    @scena.Lambda('lambda_0C49')
    def lambda_0C49():
        SetChrDirection(0x0101, 215, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C49)

    Sleep(150)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0C8A')
    def lambda_0C8A():
        SetChrDirection(0x0009, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C8A)

    @scena.Lambda('lambda_0C98')
    def lambda_0C98():
        SetChrDirection(0x0107, 215, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0C98)

    CreateThread(0x000B, 0x01, 0x01, 0x0005)
    CreateThread(0x000D, 0x01, 0x01, 0x0007)
    Sleep(100)

    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 9)
    SetChrChipByIndex(0x0008, 5)
    SetChrChipByIndex(0x0107, 13)
    CreateThread(0x000F, 0x01, 0x01, 0x0009)
    WaitForThreadExit(0x000F, 0x0001)

    @scena.Lambda('lambda_0CD9')
    def lambda_0CD9():
        CameraMove(-21250, -20, -39110, 1500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0CD9)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(120)

    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    WaitForThreadExit(0x0011, 0x0001)
    OP_94(0x01, 0x0009, 0x00B4, 0x000000C8, 0x000003E8, 0x00)

    ChrTalk(
        0x0009,
        (
            '#2070180606V魔、魔兽！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0014, 0x0080)
    SetChrChipByIndex(0x0014, 8)
    SetChrPos(0x0014, -22130, -40, -48120, 26)
    SetChrFlags(0x0014, 0x0004)

    ExecExpressionWithValue(
        0x0014,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_4A(0x0014, 0)
    SetChrSubChip(0x0014, 4)
    ChrJumpTo(0x0014, -21360, 2000, -45270, 2200, 5000)
    SetChrChipByIndex(0x0014, 7)
    OP_4B(0x0014, 0)

    @scena.Lambda('lambda_0D9B')
    def lambda_0D9B():
        CameraMove(-19870, -30, -41930, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0D9B)

    @scena.Lambda('lambda_0DB3')
    def lambda_0DB3():
        OP_6C(180000, 1500)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_0DB3)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0014, 400)
    WaitForThreadExit(0x0011, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010180607V#005F王先生！上面！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0014, 400)
    SetChrChipByIndex(0x0014, 8)
    ChrWalkTo(0x0014, -20100, 2000, -43220, 7000, 0x00)

    ExecExpressionWithValue(
        0x0014,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_4A(0x0014, 0)
    SetChrSubChip(0x0014, 4)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0E68')
    def lambda_0E68():
        ChrTurnDirection(0x0009, 0x0014, 400)
        Yield()

        Jump('lambda_0E68')

    DispatchAsync2(0x0009, 0x0001, lambda_0E68)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_0E7E')
    def lambda_0E7E():
        ChrJumpTo(0x0014, -19710, -40, -41390, 100, 5000)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_0E7E)

    ExecExpressionWithValue(
        0x0014,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    CreateThread(0x0008, 0x01, 0x01, 0x000D)
    Sleep(120)

    TerminateThread(0x0014, 0xFF)
    SetChrFlags(0x0014, 0x0020)
    SetChrFlags(0x0014, 0x0004)
    SetChrFlags(0x0014, 0x0040)
    PlayEffect(0x08, 0xFF, 0x0014, 0, 2000, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x0014, 2)
    SetChrSubChip(0x0014, 0)
    ChrMoveTo(0x0014, -20240, 800, -42020, 8000, 0x00)
    PlayEffect(0x12, 0xFF, 0x00FF, -20370, 800, -42730, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    SetChrPos(0x0014, -20240, 1000, -42020, 0)

    ExecExpressionWithValue(
        0x0014,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x2C,
        (
            (Expr.PushLong, 0xFFFF15A0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0014, 0x03, 0x01, 0x000F)
    CreateThread(0x0014, 0x02, 0x01, 0x0010)
    Sleep(400)

    ChrJumpTo(0x000B, -26370, -70, -44840, 500, 3000)
    WaitForThreadExit(0x0014, 0x0002)
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x0014, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#2070180608V#1P哇、哇哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)
    SetChrChipByIndex(0x0008, 5)
    ChrTurnDirection(0x0008, 0x000B, 400)
    OP_4B(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#2060180609V#1P布鲁诺先生，请退后！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180610V#1P哦、哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_1073')
    def lambda_1073():
        ChrWalkTo(0x0009, -16230, -30, -39360, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1073)

    @scena.Lambda('lambda_108E')
    def lambda_108E():
        CameraMove(-15540, -50, -40250, 2000)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_108E)

    ClearChrFlags(0x0011, 0x0080)
    SetChrChipByIndex(0x0011, 8)
    SetChrPos(0x0011, -19100, -30, -50010, 43)
    ClearChrFlags(0x0012, 0x0080)
    SetChrChipByIndex(0x0012, 8)
    SetChrPos(0x0012, -19100, -30, -50010, 43)
    ClearChrFlags(0x0013, 0x0080)
    SetChrChipByIndex(0x0013, 8)
    SetChrPos(0x0013, -19100, -30, -50010, 43)
    CreateThread(0x0011, 0x01, 0x01, 0x000A)
    Sleep(400)

    CreateThread(0x0012, 0x01, 0x01, 0x000B)
    Sleep(400)

    CreateThread(0x0013, 0x01, 0x01, 0x000C)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0009, 0x0012, 400)
    ChrJumpToRelative(0x0009, 0, 0, 0, 800, 12000)

    @scena.Lambda('lambda_114B')
    def lambda_114B():
        CameraMove(-19630, 60, -38120, 2000)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_114B)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0009, -17450, 0, -37530, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x0012, 400)
    WaitForThreadExit(0x0014, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#2070180611V哇、哇～！\n',
            '后面也来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(120)

    OP_62(0x0107, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_1203')
    def lambda_1203():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1203)

    @scena.Lambda('lambda_1211')
    def lambda_1211():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1211)

    ChrTurnDirection(0x0008, 0x0012, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180612V………………嗯？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180613V#012F王先生，\n',
            '后面的就拜托你了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180614V这边的就由我们来对付。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180615V#1P好、好的……放心吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_12B8')
    def lambda_12B8():
        SetChrDirection(0x00FE, 215, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12B8)

    SetChrDirection(0x0107, 215, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180616V#005F好！\n',
            '交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x000A, 8)
    SetChrChipByIndex(0x000B, 8)
    SetChrChipByIndex(0x000C, 8)
    SetChrChipByIndex(0x000D, 8)
    SetChrChipByIndex(0x000E, 8)
    SetChrChipByIndex(0x000F, 8)

    @scena.Lambda('lambda_1320')
    def lambda_1320():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1320)

    @scena.Lambda('lambda_1336')
    def lambda_1336():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1336)

    @scena.Lambda('lambda_134C')
    def lambda_134C():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_134C)

    @scena.Lambda('lambda_1362')
    def lambda_1362():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1362)

    @scena.Lambda('lambda_1378')
    def lambda_1378():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1378)

    @scena.Lambda('lambda_138E')
    def lambda_138E():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_138E)

    SetChrChipByIndex(0x0008, 6)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0008, 0x1000)
    CreateThread(0x0008, 0x01, 0x01, 0x000E)
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    ClearChrFlags(0x0008, 0x0040)
    ClearChrFlags(0x0009, 0x0040)
    ClearChrFlags(0x0008, 0x1000)
    Battle(0x000003F6, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_141D'),
        (-1, 'loc_1420'),
    )

    def _loc_141D(): pass

    label('loc_141D')

    OP_B4(0x00)

    Return()

    def _loc_1420(): pass

    label('loc_1420')

    EventBegin(0x00)
    FadeIn(1000, 0)
    CameraMove(-18050, 20, -37820, 0)
    CameraSetDistance(3000, 0)
    OP_6C(180000, 0)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrPos(0x0008, -17230, 10, -39580, 104)
    SetChrPos(0x0009, -17250, 20, -36060, 199)
    SetChrPos(0x0101, -18990, 50, -38440, 225)
    SetChrPos(0x0102, -20320, 20, -39060, 225)
    SetChrPos(0x0107, -19090, 50, -36910, 225)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 9)
    SetChrChipByIndex(0x0107, 13)
    SetChrChipByIndex(0x0008, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010180617V#002F大家总算都平安无事了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180618V#012F嗯，已经把它们击退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0107, 65535)
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070180619V#561F呼……太好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 0)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180620V还好大家都\n',
            '没受到任何伤害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_15B4')
    def lambda_15B4():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_15B4)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2070180621V呼～捡回一条命啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_15E8')
    def lambda_15E8():
        SetChrDirection(0x0101, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15E8)

    @scena.Lambda('lambda_15F6')
    def lambda_15F6():
        SetChrDirection(0x0107, 135, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_15F6)

    @scena.Lambda('lambda_1604')
    def lambda_1604():
        OP_6C(270000, 3500)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1604)

    @scena.Lambda('lambda_1614')
    def lambda_1614():
        CameraMove(-18530, 50, -38340, 3500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1614)

    SetChrFlags(0x0009, 0x0040)
    CreateThread(0x0102, 0x01, 0x01, 0x0011)
    ChrWalkTo(0x0009, -17640, 10, -36470, 1000, 0x00)
    ChrWalkTo(0x0009, -16880, -10, -38350, 1000, 0x00)
    ChrTurnDirection(0x0009, 0x0102, 400)
    ClearChrFlags(0x0009, 0x0040)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x000A, 0x0002)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0107, 0xFF)

    ChrTalk(
        0x0009,
        (
            '#2070180622V嗯…………\n',
            '虽然得救了，\n',
            '但是还要考虑接下来怎么做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180623V嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180624V首先，无论如何\n',
            '也要让这个运输车动起来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180625V#003F可是，\n',
            '刚刚不是已经说过不能修理了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180626V#063F唔～\n',
            '我觉得的确很困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180627V#012F这么说来……\n',
            '除了更换零件以外，\n',
            '的确已经没有其他办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180628V运输车的管理员是\n',
            '中央工房的普罗梅笛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180629V只要问问他，\n',
            '应该可以知道更换用的零件的保管场所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180630V可是，要做到这一点，\n',
            '就必须要回蔡斯一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180631V嗯～真头疼啊。\n',
            '布鲁诺先生，怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180632V要回蔡斯去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2070180633V我认为现在还没这必要，\n',
            '还是再稍微摆弄一下这车子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180634V能动的话当然是最好了。\n',
            '如果实在是动不了，\n',
            '也就只有回蔡斯去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180635V这样啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180636V那就暂时\n',
            '先呆在这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180637V嗯，只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180638V就是这么回事，\n',
            '我们要留在这里\n',
            '继续努力试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180639V#002F嗯，我知道了……\n',
            '王先生你们要注意安全哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180640V没问题，我不会蛮干的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180641V一旦有什么危险，\n',
            '我们会立刻返回城里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180642V那么，提妲小妹妹，\n',
            '你们去亚尔摩的路上也要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070180643V#060F啊，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180644V如果你们有空的话，\n',
            '请帮忙联络一下普罗梅笛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180645V他应该一直都在中央工房\n',
            '三楼的设计室里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180646V#000F嗯，那再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180647V#010F王先生你们务必要注意安全。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【寻找运输车】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    CreateThread(0x0008, 0x01, 0x01, 0x0012)
    CreateThread(0x0009, 0x01, 0x01, 0x0013)
    Sleep(100)

    OP_28(0x0028, 0x04, 0x04)
    OP_28(0x0028, 0x04, 0x02)
    OP_28(0x0028, 0x04, 0x10)
    OP_28(0x0028, 0x01, 0x0001)
    OP_28(0x0028, 0x01, 0x0002)
    OP_28(0x0028, 0x01, 0x0004)
    OP_28(0x0028, 0x01, 0x0008)
    OP_28(0x0028, 0x01, 0x0010)
    OP_28(0x0028, 0x01, 0x0020)
    OP_28(0x0029, 0x04, 0x04)
    OP_28(0x0029, 0x04, 0x02)
    EventEnd(0x00)
    ClearChrFlags(0x0008, 0x0010)
    ClearChrFlags(0x0009, 0x0010)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0003 offset: 0x1C59
@scena.Code('func_03_1C59')
def func_03_1C59():
    EventBegin(0x00)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    Fade(1000)
    CameraMove(-19410, 40, -38900, 0)
    SetChrPos(0x0101, -18990, 50, -38440, 180)
    SetChrPos(0x0102, -20320, 20, -39060, 135)
    SetChrPos(0x0107, -19090, 50, -36910, 180)
    OP_6C(300000, 0)
    CameraSetDistance(3000, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010180754V#000F呼～久等了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0010)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0008, 0x0101, 400)
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180755V哦，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180756V怎么样？\n',
            '导力引擎\n',
            '已经找到了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180757V#001F嗯，已经找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180758V#010F让你们久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180759V哦哦，就是这东西，\n',
            '哎呀，真是帮了大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180760V你们走了之后\n',
            '我又想尽了各种办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180761V但是不管怎样\n',
            '还是没法让车子动起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2060180762V我们本来打算离开的。\n',
            '刚刚正准备商量\n',
            '回蔡斯的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180763V#000F是这样啊，\n',
            '我们能够赶上真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180764V#010F那么就立刻修理运输车吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180765V#060F啊，好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180766V#061F交给我来办吧，\n',
            '啪啪几下就可以更换好导力引擎了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180767V啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0107, 400)

    ChrTalk(
        0x0009,
        (
            '#2070180768V多谢你帮忙了，小姑娘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F71')
    def lambda_1F71():
        ChrWalkTo(0x0009, -19290, -30, -41320, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1F71)

    CreateThread(0x0008, 0x01, 0x01, 0x0014)
    SetChrFlags(0x0107, 0x0040)
    ChrWalkTo(0x0107, -17710, 20, -38200, 1500, 0x00)
    FadeOut(1000, 0, -1)
    ChrWalkTo(0x0107, -19050, 30, -40850, 1500, 0x00)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    OP_0D()
    CameraMove(-18190, 10, -40240, 0)
    SetChrPos(0x0107, -17490, 10, -39610, 182)
    SetChrPos(0x0008, -19060, -10, -40450, 145)
    SetChrChipByIndex(0x0009, 14)
    CameraSetDistance(3000, 0)
    OP_6C(276000, 0)
    SetChrPos(0x0010, -17420, -20, -41550, 51)
    SetChrFlags(0x0010, 0x0040)
    OP_A1(0x0010, 0x0000)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0002)
    OP_71(0x0000, 0x0400)
    OP_71(0x0000, 0x0040)
    Sleep(1)

    ClearChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0009, 0x0040)
    SetChrBattleFlags(0x0009, 0x0020)
    OP_89(0x0009, -17120, 440, -41360, 51)
    SetChrFlags(0x0009, 0x0020)
    LoadEffect(0x00, 'map\\\\mp024_00.eff')
    ChrTurnDirection(0x0101, 0x0009, 0)
    Sleep(400)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070180769V#060F#4P……这样就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x0107, 0x00B4, 0x000005DC, 0x000007D0, 0x00)

    ChrTalk(
        0x0009,
        (
            '#2070180770V……那么，\n',
            '动起来了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(157, 0x00, 0x64)
    Sleep(400)

    PlaySE(207, 0x01, 0x55)

    ChrTalk(
        0x0107,
        (
            '#0070180771V#062F#4P……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180772V#060F#4P……嗯，没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180773V呼～\n',
            '这下总算可以把货物运送过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180774V真不愧是\n',
            '拉赛尔博士的孙女啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180775V虽然还在上主日学校的年纪，\n',
            '维修的能力却是顶呱呱哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180776V#067F#4P嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180777V好了，我们该出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2070180778V你们也要注意安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180779V#000F#2P嗯，我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2060180780V那么就再见了，\n',
            '今天多亏了你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180781V#010F#2P路上小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22CF')
    def lambda_22CF():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_22CF')

    DispatchAsync2(0x0000, 0x0001, lambda_22CF)

    @scena.Lambda('lambda_22E0')
    def lambda_22E0():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_22E0')

    DispatchAsync2(0x0001, 0x0001, lambda_22E0)

    @scena.Lambda('lambda_22F1')
    def lambda_22F1():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_22F1')

    DispatchAsync2(0x0002, 0x0001, lambda_22F1)

    SetChrDirection(0x0008, 51, 400)
    SetChrFlags(0x0008, 0x0040)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 40)
    OP_70(0x0000, 200)

    @scena.Lambda('lambda_2321')
    def lambda_2321():
        CameraMove(-14070, -40, -37570, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_2321)

    OP_24(0x00CF, 0x64)

    @scena.Lambda('lambda_233D')
    def lambda_233D():
        OP_94(0x01, 0x0010, 0x0000, 0x00004650, 0x000006A4, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_233D)

    PlayEffect(0x00, 0x00, 0x0010, 0, 200, -7000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x01, 0x0010, 0, 200, -4000, 0, 0, 0, 1000, 500, 500, 0x00FF, 0, 0, 0, 0)
    ChrWalkTo(0x0008, -17490, 10, -39610, 1700, 0x00)
    SetChrDirection(0x0008, 51, 0)

    @scena.Lambda('lambda_23D8')
    def lambda_23D8():
        OP_94(0x01, 0x0008, 0x0000, 0x00004E20, 0x000006A4, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_23D8)

    WaitForThreadExit(0x0010, 0x0003)
    Sleep(1000)

    @scena.Lambda('lambda_23F8')
    def lambda_23F8():
        OP_69(0x0101, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_23F8)

    CreateThread(0x0000, 0x03, 0x01, 0x0016)
    WaitForThreadExit(0x0010, 0x0001)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    OP_72(0x0000, 0x0020)
    RemoveItem(0x0346, 1)
    OP_28(0x0029, 0x01, 0x0040)
    OP_28(0x0029, 0x04, 0x10)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    OP_71(0x0000, 0x0004)
    WaitForThreadExit(0x0010, 0x0003)
    WaitForThreadExit(0x0000, 0x0003)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【修理运输车】',
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

    Return()

# id: 0x0004 offset: 0x24AA
@scena.Code('func_04_24AA')
def func_04_24AA():
    OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x000007D0, 0x00)
    SetChrChipByIndex(0x00FE, 7)

    Return()

# id: 0x0005 offset: 0x24BF
@scena.Code('func_05_24BF')
def func_05_24BF():
    OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x000007D0, 0x00)
    SetChrChipByIndex(0x00FE, 7)

    Return()

# id: 0x0006 offset: 0x24D4
@scena.Code('func_06_24D4')
def func_06_24D4():
    OP_94(0x01, 0x00FE, 0x0000, 0x000005DC, 0x000007D0, 0x00)
    OP_4A(0x00FE, 0)
    SetChrSubChip(0x00FE, 4)
    ChrJumpTo(0x00FE, -24770, 60, -41600, 800, 1000)
    OP_4B(0x00FE, 0)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x000007D0, 0x00)
    SetChrChipByIndex(0x00FE, 7)

    Return()

# id: 0x0007 offset: 0x251C
@scena.Code('func_07_251C')
def func_07_251C():
    OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x000007D0, 0x00)
    SetChrChipByIndex(0x00FE, 7)

    Return()

# id: 0x0008 offset: 0x2531
@scena.Code('func_08_2531')
def func_08_2531():
    OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x000007D0, 0x00)
    SetChrChipByIndex(0x00FE, 7)

    Return()

# id: 0x0009 offset: 0x2546
@scena.Code('func_09_2546')
def func_09_2546():
    OP_94(0x01, 0x00FE, 0x0000, 0x00000FA0, 0x000007D0, 0x00)
    SetChrChipByIndex(0x00FE, 7)

    Return()

# id: 0x000A offset: 0x255B
@scena.Code('func_0A_255B')
def func_0A_255B():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -16020, 10, -44260, 5000, 0x00)

    @scena.Lambda('lambda_257A')
    def lambda_257A():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_257A')

    DispatchAsync2(0x00FE, 0x0002, lambda_257A)

    ChrMoveTo(0x00FE, -13820, -40, -38890, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 7)
    TerminateThread(0x00FE, 0x02)

    Return()

# id: 0x000B offset: 0x25A3
@scena.Code('func_0B_25A3')
def func_0B_25A3():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -16020, 10, -44260, 5000, 0x00)

    @scena.Lambda('lambda_25C2')
    def lambda_25C2():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_25C2')

    DispatchAsync2(0x00FE, 0x0002, lambda_25C2)

    ChrMoveTo(0x00FE, -14030, -90, -41170, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 7)
    TerminateThread(0x00FE, 0x02)

    Return()

# id: 0x000C offset: 0x25EB
@scena.Code('func_0C_25EB')
def func_0C_25EB():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -16020, 10, -44260, 5000, 0x00)

    @scena.Lambda('lambda_260A')
    def lambda_260A():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_260A')

    DispatchAsync2(0x00FE, 0x0002, lambda_260A)

    ChrMoveTo(0x00FE, -15520, -60, -42450, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 7)
    TerminateThread(0x00FE, 0x02)

    Return()

# id: 0x000D offset: 0x2633
@scena.Code('func_0D_2633')
def func_0D_2633():
    SetChrDirection(0x0008, 225, 0)
    TerminateThread(0x0008, 0x00)
    SetChrChipByIndex(0x0008, 11)
    PlaySE(501, 0x00, 0x64)
    OP_99(0x0008, 0x00, 0x03, 3000)
    Sleep(200)

    OP_99(0x0008, 0x04, 0x07, 3000)
    ChrJumpToRelative(0x0009, 0, 0, 0, 800, 12000)

    Return()

# id: 0x000E offset: 0x2677
@scena.Code('func_0E_2677')
def func_0E_2677():
    ChrWalkTo(0x00FE, -17710, 30, -39470, 5000, 0x00)

    @scena.Lambda('lambda_2691')
    def lambda_2691():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2691')

    DispatchAsync2(0x00FE, 0x0002, lambda_2691)

    ChrMoveTo(0x00FE, -16340, -20, -38950, 5000, 0x00)
    TerminateThread(0x00FE, 0x02)

    Return()

# id: 0x000F offset: 0x26B5
@scena.Code('func_0F_26B5')
def func_0F_26B5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_26F9',
    )

    SetChrDirection(0x00FE, 45, 1000)
    SetChrDirection(0x00FE, 90, 1000)
    SetChrDirection(0x00FE, 135, 1000)
    SetChrDirection(0x00FE, 180, 1000)
    SetChrDirection(0x00FE, 225, 1000)
    SetChrDirection(0x00FE, 270, 1000)
    SetChrDirection(0x00FE, 315, 1000)
    SetChrDirection(0x00FE, 360, 1000)

    Jump('func_0F_26B5')

    def _loc_26F9(): pass

    label('loc_26F9')

    Return()

# id: 0x0010 offset: 0x26FA
@scena.Code('func_10_26FA')
def func_10_26FA():
    ChrMoveTo(0x0014, -23720, 200, -44920, 8000, 0x00)
    PlayEffect(0x12, 0xFF, 0x00FF, -23720, 30, -44920, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlaySE(523, 0x00, 0x5F)

    @scena.Lambda('lambda_274E')
    def lambda_274E():
        ChrSetRGBAMask(0x0014, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_274E)

    ChrJumpTo(0x0014, -24920, 200, -44910, 500, 4000)
    ChrJumpTo(0x0014, -25940, 200, -45810, 500, 2000)

    Return()

# id: 0x0011 offset: 0x2789
@scena.Code('func_11_2789')
def func_11_2789():
    ChrWalkTo(0x0102, -19790, 20, -39430, 1000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0012 offset: 0x27A5
@scena.Code('func_12_27A5')
def func_12_27A5():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x0008, -19060, -10, -40450, 2000, 0x00)
    SetChrDirection(0x0008, 145, 400)
    ClearChrFlags(0x00FE, 0x0040)

    Return()

# id: 0x0013 offset: 0x27CB
@scena.Code('func_13_27CB')
def func_13_27CB():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x0009, -17490, 10, -39610, 2000, 0x00)
    SetChrDirection(0x0009, 182, 400)
    ClearChrFlags(0x00FE, 0x0040)

    Return()

# id: 0x0014 offset: 0x27F1
@scena.Code('func_14_27F1')
def func_14_27F1():
    ChrWalkTo(0x0008, -20940, -50, -40140, 3000, 0x00)
    SetChrDirection(0x0008, 135, 400)

    Return()

# id: 0x0015 offset: 0x280D
@scena.Code('func_15_280D')
def func_15_280D():
    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)

    Return()

# id: 0x0016 offset: 0x284A
@scena.Code('func_16_284A')
def func_16_284A():
    Sleep(4000)

    OP_24(0x00CF, 0x5F)
    Sleep(100)

    OP_24(0x00CF, 0x5A)
    Sleep(100)

    OP_24(0x00CF, 0x55)
    Sleep(100)

    OP_24(0x00CF, 0x50)
    Sleep(100)

    OP_24(0x00CF, 0x4B)
    Sleep(100)

    OP_24(0x00CF, 0x46)
    Sleep(100)

    OP_24(0x00CF, 0x41)
    Sleep(100)

    OP_24(0x00CF, 0x3C)
    Sleep(100)

    OP_24(0x00CF, 0x37)
    Sleep(100)

    OP_23(0x00CF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
